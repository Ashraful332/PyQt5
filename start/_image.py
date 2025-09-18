# start with pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("../assets/icon.svg"))

        label = QLabel(self)
        label.setGeometry(0,0,400,300)

        pixmap = QPixmap("../assets/satalite.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
