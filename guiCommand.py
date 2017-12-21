# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCommand.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera = QtWidgets.QWidget(self.centralwidget)
        self.camera.setObjectName("camera")
        self.label = QtWidgets.QLabel(self.camera)
        self.label.setGeometry(QtCore.QRect(420, 110, 55, 16))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.camera)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnTakePicture = QtWidgets.QPushButton(self.widget)
        self.btnTakePicture.setObjectName("btnTakePicture")
        self.horizontalLayout_5.addWidget(self.btnTakePicture)
        self.btnVideo = QtWidgets.QPushButton(self.widget)
        self.btnVideo.setObjectName("btnVideo")
        self.horizontalLayout_5.addWidget(self.btnVideo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnViewPhoto = QtWidgets.QPushButton(self.widget)
        self.btnViewPhoto.setObjectName("btnViewPhoto")
        self.horizontalLayout_6.addWidget(self.btnViewPhoto)
        self.btnViewVideo = QtWidgets.QPushButton(self.widget)
        self.btnViewVideo.setObjectName("btnViewVideo")
        self.horizontalLayout_6.addWidget(self.btnViewVideo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addWidget(self.widget)
        self.mouvement = QtWidgets.QWidget(self.centralwidget)
        self.mouvement.setObjectName("mouvement")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mouvement)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnForward = QtWidgets.QToolButton(self.mouvement)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout_2.addWidget(self.btnForward)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLeft = QtWidgets.QToolButton(self.mouvement)
        self.btnLeft.setObjectName("btnLeft")
        self.horizontalLayout.addWidget(self.btnLeft)
        self.btnStop = QtWidgets.QToolButton(self.mouvement)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.btnRight = QtWidgets.QToolButton(self.mouvement)
        self.btnRight.setObjectName("btnRight")
        self.horizontalLayout.addWidget(self.btnRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnBackward = QtWidgets.QToolButton(self.mouvement)
        self.btnBackward.setObjectName("btnBackward")
        self.horizontalLayout_3.addWidget(self.btnBackward)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addWidget(self.mouvement)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btnTakePicture.setText(_translate("MainWindow", "Take Photo"))
        self.btnVideo.setText(_translate("MainWindow", "Start Video"))
        self.btnViewPhoto.setText(_translate("MainWindow", "Show Photo"))
        self.btnViewVideo.setText(_translate("MainWindow", "Show Video"))
        self.btnForward.setText(_translate("MainWindow", "forward"))
        self.btnLeft.setText(_translate("MainWindow", "left"))
        self.btnStop.setText(_translate("MainWindow", "stop"))
        self.btnRight.setText(_translate("MainWindow", "rigth"))
        self.btnBackward.setText(_translate("MainWindow", "backward"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

