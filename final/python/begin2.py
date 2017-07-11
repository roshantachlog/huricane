from PyQt5 import QtCore, QtGui, QtWidgets
from Maintenance import Ui_Maintenance

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Maintenance()
    ui.show()
    sys.exit(app.exec_())


