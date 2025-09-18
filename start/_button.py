# start with pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("../assets/icon.svg"))
        self.initUI()

    def initUI(self):
        self.button =  QPushButton("Click Me!",self)
        self.button.setGeometry(0,0,200,100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.on_Click)
        self.label = QLabel("Hello",self)

        self.label.setGeometry(0,100,200,100)

    def on_Click(self):
        print("Button Clicked!")
        self.button.setText("Clicked!")
        self.label.setText("Goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
