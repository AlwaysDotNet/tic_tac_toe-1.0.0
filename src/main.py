from gamewindow import GameWindow
from PyQt6.QtWidgets import QApplication
from sys import argv

if __name__ == "__main__":
    app = QApplication(argv)
    sg = GameWindow()
    sg.show()
    exit(app.exec())