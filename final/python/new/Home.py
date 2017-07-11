# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul  7 11:58:54 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.setEnabled(True)
        Home.resize(800, 480)
        Home.setSizeIncrement(QtCore.QSize(1, 1))
        Home.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        Home.setIconSize(QtCore.QSize(65, 65))
        self.centralWidget = QtWidgets.QWidget(Home)#MainWindow
        self.centralWidget.setObjectName("centralWidget")
        self.MAINTENANCE = QtWidgets.QPushButton(self.centralWidget)
        self.MAINTENANCE.setGeometry(QtCore.QRect(80, 290, 71, 71))
        self.MAINTENANCE.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.MAINTENANCE.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(170, 85, 255);\n"
"border-top-color: rgb(85, 85, 127);\n"
"selection-color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: solid;")
        self.MAINTENANCE.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/Home/maintanence.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MAINTENANCE.setIcon(icon)
        self.MAINTENANCE.setIconSize(QtCore.QSize(65, 65))
        self.MAINTENANCE.setObjectName("MAINTENANCE")
        self.SCHEDULE = QtWidgets.QPushButton(self.centralWidget)
        self.SCHEDULE.setGeometry(QtCore.QRect(220, 290, 71, 71))
        self.SCHEDULE.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.SCHEDULE.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/Home/schedule.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SCHEDULE.setIcon(icon1)
        self.SCHEDULE.setIconSize(QtCore.QSize(70, 70))
        self.SCHEDULE.setObjectName("SCHEDULE")
        self.STATUS = QtWidgets.QPushButton(self.centralWidget)
        self.STATUS.setGeometry(QtCore.QRect(360, 290, 71, 71))
        self.STATUS.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.STATUS.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/Home/status.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.STATUS.setIcon(icon2)
        self.STATUS.setIconSize(QtCore.QSize(60, 60))
        self.STATUS.setObjectName("STATUS")
        self.LAMP_LIFE = QtWidgets.QPushButton(self.centralWidget)
        self.LAMP_LIFE.setGeometry(QtCore.QRect(500, 290, 71, 71))
        self.LAMP_LIFE.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.LAMP_LIFE.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/Home/bulb_life.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LAMP_LIFE.setIcon(icon3)
        self.LAMP_LIFE.setIconSize(QtCore.QSize(65, 65))
        self.LAMP_LIFE.setObjectName("LAMP_LIFE")
        self.ABOUT = QtWidgets.QPushButton(self.centralWidget)
        self.ABOUT.setGeometry(QtCore.QRect(640, 290, 91, 71))
        self.ABOUT.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);")
        self.ABOUT.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/Home/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ABOUT.setIcon(icon4)
        self.ABOUT.setIconSize(QtCore.QSize(56, 56))
        self.ABOUT.setObjectName("ABOUT")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(350, 210, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Sans Serif\";\n"
"color: rgb(68, 72, 78);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(80, 360, 151, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(220, 360, 111, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(370, 360, 91, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(510, 360, 131, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(670, 360, 71, 29))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 260, 161, 5))
        self.frame_2.setStyleSheet("background-color: rgb(68, 72, 78);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, -50, 161, 5))
        self.frame_3.setStyleSheet("background-color: rgb(68, 72, 78);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralWidget)
        self.frame_4.setGeometry(QtCore.QRect(320, 210, 161, 5))
        self.frame_4.setStyleSheet("background-color: rgb(68, 72, 78);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, -50, 161, 5))
        self.frame_5.setStyleSheet("background-color: rgb(68, 72, 78);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(240, 30, 291, 121))
        self.label_7.setStyleSheet("image:url(\'../icons/Home/hurricane-logo-retina.png\');")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.shutdown = QtWidgets.QPushButton(self.centralWidget)
        self.shutdown.setGeometry(QtCore.QRect(720, 20, 51, 51))
        self.shutdown.setStyleSheet("border:0px;")
        self.shutdown.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/Home/shutdown_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shutdown.setIcon(icon5)
        self.shutdown.setIconSize(QtCore.QSize(39, 46))
        self.shutdown.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(550, 280, 31, 29))
        self.label_8.setStyleSheet("image:url(\'/home/tachlog/Desktop/hurricanenew/final/icons/Home/warningred.png\');\n"
"border:0px")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        Home.setCentralWidget(self.centralWidget)
       
        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self,Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.label.setText(_translate("Home", "<html><head/><body><p><span style=\" font-size:18pt;\">M E N U</span></p></body></html>"))
        self.label_2.setText(_translate("Home", "MAINTENANCE"))
        self.label_3.setText(_translate("Home", "SCHEDULE"))
        self.label_4.setText(_translate("Home", "STATUS"))
        self.label_5.setText(_translate("Home", "LAMP LIFE"))
        self.label_6.setText(_translate("Home", "ABOUT"))
        self.shutdown.clicked.connect(self.shutdown)



    def shutdown(self):
        ##############################
        #add confirmation message box here
        ##############################
        import os
        os.system('systemctl poweroff') 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())

