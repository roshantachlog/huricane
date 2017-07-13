from PyQt5 import QtCore, QtGui, QtWidgets
from clock import Ui_Clock

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Clock()
    ui.showFullScreen()
    sys.exit(app.exec_())


