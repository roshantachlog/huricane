from PyQt5 import QtCore, QtGui, QtWidgets
from Home import Ui_Home

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Home()
    ui.show()
    sys.exit(app.exec_())


