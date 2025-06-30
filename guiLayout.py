import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Haxball GUI')
        self.setGeometry(1410, 50, 500, 500)
        self.setWindowIcon(QIcon('gui2.webp'))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel('#1', self)
        label2 = QLabel('#2', self)
        label3 = QLabel('#3', self)
        label4 = QLabel('#4', self)

        label1.setStyleSheet('background-color: blue')
        label2.setStyleSheet('background-color: red')
        label3.setStyleSheet('background-color: green')
        label4.setStyleSheet('background-color: pink')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
