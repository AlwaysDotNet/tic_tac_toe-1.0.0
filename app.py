from PyQt6.QtWidgets import QApplication
from sys import argv, exit
from gameui import GameUI

if __name__ == "__main__":
    app = QApplication(argv)
    gm = GameUI()
    gm.show()
    exit(app.exec())
    