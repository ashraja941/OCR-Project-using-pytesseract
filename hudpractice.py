import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
import socket


'''
def window():
   app = QApplication(sys.argv)
   win = QWidget() 
	
   l1 = QLabel()

   l1.setText("90")
   l1.setFont(QFont('Arial',30))
	
   l1.setAlignment(Qt.AlignCenter)
	
   vbox = QVBoxLayout()
   vbox.addWidget(l1)

   win.setLayout(vbox)
   win.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.X11BypassWindowManagerHint
        )

   win.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignRight,QSize(200, 100),qApp.desktop().availableGeometry()))
   win.show()
   timer = QTimer()
   timer.timeout(l1.setText("1"))
   timer.start(1000)
'''



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignRight,QSize(100, 100),qApp.desktop().availableGeometry()))
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.X11BypassWindowManagerHint
        )
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText("90")
        self.label.setFont(QFont('Arial',30))
        layout.addWidget(self.label)
        self.setLayout(layout)
        timer = QTimer(self)
        timer.timeout.connect(self.server)
        timer.start(1000)
    
    def upd(self):
        fil = open('10.147.18.246:8080/boost/Config.json',)
        boost = json.load(fil)
        self.label.setText(boost["boost"])

    def server(self):
        boost = s.recv(1024)
        boost = boost.decode()
        self.label.setText(str(boost))



if __name__ == '__main__':
    s=socket.socket()
    host = "192.168.56.1"
    port = 1234
    s.connect((host,port))
    print("Connected...\n")

    App = QApplication(sys.argv)
    window = Window()
    window.show()
    App.exit(App.exec_())