import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight, Qt.AlignRight,
                QSize(200, 50),
                qApp.desktop().availableGeometry()
        ))


    def mousePressEvent(self, event):
        QtWidgets.qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()