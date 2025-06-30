import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, QDate, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.date_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self): 
        self.setWindowTitle('Parwesh klok')

        vbox = QVBoxLayout()
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
            color: green;
            font-size: 120px;
            font-weight: bold;
            font-family: 'Segoe UI', Arial, sans-serif;
            text-shadow: 2px 2px 8px #FF0000;
        """)

        
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("""
            color: #CCCCCC;
            font-size: 32px;
            font-family: 'Segoe UI', Arial, sans-serif;
        """)

        
        self.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:1,
                stop:0 #000000, stop:1 #1a1a1a
            );
        """)

        
        self.update_time()

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        
        self.adjustSize()

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss AP')
        current_date = QDate.currentDate().toString('dddd, dd MMMM yyyy')
        self.time_label.setText(current_time)
        self.date_label.setText(current_date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
