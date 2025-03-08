# SongRequestsApp

SongRequestsApp is a Python application designed to manage and retrieve song requests during live sessions. It provides an intuitive interface for DJs or event hosts to handle incoming song requests efficiently.

## Features

- **Real-time Song Request Management:** Accept and organize song requests during live events.
- **User-Friendly Interface:** Built with PyQt5 to ensure a responsive and easy-to-use GUI.
- **Session Persistence:** Maintain song request data throughout the session.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/drenchew/SongRequestsApp.git
   cd SongRequestsApp
nstall Dependencies:

It's recommended to use a virtual environment:

python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'

Install the required packages:

    pip install -r requirements.txt

Usage

    Run the Application:

    python widget.py

    Interface Overview:
        Song Request List: Displays incoming song requests.
        Controls: Options to add, remove, or manage song requests.

Development
File Structure

    widget.py: Main application file initializing the GUI and core functionalities.
    ui_form.py: Generated Python file from the Qt Designer .ui file for the main form.
    form.ui: Qt Designer file defining the UI layout.
    requirements.txt: Lists all Python dependencies.

Modifying the UI

If you wish to modify the user interface:

    Open form.ui in Qt Designer.

    Make the desired changes.

    Convert the .ui file to a Python module:

    pyuic5 form.ui -o ui_form.py

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
