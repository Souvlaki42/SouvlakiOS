import sys, globals
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon

globals.cmd("Calendar")

class Calendar(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(500)
        self.setStyleSheet("""
            QWidget {
                font-size: 50px;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        layout.addWidget(self.dateEdit)

        self.todayButton = QPushButton("&Today", clicked=self.setToday)
        self.dateEdit.calendarWidget().layout().addWidget(self.todayButton)

    def setToday(self):
        today = QDate().currentDate()
        self.dateEdit.calendarWidget().setSelectedDate(today)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app2 = Calendar()
    app.setApplicationName("Calendar")
    app2.setWindowIcon(QIcon("images/logo.png"))
    app2.show()

    sys.exit(app.exec_())   