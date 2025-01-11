import sys
import os
import random
import string
from dotenv import load_dotenv
from PySide6.QtWidgets import (
    QApplication, QWidget, QMessageBox, QVBoxLayout, QLabel, QLineEdit,
    QScrollArea, QCheckBox, QPushButton
)
from PySide6.QtCore import QThread, Signal, Qt
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.server_api import ServerApi
from ui_form import Ui_Widget


class CustomCheckBox(QCheckBox):
    def __init__(self,txt,name):
        print("CustomCheckBox created")
        super().__init__(txt)
        self.song_name = name
        self.setStyleSheet("""
            QCheckBox {
                       spacing: 10px;
                       color: #4CAF50;
                   }
            QCheckBox::indicator {
                       width: 20px;
                       height: 20px;
                       border: 2px solid #4CAF50;
                       border-radius: 3px;
                       background-color: white;
                   }
            QCheckBox::indicator:checked {
                       background-color: #4CAF50;
                       border: 2px solid #4CAF50;
                   }
            QCheckBox::indicator:hover {
                       border: 2px solid #81C784;
                   }
               """)


class MongoListenerThread(QThread):
    new_song_signal = Signal(dict)

    def __init__(self, session_id):
        super().__init__()
        self.session_id = session_id
        self.running = True

        try:
            load_dotenv()
            uri = os.getenv("MONGO_URI")
            if not uri:
                raise ValueError("MONGO_URI is not set in the .env file.")
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client["songRq"]
            self.songs_coll = self.db.song_requests
        except (PyMongoError) as e:
            print(f"MongoDB Initialization Error: {e}")
            self.client = None

    def run(self):
        self.loop()


    def stop(self):
        self.running = False
        if self.client:
            self.client.close()

    def loop(self):
        if not self.client:
            return

        while self.running:
            try:
                pipeline = [{"$match": {"fullDocument.session_id": self.session_id}}]
                with self.songs_coll.watch(pipeline, full_document="updateLookup") as stream:
                    for change in stream:
                        self.new_song_signal.emit(change["fullDocument"])

            except Exception as e:
                print(f"Change Stream Error: {e}")
        print("finnished")


class Dashboard(QWidget):
    def __init__(self, session_id, password, parent=None):
        super().__init__(parent)

        self.session_id = session_id
        self.password = password
        self.song_ids = set()
        self.checkboxes = []

        self.setWindowTitle(f"Song Requests - Session {self.session_id}")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout(self)

        self.title_label = QLabel(f"Songs for Session: {self.session_id}")
        self.layout.addWidget(self.title_label)

        self.pass_label = QLabel(f"Password: {self.password}")
        self.layout.addWidget(self.pass_label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search songs...")
        self.search_input.textChanged.connect(self.filter_songs)
        self.layout.addWidget(self.search_input)

        self.scroll_area = QScrollArea()
        self.song_container = QWidget()
        self.song_layout = QVBoxLayout(self.song_container)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.song_container)
        self.layout.addWidget(self.scroll_area)

        self.submit_button = QPushButton("Mark as Played")
        self.submit_button.clicked.connect(self.get_selected_songs)
        self.layout.addWidget(self.submit_button)

        try:
            load_dotenv()
            uri = os.getenv("MONGO_URI")
            if not uri:
                raise ValueError("MONGO_URI is not set in the .env file.")
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client["songRq"]
            self.songs_coll = self.db.song_requests
            self.load_songs()
        except (ConnectionError, ConfigurationError, ValueError) as e:
            print(f"MongoDB Initialization Error: {e}")
            QMessageBox.critical(self, "Error", "Failed to connect to MongoDB.")
            self.close()

        self.listener_thread = MongoListenerThread(self.session_id)
        self.listener_thread.new_song_signal.connect(self.add_song_to_ui)
        self.listener_thread.start()

    def load_songs(self):
        data = self.songs_coll.find({"session_id": self.session_id})
        for item in data:
            self.add_song_to_ui(item)

    def add_song_to_ui(self, item):
        song_id = str(item["_id"])
        if song_id in self.song_ids:
            return
        self.song_ids.add(song_id)

        song = item.get("song", "Unknown Song")
        user = item.get("username", "Anonymous")
        txt = f"{user}: {song}"


        #checkbox = QCheckBox(txt)
        checkbox = CustomCheckBox(txt,song)
        self.song_layout.addWidget(checkbox)
        self.checkboxes.append(checkbox)

    def filter_songs(self):
        search_text = self.search_input.text().lower()
        for checkbox in self.checkboxes:
            checkbox.setVisible(search_text in checkbox.text().lower())

    def get_selected_songs(self):
        for cb in self.checkboxes[:]:
            if cb.isChecked():
                self.song_layout.removeWidget(cb)
                cb.deleteLater()
                self.checkboxes.remove(cb)
                query = {"session_id":self.session_id,"song":cb.song_name}
                deleted =self.songs_coll.delete_one(query)
                print("deleted",deleted)



    def closeEvent(self, event):
       # Signal the thread to stop
       self.listener_thread.stop()
       # Wait for the thread to finish
       self.listener_thread.wait()
       event.accept()


class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        load_dotenv()
        uri = os.getenv("MONGO_URI")
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["songRq"]
        self.sessions_coll = self.db.sessions

        self.ui.join_btn.clicked.connect(self.on_join_button_clicked)
        self.ui.create_btn.clicked.connect(self.on_create_button_clicked)

    def on_join_button_clicked(self):
        session_id = self.ui.sessionid_input.text()
        password = self.ui.password_input.text()

        query = {"session_id": session_id, "password": password}
        user = self.sessions_coll.find_one(query)

        if not user:
            QMessageBox.warning(self, "Error", "Wrong Session ID or Password!")
            return

        self.open_dashboard(session_id, password)

    def on_create_button_clicked(self):
        session_id = self.count_sessions() + 1
        password = self.generate_password()

        data = {"session_id": session_id, "password": password}
        self.sessions_coll.insert_one(data)
        self.open_dashboard(session_id, password)

    def generate_password(self):
        return ''.join(random.choices(string.digits, k=4))

    def count_sessions(self):
        return self.sessions_coll.count_documents({})

    def open_dashboard(self, session_id, password):
        self.dashboard = Dashboard(session_id, password)
        self.dashboard.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
