# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(828, 443)
        Widget.setStyleSheet(u"/* Dark Fancy Theme */\n"
"\n"
"QWidget {\n"
"    background-color: #121212;\n"
"    color: #E0E0E0;\n"
"    font-family: \"Poppins\", \"Montserrat\", \"Segoe UI\", sans-serif;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #121212;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #1E1E1E;\n"
"    color: #E0E0E0;\n"
"    border-bottom: 1px solid #292929;\n"
"    font-family: \"Poppins\", sans-serif;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 5px 15px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: #333;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #292929;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 8px 25px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #333;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2A2A2A;\n"
"    border: 1px solid #333;\n"
"   "
                        " border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    color: #E0E0E0;\n"
"    font-weight: bold;\n"
"    font-size: 14pt;\n"
"    font-family: \"Poppins\", sans-serif;\n"
"    transition: background-color 0.3s, transform 0.2s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #444;\n"
"    transform: scale(1.05);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666;\n"
"    transform: scale(0.95);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #333;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #E0E0E0;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #333;\n"
"    border-radius: 4px;\n"
"    color: #E0E0E0;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #1E1E1E;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertic"
                        "al {\n"
"    background: #555;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background-color: #1E1E1E;\n"
"    border-top: 1px solid #292929;\n"
"    font-family: \"Poppins\", sans-serif;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #333;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #E0E0E0;\n"
"    font-family: \"Montserrat\", sans-serif;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1E1E1E;\n"
"    selection-background-color: #444;\n"
"    border: 1px solid #333;\n"
"}\n"
"")
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(258, 70, 281, 207))
        self.gridLayoutWidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.join_btn = QPushButton(self.gridLayoutWidget)
        self.join_btn.setObjectName(u"join_btn")
        self.join_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.join_btn, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.sessionid_input = QLineEdit(self.gridLayoutWidget)
        self.sessionid_input.setObjectName(u"sessionid_input")
        self.sessionid_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.sessionid_input, 1, 0, 1, 1)

        self.password_input = QLineEdit(self.gridLayoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.password_input, 2, 0, 1, 1)

        self.create_btn = QPushButton(Widget)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setGeometry(QRect(330, 290, 141, 41))
        self.create_btn.setStyleSheet(u"")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.join_btn.setText(QCoreApplication.translate("Widget", u"Join", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#26a269;\">Enter A Party!</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#26a269;\">Or Create A Party</span></p></body></html>", None))
        self.sessionid_input.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter Session ID", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Widget", u"Password", None))
        self.create_btn.setText(QCoreApplication.translate("Widget", u"Create", None))
    # retranslateUi

