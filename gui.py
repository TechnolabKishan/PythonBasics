import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Haxball GUI')
        self.setGeometry(1410, 50, 500, 500)
        self.setWindowIcon(QIcon('Hassi (2).webp'))

        
        background = QLabel(self)
        background.setGeometry(0, 0, 500, 500)
        background.setPixmap(QPixmap('gui3.jpg'))
        background.setScaledContents(True)
        background.setGeometry(self.width() - background.width(), self.height() - background.height(), background.width(), background.height())

        
        title = QLabel("Haxball", self)
        title.setFont(QFont('sans-serif', 35))
        title.setGeometry(0, 0, 500, 100)
        title.setStyleSheet('color: yellow; background-color: transparent;')
        title.setAlignment(Qt.AlignCenter)

        self.setStyleSheet('background-color: black;')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
