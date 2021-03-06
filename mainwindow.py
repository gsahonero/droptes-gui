# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 359)
        MainWindow.setStatusTip("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.homeButtton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButtton.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.homeButtton.setObjectName("homeButtton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(350, 30, 75, 23))
        self.stopButton.setObjectName("stopButton")
        self.vel1Label = QtWidgets.QLabel(self.centralwidget)
        self.vel1Label.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.vel1Label.setObjectName("vel1Label")
        self.vel2Label = QtWidgets.QLabel(self.centralwidget)
        self.vel2Label.setGeometry(QtCore.QRect(60, 220, 47, 13))
        self.vel2Label.setObjectName("vel2Label")
        self.vel1Slider = QtWidgets.QSlider(self.centralwidget)
        self.vel1Slider.setGeometry(QtCore.QRect(60, 110, 291, 22))
        self.vel1Slider.setOrientation(QtCore.Qt.Horizontal)
        self.vel1Slider.setObjectName("vel1Slider")
        self.vel2Slider = QtWidgets.QSlider(self.centralwidget)
        self.vel2Slider.setGeometry(QtCore.QRect(60, 250, 291, 22))
        self.vel2Slider.setOrientation(QtCore.Qt.Horizontal)
        self.vel2Slider.setObjectName("vel2Slider")
        self.fwVel1 = QtWidgets.QPushButton(self.centralwidget)
        self.fwVel1.setGeometry(QtCore.QRect(420, 90, 31, 23))
        self.fwVel1.setObjectName("fwVel1")
        self.bwVel1 = QtWidgets.QPushButton(self.centralwidget)
        self.bwVel1.setGeometry(QtCore.QRect(420, 130, 31, 23))
        self.bwVel1.setObjectName("bwVel1")
        self.fwVel2 = QtWidgets.QPushButton(self.centralwidget)
        self.fwVel2.setGeometry(QtCore.QRect(420, 230, 31, 23))
        self.fwVel2.setObjectName("fwVel2")
        self.bwVel2 = QtWidgets.QPushButton(self.centralwidget)
        self.bwVel2.setGeometry(QtCore.QRect(420, 270, 31, 23))
        self.bwVel2.setObjectName("bwVel2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuAbout.addAction(self.actionVersion)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DropTES GUI"))
        self.homeButtton.setText(_translate("MainWindow", "Home"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.vel1Label.setText(_translate("MainWindow", "Vel 1"))
        self.vel2Label.setText(_translate("MainWindow", "Vel 2"))
        self.fwVel1.setText(_translate("MainWindow", "FW"))
        self.bwVel1.setText(_translate("MainWindow", "BW"))
        self.fwVel2.setText(_translate("MainWindow", "FW"))
        self.bwVel2.setText(_translate("MainWindow", "BW"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
