import sys
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from gui import Ui_MainWindow
from client import Client
sys.path.append('video_processing')
sys.path.append('localisation')
from videoProcessing import VideoProcessing
from mapping import mapping
from map_environement import map_environement
import datetime

class Main(Ui_MainWindow, Client, mapping):
    """
    gui for commanding pgU1
    """
    def __init__(self, w):
        self.setupUi(w)
        Client.__init__(self)
        mapping.__init__(self,str(datetime.datetime.now()))
        self.btnConnection.clicked.connect(self.connection_to_pi)
        self.btnCamera.clicked.connect(self.switch_camera)
        self.initMovement()
        self.camera = VideoProcessing()
        self.camera_on_off = False
        self.fps = 30
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(int(1000/self.fps))
        self.timer.timeout.connect(self.get_frame)
        self.map_generation(5,5)
        self.auxiliaire_window()
    
    def auxiliaire_window(self):
        self.map_environement = map_environement(self.currentMap)
        self.layout_map_environement = QtWidgets.QHBoxLayout()
        self.layout_map_environement.addWidget(self.map_environement)
        self.gb_map.setLayout(self.layout_map_environement)
        
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
    def switch_camera(self):
        """ turn the camera on or off"""
        if self.camera_on_off == False:
            self.timer.start()   
            self.camera_on_off = True
            self.capture = self.camera.camera_config()
            self.dimensionsCamera = self.capture.read()[1].shape[1::-1]
            scene = QtWidgets.QGraphicsScene()
            self.screenCamera.setScene(scene)
            
            pixmap = QtGui.QPixmap(*self.dimensionsCamera)
            self.pixmapItem = scene.addPixmap(pixmap)            
        else:
            self.camera.kill_camera()
            self.camera_on_off =False 
            self.timer.stop()
         
    def get_frame(self): 
        _, frame = self.capture.read()
        image = QtGui.QImage(frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(image)
        self.pixmapItem.setPixmap(pixmap)
     
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = Main(w)
    w.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
