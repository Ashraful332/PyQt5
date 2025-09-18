# start with pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon("../assets/icon.svg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial",140))
        label.setGeometry(0, 0, 500, 200)
        label.setStyleSheet("color: blue;"
        "background-color: red;"
        "font-weight: bold;"
        "font-style: italic;"
        )

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
