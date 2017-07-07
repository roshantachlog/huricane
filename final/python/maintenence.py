# -*- coding: utf-8 -*-

####################################################################################################################
# Environment :- python3, PyQt5 ,SQLite database
# Auther      :- Muhammed Roshan
# Company     :- Tachlog
# Created     :- Fri Jul  7 12:31:00 2017
#      
#This program allows the individual controll of each node for maintenance purpose.
# The user can mannually switch ON/OFF the Fan and UV lamp of any node individually.

####################################################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Maintenance(object):
    def setupUi(self, Maintenance):
        Maintenance.setObjectName("Maintenance")
        Maintenance.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(20)
        Maintenance.setFont(font)
        Maintenance.setStyleSheet("background-color: rgb(222, 231, 220);")
        self.centralWidget = QtWidgets.QWidget(Maintenance)
        self.centralWidget.setObjectName("centralWidget")
        self.NODE1 = QtWidgets.QPushButton(self.centralWidget)
        self.NODE1.setGeometry(QtCore.QRect(0, 70, 171, 81))
        self.NODE1.setStyleSheet("background-color: rgb(108, 181, 85);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 255, 0);")
        self.NODE1.setObjectName("NODE1")
        self.NODE2 = QtWidgets.QPushButton(self.centralWidget)
        self.NODE2.setGeometry(QtCore.QRect(0, 150, 171, 81))
        self.NODE2.setStyleSheet("background-color: rgb(166, 229, 149);\n"
"border-color:  rgb(166, 229, 149);\n"
"color: rgb(64, 98, 72);")
        self.NODE2.setObjectName("NODE2")
        self.NODE3 = QtWidgets.QPushButton(self.centralWidget)
        self.NODE3.setGeometry(QtCore.QRect(0, 230, 171, 81))
        self.NODE3.setStyleSheet("background-color: rgb(108, 181, 85);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 255, 0);")
        self.NODE3.setObjectName("NODE3")
        self.NODE4 = QtWidgets.QPushButton(self.centralWidget)
        self.NODE4.setGeometry(QtCore.QRect(0, 310, 171, 81))
        self.NODE4.setStyleSheet("background-color: rgb(108, 181, 85);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 255, 0);")
        self.NODE4.setObjectName("NODE4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 261, 29))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(64, 98, 72);")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(290, 50, 211, 4))
        self.frame.setStyleSheet("background-color:  rgb(64, 98, 72);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(490, 0, 91, 61))
        self.label_2.setStyleSheet("image:url(\'../icons/Home/maintanence.png\');")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(180, 60, 641, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(300, 120, 111, 111))
        self.label_3.setStyleSheet("image:url(\'../icons/maintanence/uv_lamp.png\');")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(570, 120, 118, 111))
        self.label_4.setStyleSheet("image:url(\'../icons/maintanence/fan.png\');")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.LAMP_ON = QtWidgets.QPushButton(self.centralWidget)
        self.LAMP_ON.setGeometry(QtCore.QRect(280, 260, 51, 37))
        self.LAMP_ON.setStyleSheet("background-color: rgb(0, 255,44);")
        self.LAMP_ON.setObjectName("LAMP_ON")
        self.FAN_OFF = QtWidgets.QPushButton(self.centralWidget)
        self.FAN_OFF.setGeometry(QtCore.QRect(640, 260, 51, 37))
        self.FAN_OFF.setStyleSheet("background-color: rgb(248, 0, 48);")
        self.FAN_OFF.setObjectName("FAN_OFF")
        self.FAN_ON = QtWidgets.QPushButton(self.centralWidget)
        self.FAN_ON.setGeometry(QtCore.QRect(590, 260, 51, 37))
        self.FAN_ON.setStyleSheet("background-color: rgb(222, 231, 220);")
        self.FAN_ON.setObjectName("FAN_ON")
        self.LAMP_OFF = QtWidgets.QPushButton(self.centralWidget)
        self.LAMP_OFF.setGeometry(QtCore.QRect(330, 260, 51, 37))
        self.LAMP_OFF.setStyleSheet("background-color:rgb(222, 231, 220);")
        self.LAMP_OFF.setObjectName("LAMP_OFF")
        self.HOME_BUTTON = QtWidgets.QPushButton(self.centralWidget)
        self.HOME_BUTTON.setGeometry(QtCore.QRect(430, 346, 91, 41))
        self.HOME_BUTTON.setStyleSheet("border:0px\n"
"")
        self.HOME_BUTTON.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/maintanence/home_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HOME_BUTTON.setIcon(icon)
        self.HOME_BUTTON.setIconSize(QtCore.QSize(45, 45))
        self.HOME_BUTTON.setObjectName("HOME_BUTTON")
        Maintenance.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Maintenance)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 34))
        self.menuBar.setObjectName("menuBar")
        Maintenance.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Maintenance)
        self.mainToolBar.setObjectName("mainToolBar")
        Maintenance.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Maintenance)
        self.statusBar.setObjectName("statusBar")
        Maintenance.setStatusBar(self.statusBar)

        self.retranslateUi(Maintenance)
        QtCore.QMetaObject.connectSlotsByName(Maintenance)

    def retranslateUi(self, Maintenance):
        _translate = QtCore.QCoreApplication.translate
        Maintenance.setWindowTitle(_translate("Maintenance", "Maintenance"))
        self.NODE1.setText(_translate("Maintenance", "   NODE 1"))
        self.NODE2.setText(_translate("Maintenance", "   NODE 2"))
        self.NODE3.setText(_translate("Maintenance", "   NODE 3"))
        self.NODE4.setText(_translate("Maintenance", "   NODE 4"))
        self.label.setText(_translate("Maintenance", "MAINTANENCE"))
        self.LAMP_ON.setText(_translate("Maintenance", "ON"))
        self.FAN_OFF.setText(_translate("Maintenance", "OFF"))
        self.FAN_ON.setText(_translate("Maintenance", "ON"))
        self.LAMP_OFF.setText(_translate("Maintenance", "OFF"))

        # Function calling 
        self.NODE1.clicked.connect(self.Node1)
        self.NODE2.clicked.connect(self.Node2)
        self.NODE3.clicked.connect(self.Node3)
        self.NODE3.clicked.connect(self.Node4)
        self.HOME_BUTTON.clicked.connect(self.Home)
        self.LAMP_OFF.clicked.connect(self.Lamp_off)
        self.LAMP_ON.clicked.connect(self.Lamp_on)
        self.FAN_ON.clicked.connect(self.Fan_on)
        self.FAN_OFF.clicked.connect(self.Fan_off)

#############################################################################################################
#Function defenitions starts here
# This fucntion 
#
#############################################################################################################    

    def Node1(self):
        print ("ello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Maintenance = QtWidgets.QMainWindow()
    ui = Ui_Maintenance()
    ui.setupUi(Maintenance)
    Maintenance.show()
    sys.exit(app.exec_())

