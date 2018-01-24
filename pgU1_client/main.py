import sys
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from gui import Ui_MainWindow
from client import Client
sys.path.append(
    r'video_processing')
from videoProcessing import VideoProcessing


class Main(Ui_MainWindow, Client):
    """
    gui for commanding pgU1
    """
    def __init__(self, w):
        self.setupUi(w)
        Client.__init__(self)
        self.btnConnection.clicked.connect(self.connection_to_pi)
        self.initMovement()
    def initMovement(self):
        """
        initiation of the movement related button
        """
        self.btnBackward.clicked.connect(lambda: self.move(self.btnBackward.text()))
        self.btnForward.clicked.connect(lambda: self.move(self.btnForward.text()))
        self.btnRight.clicked.connect(lambda: self.move(self.btnRight.text()))
        self.btnLeft.clicked.connect(lambda: self.move(self.btnLeft.text()))
        self.btnStop.clicked.connect(lambda: self.move(self.btnStop.text()))
    def move(self, mvt):
        """
        function related of movement
        """
        if mvt == 'forward':
            self.send_command('f')
        elif mvt == 'backward':
            self.send_command('b')
        elif mvt == 'rigth':
            self.send_command('trf')
        elif mvt == 'left':
            self.send_command('tlf')
        elif mvt == 'stop':
            self.send_command('stop')
    def connection_to_pi(self):
        """connection to the pi
        """
        self.connection()
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = Main(w)
    w.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
