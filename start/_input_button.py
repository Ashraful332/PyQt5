# start with pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("../assets/icon.svg"))
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,40)
        self.line_edit.setStyleSheet("font-size: 15px;")
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter your name")
    
    def submit(self):
        text = self.line_edit.text()
        print(f"your name is {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
