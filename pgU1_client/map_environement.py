from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from pyqt_map import Ui_Dialog

class map_environement(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,current_map,parent=None):
        super(map_environement,self).__init__(parent)
        self.setupUi(self)
        self.current_map = current_map
        self.populate_map()
        
    def populate_map(self):
        dim = self.current_map.shape
        i = 0
        j = 0
        for el in self.current_map:
            

