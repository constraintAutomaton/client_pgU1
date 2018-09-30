from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from PyQt5.QtMultimedia import QSound
from pyqt_map import Ui_Dialog

class pyqt_map(Ui_Dialog):
    def __init__(self, w):
        self.setupUi(w)

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QDialog()
    prog = pyqt_map(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 