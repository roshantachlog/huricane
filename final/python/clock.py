
from PyQt5 import QtCore, QtGui, QtWidgets
#from Schedule import Schedule_window
class Ui_Clock(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        #MainWindow.setObjectName("MainWindow")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setEnabled(True)
        self.resize(800, 480)
        #self.setStyleSheet("background-color: rgb(250, 215, 220);\n"
#"border-color: rgb(234, 85, 85);")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 120, 261, 71))
        self.widget_2.setStyleSheet("background-color: rgb(183, 66, 66);")
        self.widget_2.setObjectName("widget_2")
        self.MINUTE_CENTER = QtWidgets.QLabel(self.widget_2)
        self.MINUTE_CENTER.setGeometry(QtCore.QRect(157, 0, 91, 71))
        self.MINUTE_CENTER.setStyleSheet("background-color: rgb(183, 66, 66);\n"
"color: rgb(255, 255, 255);\n"
"font: 48pt \"Sans Serif\";")
        self.MINUTE_CENTER.setObjectName("MINUTE_CENTER")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(120, 0, 16, 80))
        self.widget_3.setStyleSheet("background-color: rgb(255,215,220);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(-3, 0, 21, 61))
        self.label_3.setStyleSheet("color: rgb(183, 66, 66);\n"
"font: 48pt \"Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.HOUR_CENTER = QtWidgets.QLabel(self.widget_2)
        self.HOUR_CENTER.setGeometry(QtCore.QRect(20, 0, 91, 71))
        self.HOUR_CENTER.setStyleSheet("background-color: rgb(183, 66, 66);\n"
"color: rgb(255, 255, 255);\n"
"font: 48pt \"Sans Serif\";")
        self.HOUR_CENTER.setObjectName("HOUR_CENTER")
        self.HOUR_UP = QtWidgets.QPushButton(self.centralWidget)
        self.HOUR_UP.setGeometry(QtCore.QRect(0, 83, 121, 37))
        self.HOUR_UP.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.HOUR_UP.setObjectName("HOUR_UP")
        self.MINUTE_UP = QtWidgets.QPushButton(self.centralWidget)
        self.MINUTE_UP.setGeometry(QtCore.QRect(135, 83, 123, 37))
        self.MINUTE_UP.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.MINUTE_UP.setObjectName("MINUTE_UP")
        self.HOUR_DOWN = QtWidgets.QPushButton(self.centralWidget)
        self.HOUR_DOWN.setEnabled(True)
        self.HOUR_DOWN.setGeometry(QtCore.QRect(0, 190, 121, 37))
        self.HOUR_DOWN.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.HOUR_DOWN.setObjectName("HOUR_DOWN")
        self.MINUTE_DOWN = QtWidgets.QPushButton(self.centralWidget)
        self.MINUTE_DOWN.setGeometry(QtCore.QRect(135, 190, 123, 37))
        self.MINUTE_DOWN.setStyleSheet("\n"
"color: rgb(149, 50, 41);\n"
"background-color: rgb(237, 158, 158);\n"
"font: 18pt \"Sans Serif\";")
        self.MINUTE_DOWN.setObjectName("MINUTE_DOWN")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 241, 41))
        self.label_4.setStyleSheet("color: rgb(240,110,110);\n"
"border:0px;\n"
"font: 24pt \"Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.CANCEL = QtWidgets.QPushButton(self.centralWidget)
        self.CANCEL.setGeometry(QtCore.QRect(0, 260, 128, 51))
        self.CANCEL.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 170);\n"
"color: rgb(183, 66, 66);font: 18pt \"Sans Serif\";")
        self.CANCEL.setObjectName("CANCEL")
        self.OK = QtWidgets.QPushButton(self.centralWidget)
        self.OK.setEnabled(True)
        self.OK.setGeometry(QtCore.QRect(130, 260, 128, 51))
        self.OK.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 18pt \"Sans Serif\";\n"
"background-color: rgb(255, 170, 170);\n"
"color: rgb(183, 66, 66);")
        self.OK.setObjectName("OK")
        self.setCentralWidget(self.centralWidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
####################################################################
# Global varaiable declaration
#
####################################################################

    global HOUR_CNTR
    HOUR_CNTR = 0
    global MINUTE_CNTR
    MINUTE_CNTR =0 

    def retranslateUi(self):
        HOUR="00"
        MINUTE="00"
        
        _translate = QtCore.QCoreApplication.translate
        self.MINUTE_CENTER.setText(_translate("MainWindow", MINUTE))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.HOUR_CENTER.setText(_translate("MainWindow", HOUR))
        self.HOUR_UP.setText(_translate("MainWindow", "00"))
        self.MINUTE_UP.setText(_translate("MainWindow", "01"))
        self.HOUR_DOWN.setText(_translate("MainWindow", "23"))
        self.MINUTE_DOWN.setText(_translate("MainWindow", "59"))
        self.label_4.setText(_translate("MainWindow", "Starting Time"))
        self.CANCEL.setText(_translate("MainWindow", "CANCEL"))
        self.OK.setText(_translate("MainWindow", "OK"))

###############################################################################
# Function call
###############################################################################

        self.HOUR_UP.clicked.connect(self.Hour_Up)
        self.MINUTE_UP.clicked.connect(self.Minute_Up)
        self.MINUTE_DOWN.clicked.connect(self.Minute_Down)
        self.OK.clicked.connect(self.Ok)
        self.CANCEL.clicked.connect(self.Cancel)
        self.HOUR_DOWN.clicked.connect(self.Hour_Down)

##############################################################################
# Function defenition
##############################################################################


# hour up button response

    def Hour_Up(self ):
        print("hour up")
        global HOUR_CNTR
        HOUR_CNTR = self.HOUR_INC(HOUR_CNTR)
        HOUR_STR=str(HOUR_CNTR)
        HOUR_STR=HOUR_STR.zfill(2)
        self.HOUR_CENTER.setText( HOUR_STR)
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
        self.HOUR_CENTER.setText(HOUR_STR)
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
        self.MINUTE_CENTER.setText(MINUTE_STR)
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
        self.MINUTE_CENTER.setText(MINUTE_STR)

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

