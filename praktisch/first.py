# start with pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("../assets/icon.svg"))
        self.Texts()

    def Texts(self):
        # central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # main layout
        layout = QVBoxLayout()

        # heading
        heading = QLabel("Bangladesh", self)
        heading.setFont(QFont("Arial", 24, QFont.Bold))

        # paragraph inside QLabel
        paragraph = QLabel("""
        Bangladesh, officially the People's Republic of Bangladesh, is a country in South Asia. 
        It is the eighth-most populous country in the world and among the most densely populated 
        with a population of over 171 million within an area of 148,460 square kilometres (57,320 sq mi).
        
        Bangladesh shares land borders with India to the north, west, and east, and Myanmar to the southeast. 
        It has a coastline along the Bay of Bengal to its south and is separated from Bhutan and Nepal by the 
        Siliguri Corridor. Dhaka, the capital and largest city, is the nation's political, financial, and cultural centre. 
        Chittagong is the second-largest city and the busiest port of the country.
        
        The territory of modern Bangladesh was a stronghold of many Buddhist and Hindu dynasties in ancient history. 
        Following the Muslim conquest in 1204, the region saw Sultanate and Mughal rule. During the Mughal period, 
        particularly under the Bengal Subah, the region emerged as one of the most prosperous and commercially active 
        parts of the empire, known for its thriving textile industry and agricultural productivity.
        """)
        paragraph.setWordWrap(True)
        paragraph.setFont(QFont("Arial", 12))

        # scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)  # auto resize
        scroll.setWidget(paragraph)      # put paragraph inside scroll

        # add to layout
        layout.addWidget(heading)
        layout.addWidget(scroll)

        central_widget.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
