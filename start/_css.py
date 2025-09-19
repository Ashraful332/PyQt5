# start with pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("../assets/icon.svg"))

        # buttons
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()

    def initUI(self):  # fixed
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox) 

        self.button1.setObjectName("btn1")
        self.button2.setObjectName("btn2")
        self.button3.setObjectName("btn3")

        self.setStyleSheet("""
        QPushButton{
            font-size:20px;
            padding: 15px 75px;
            margin: 25px;
            border: 3px solid;
            border-radius: 15px;
        }
        QPushButton#btn1{
            background-color: #de0404;
        }
        QPushButton#btn2{
            background-color: green;
        }
        QPushButton#btn3{
            background-color: #4a40a3;
        }

        QPushButton#btn1:hover{
            background-color: red;
        }
        QPushButton#btn2:hover{
            background-color: #1ad662;
        }
        QPushButton#btn3:hover{
            background-color: blue;
        }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
