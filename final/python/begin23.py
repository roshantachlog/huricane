from PyQt5 import QtCore, QtGui, QtWidgets
from third import Ui_Clock

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Clock()
    ui.show()
    sys.exit(app.exec_())


