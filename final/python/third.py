from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Clock(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)
        self.resize(720, 480)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(31, 30, 651, 331))
        self.frame.setStyleSheet("background-color: rgb(238, 234, 234);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(13, 10, 271, 231))
        self.frame_2.setStyleSheet("background-color: rgb(250, 215, 220);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(369, 10, 271, 231))
        self.frame_3.setStyleSheet("background-color: rgb(250, 215, 220);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label7 = QtWidgets.QLabel(self.frame)
        self.label7.setGeometry(QtCore.QRect(136, 110, 16, 71))
        self.label7.setStyleSheet("background-color: rgb(250, 215, 220);\n"
"color: rgb(183, 66, 66);\n"
"font: 48pt \"Sans Serif\";\n"
"border:0px")
        self.label7.setObjectName("label7")
        self.label8 = QtWidgets.QLabel(self.frame)
        self.label8.setGeometry(QtCore.QRect(491, 110, 16, 71))
        self.label8.setStyleSheet("background-color: rgb(250, 215, 220);\n"
"color: rgb(183, 66, 66);\n"
"font: 48pt \"Sans Serif\";\n"
"border:0px")
        self.label8.setObjectName("label8")
        self.HOUR_DOWN_2 = QtWidgets.QPushButton(self.frame)
        self.HOUR_DOWN_2.setEnabled(True)
        self.HOUR_DOWN_2.setGeometry(QtCore.QRect(375, 187, 121, 37))
        self.HOUR_DOWN_2.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.HOUR_DOWN_2.setObjectName("HOUR_DOWN_2")
        self.OK = QtWidgets.QPushButton(self.frame)
        self.OK.setEnabled(True)
        self.OK.setGeometry(QtCore.QRect(360, 260, 221, 51))
        self.OK.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 18pt \"Sans Serif\";\n"
"background-color: rgb(255, 170, 170);\n"
"color: rgb(106, 71, 71);")
        self.OK.setObjectName("OK")
        self.MINUTE_DOWN = QtWidgets.QPushButton(self.frame)
        self.MINUTE_DOWN.setGeometry(QtCore.QRect(154, 190, 123, 37))
        self.MINUTE_DOWN.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.MINUTE_DOWN.setObjectName("MINUTE_DOWN")
        self.MINUTE_UP_2 = QtWidgets.QPushButton(self.frame)
        self.MINUTE_UP_2.setGeometry(QtCore.QRect(510, 80, 123, 37))
        self.MINUTE_UP_2.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.MINUTE_UP_2.setObjectName("MINUTE_UP_2")
        self.HOUR_UP = QtWidgets.QPushButton(self.frame)
        self.HOUR_UP.setGeometry(QtCore.QRect(19, 83, 121, 37))
        self.HOUR_UP.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.HOUR_UP.setObjectName("HOUR_UP")
        self.MINUTE_CENTER_2 = QtWidgets.QLabel(self.frame)
        self.MINUTE_CENTER_2.setGeometry(QtCore.QRect(510, 117, 122, 71))
        self.MINUTE_CENTER_2.setStyleSheet("background-color: rgb(183, 66, 66);\n"
"color: rgb(255, 255, 255);\n"
"font: 48pt \"Sans Serif\";")
        self.MINUTE_CENTER_2.setObjectName("MINUTE_CENTER_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(445, 20, 191, 41))
        self.label_5.setStyleSheet("color: rgb(184, 11, 5);\n"
"background-color: rgb(250, 215, 220);\n"
"border:0px;\n"
"font: 24pt \"Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.CANCEL = QtWidgets.QPushButton(self.frame)
        self.CANCEL.setGeometry(QtCore.QRect(85, 260, 211, 51))
        self.CANCEL.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 170);\n"
"color: rgb(106, 71, 71);font: 18pt \"Sans Serif\";")
        self.CANCEL.setObjectName("CANCEL")
        self.MINUTE_DOWN_2 = QtWidgets.QPushButton(self.frame)
        self.MINUTE_DOWN_2.setGeometry(QtCore.QRect(510, 187, 123, 37))
        self.MINUTE_DOWN_2.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.MINUTE_DOWN_2.setObjectName("MINUTE_DOWN_2")
        self.HOUR_UP_2 = QtWidgets.QPushButton(self.frame)
        self.HOUR_UP_2.setGeometry(QtCore.QRect(375, 80, 121, 37))
        self.HOUR_UP_2.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.HOUR_UP_2.setObjectName("HOUR_UP_2")
        self.MINUTE_UP = QtWidgets.QPushButton(self.frame)
        self.MINUTE_UP.setGeometry(QtCore.QRect(154, 83, 123, 37))
        self.MINUTE_UP.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.MINUTE_UP.setObjectName("MINUTE_UP")
        self.HOUR_CENTER_2 = QtWidgets.QLabel(self.frame)
        self.HOUR_CENTER_2.setGeometry(QtCore.QRect(376, 117, 119, 71))
        self.HOUR_CENTER_2.setStyleSheet("background-color: rgb(183, 66, 66);\n"
"color: rgb(255, 255, 255);\n"
"font: 48pt \"Sans Serif\";")
        self.HOUR_CENTER_2.setObjectName("HOUR_CENTER_2")
        self.HOUR_DOWN = QtWidgets.QPushButton(self.frame)
        self.HOUR_DOWN.setEnabled(True)
        self.HOUR_DOWN.setGeometry(QtCore.QRect(19, 190, 121, 37))
        self.HOUR_DOWN.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.HOUR_DOWN.setObjectName("HOUR_DOWN")
        self.MINUTE_CENTER = QtWidgets.QLabel(self.frame)
        self.MINUTE_CENTER.setGeometry(QtCore.QRect(154, 120, 122, 71))
        self.MINUTE_CENTER.setStyleSheet("background-color: rgb(183, 66, 66);\n"
"color: rgb(255, 255, 255);\n"
"font: 48pt \"Sans Serif\";")
        self.MINUTE_CENTER.setObjectName("MINUTE_CENTER")
        self.HOUR_CENTER = QtWidgets.QLabel(self.frame)
        self.HOUR_CENTER.setGeometry(QtCore.QRect(20, 120, 119, 71))
        self.HOUR_CENTER.setStyleSheet("background-color: rgb(183, 66, 66);\n"
"color: rgb(255, 255, 255);\n"
"font: 48pt \"Sans Serif\";")
        self.HOUR_CENTER.setObjectName("HOUR_CENTER")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(39, 20, 231, 41))
        self.label_4.setStyleSheet("color: rgb(184, 11, 5);\n"
"border:0px;\n"
"font: 24pt \"Sans Serif\";\n"
"background-color: rgb(250, 215, 220);")
        self.label_4.setObjectName("label_4")
        self.setCentralWidget(self.centralWidget)
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    global HOUR_CNTR
    HOUR_CNTR = 0
    global MINUTE_CNTR
    MINUTE_CNTR = 0 
    global HOUR_CNTR_2
    HOUR_CNTR_2 = 0
    global MINUTE_CNTR_2
    MINUTE_CNTR_2=0

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label7.setText(_translate("MainWindow", ":"))
        self.label8.setText(_translate("MainWindow", ":"))
        self.HOUR_DOWN_2.setText(_translate("MainWindow", "99"))
        self.OK.setText(_translate("MainWindow", "OK"))
        self.MINUTE_DOWN.setText(_translate("MainWindow", "59"))
        self.MINUTE_UP_2.setText(_translate("MainWindow", "01"))
        self.HOUR_UP.setText(_translate("MainWindow", "01"))
        self.MINUTE_CENTER_2.setText(_translate("MainWindow", " 00"))
        self.label_5.setText(_translate("MainWindow", "Duration "))
        self.CANCEL.setText(_translate("MainWindow", "CANCEL"))
        self.MINUTE_DOWN_2.setText(_translate("MainWindow", "59"))
        self.HOUR_UP_2.setText(_translate("MainWindow", "01"))
        self.MINUTE_UP.setText(_translate("MainWindow", "01"))
        self.HOUR_CENTER_2.setText(_translate("MainWindow", " 00"))
        self.HOUR_DOWN.setText(_translate("MainWindow", "23"))
        self.MINUTE_CENTER.setText(_translate("MainWindow", " 00"))
        self.HOUR_CENTER.setText(_translate("MainWindow", " 00"))
        self.label_4.setText(_translate("MainWindow", "Starting Time"))

#function call of duration

        self.HOUR_UP.clicked.connect(self.Hour_Up)
        self.MINUTE_UP.clicked.connect(self.Minute_Up)
        self.MINUTE_DOWN.clicked.connect(self.Minute_Down)
        self.OK.clicked.connect(self.Ok)
        self.CANCEL.clicked.connect(self.Cancel)
        self.HOUR_DOWN.clicked.connect(self.Hour_Down)

#function call of duration
        self.HOUR_DOWN_2.clicked.connect(self.Hour_Down_2)
        self.HOUR_UP_2.clicked.connect(self.Hour_Up_2)
        self.MINUTE_UP_2.clicked.connect(self.Minute_Up_2)
        self.MINUTE_DOWN_2.clicked.connect(self.Minute_Down_2)

    def Hour_Up(self ):
        print("hour up")
        global HOUR_CNTR
        HOUR_CNTR = self.HOUR_INC(HOUR_CNTR)
        HOUR_STR=str(HOUR_CNTR)
        HOUR_STR=HOUR_STR.zfill(2)
        self.HOUR_CENTER.setText(" "+ HOUR_STR)
        print(HOUR_STR)

        self.HOUR_UP.setText(str(self.HOUR_INC(HOUR_CNTR)).zfill(2))
        
        self.HOUR_DOWN.setText(str(self.HOUR_DEC(HOUR_CNTR)).zfill(2))


# hour increment
        
    def HOUR_INC(self,HOUR):
        if HOUR<23:
            HOUR = HOUR+1
        else :
            HOUR = 0
        return HOUR

# hour down button response

    def Hour_Down(self):
        print("hour down")
        global HOUR_CNTR
        HOUR_CNTR = self.HOUR_DEC(HOUR_CNTR)
        HOUR_STR=str(HOUR_CNTR)
        HOUR_STR=HOUR_STR.zfill(2)
        self.HOUR_CENTER.setText(" "+HOUR_STR)
        print(HOUR_STR)

        self.HOUR_UP.setText(str(self.HOUR_INC(HOUR_CNTR)).zfill(2))

        self.HOUR_DOWN.setText(str(self.HOUR_DEC(HOUR_CNTR)).zfill(2))

#hour decrement

    def HOUR_DEC(self,HOUR):
        if HOUR>0:
            HOUR = HOUR-1
        else:
            HOUR = 23
        return HOUR
        
# button minute up funtion defenition

    def Minute_Up(self):
        print("minut up")
        global MINUTE_CNTR
        MINUTE_CNTR = self.MINUTE_INC(MINUTE_CNTR)  
        MINUTE_STR=str(MINUTE_CNTR)
        MINUTE_STR=MINUTE_STR.zfill(2)
        self.MINUTE_CENTER.setText(" "+MINUTE_STR)
        print (MINUTE_STR)

        MINUTE_UP = str(self.MINUTE_INC(MINUTE_CNTR))
        MINUTE_UP = MINUTE_UP.zfill(2)
        self.MINUTE_UP.setText(MINUTE_UP)

        MINUTE_DOWN = str(self.MINUTE_DEC(MINUTE_CNTR))
        MINUTE_DOWN = MINUTE_DOWN.zfill(2)
        self.MINUTE_DOWN.setText(MINUTE_DOWN)
# minute increment funtion defenition

    def MINUTE_INC(self,MINUTE):
        if MINUTE<59:
            MINUTE = MINUTE+1
        else :
            MINUTE = 0
        return MINUTE

# minute down funtion defenition

    def Minute_Down(self):
        print("minute down")
        global MINUTE_CNTR
        MINUTE_CNTR = self.MINUTE_DEC(MINUTE_CNTR)
        MINUTE_STR = str(MINUTE_CNTR)
        MINUTE_STR=MINUTE_STR.zfill(2)
        self.MINUTE_CENTER.setText(" "+MINUTE_STR)

        MINUTE_UP = str(self.MINUTE_INC(MINUTE_CNTR))
        MINUTE_UP = MINUTE_UP.zfill(2)
        self.MINUTE_UP.setText(MINUTE_UP)

        MINUTE_DOWN = str(self.MINUTE_DEC(MINUTE_CNTR))
        MINUTE_DOWN = MINUTE_DOWN.zfill(2)
        self.MINUTE_DOWN.setText(MINUTE_DOWN)
        
        
        print (MINUTE_STR)  
        
# minute decrement funtion defenition

    def MINUTE_DEC(self,MINUTE):
        if MINUTE>0:
            MINUTE = MINUTE-1
        else:
            MINUTE = 59
        return MINUTE


#################################################
#
#
###################################################
    def Hour_Up_2(self ):
        print("hour up")
        global HOUR_CNTR_2
        HOUR_CNTR_2 = self.HOUR_INC_2(HOUR_CNTR_2)
        HOUR_STR_2=str(HOUR_CNTR_2)
        HOUR_STR_2=HOUR_STR_2.zfill(2)
        self.HOUR_CENTER_2.setText(" "+HOUR_STR_2)
        print(HOUR_STR_2)

        self.HOUR_UP_2.setText(str(self.HOUR_INC_2(HOUR_CNTR_2)).zfill(2))
        
        self.HOUR_DOWN_2.setText(str(self.HOUR_DEC_2(HOUR_CNTR_2)).zfill(2))


# hour increment
        
    def HOUR_INC_2(self,HOUR):
        if HOUR<99:
            HOUR = HOUR+1
        else :
            HOUR = 0
        return HOUR

# hour down button response

    def Hour_Down_2(self):
        print("hour down")
        global HOUR_CNTR_2
        HOUR_CNTR_2 = self.HOUR_DEC_2(HOUR_CNTR_2)
        HOUR_STR_2=str(HOUR_CNTR_2)
        HOUR_STR_2=HOUR_STR_2.zfill(2)
        self.HOUR_CENTER_2.setText(" "+HOUR_STR_2)
        print(HOUR_STR_2)

        self.HOUR_UP_2.setText(str(self.HOUR_INC_2(HOUR_CNTR_2)).zfill(2))

        self.HOUR_DOWN_2.setText(str(self.HOUR_DEC_2(HOUR_CNTR_2)).zfill(2))

#hour decrement

    def HOUR_DEC_2(self,HOUR):
        if HOUR>0:
            HOUR = HOUR-1
        else:
            HOUR = 99
        return HOUR
        
# button minute up funtion defenition

    def Minute_Up_2(self):
        print("minut up")
        global MINUTE_CNTR_2
        MINUTE_CNTR_2 = self.MINUTE_INC_2(MINUTE_CNTR_2)  
        MINUTE_STR_2=str(MINUTE_CNTR_2)
        MINUTE_STR_2=MINUTE_STR_2.zfill(2)
        self.MINUTE_CENTER_2.setText(" "+MINUTE_STR_2)
        print (MINUTE_STR_2)

        MINUTE_UP_2 = str(self.MINUTE_INC_2(MINUTE_CNTR_2))
        MINUTE_UP_2 = MINUTE_UP_2.zfill(2)
        self.MINUTE_UP_2.setText(MINUTE_UP_2)

        MINUTE_DOWN_2 = str(self.MINUTE_DEC_2(MINUTE_CNTR_2))
        MINUTE_DOWN_2 = MINUTE_DOWN_2.zfill(2)
        self.MINUTE_DOWN_2.setText(MINUTE_DOWN_2)
# minute increment funtion defenition

    def MINUTE_INC_2(self,MINUTE):
        if MINUTE<59:
            MINUTE = MINUTE+1
        else :
            MINUTE = 0
        return MINUTE

# minute down funtion defenition

    def Minute_Down_2(self):
        print("minute down")
        global MINUTE_CNTR_2
        MINUTE_CNTR_2 = self.MINUTE_DEC_2(MINUTE_CNTR_2)
        MINUTE_STR_2 = str(MINUTE_CNTR_2)
        MINUTE_STR_2=MINUTE_STR_2.zfill(2)
        self.MINUTE_CENTER_2.setText(" "+MINUTE_STR_2)

        MINUTE_UP_2 = str(self.MINUTE_INC_2(MINUTE_CNTR_2))
        MINUTE_UP_2 = MINUTE_UP_2.zfill(2)
        self.MINUTE_UP_2.setText(MINUTE_UP_2)

        MINUTE_DOWN_2 = str(self.MINUTE_DEC_2(MINUTE_CNTR_2))
        MINUTE_DOWN_2 = MINUTE_DOWN_2.zfill(2)
        self.MINUTE_DOWN_2.setText(MINUTE_DOWN_2)
        
        
        print (MINUTE_STR_2)  
        
# minute decrement funtion defenition

    def MINUTE_DEC_2(self,MINUTE):
        if MINUTE>0:
            MINUTE = MINUTE-1
        else:
            MINUTE = 59
        return MINUTE


    def Ok(self):
        print("OK")
        global HOUR_CNTR
        global MINUTE_CNTR
        #back=Schedule_window()
        #back.Add_new_schedule.START_TM['HOUR']=HOUR_CNTR
        #back.Add_new_schedule.START_TM['MINUTE']=MINUTE_CNTR
        self.close()

    def Cancel(self):
        print("Cancel")
        self.close()            




