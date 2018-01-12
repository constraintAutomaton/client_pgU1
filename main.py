from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from PyQt5.QtMultimedia import QSound
from guiCommand import Ui_MainWindow
from client import Client
sys.path.append(r'C:\Users\Utilisateur\Documents\Python_Scripts\pgU1_pc_command\video_processing')
from videoProcessing import VideoProcessing

class guiCommand(Ui_MainWindow,Client):
    def __init__(self, w):
        self.setupUi(w)
        Client.__init__(self)
        self.initMovement()
        
    def initMovement(self):
        self.btnBackward.clicked.connect(lambda :self.move(self.btnBackward.text()))
        self.btnForward.clicked.connect(lambda :self.move(self.btnForward.text()))
        self.btnRight.clicked.connect(lambda :self.move(self.btnRight.text()))
        self.btnLeft.clicked.connect(lambda :self.move(self.btnLeft.text()))
        self.btnStop.clicked.connect(lambda :self.move(self.btnStop.text()))
        
    def move(self,mvt):
        if mvt == 'forward':
            self.sendCommand('f')
        elif mvt == 'backward':
            self.sendCommand('b')
        elif mvt == 'rigth':
            self.sendCommand('trf')
        elif mvt == 'left':
            self.sendCommand('tlf')
        elif mvt == 'stop':
            self.sendCommand('stop')
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = guiCommand(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 