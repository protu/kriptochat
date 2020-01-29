import sys
from mover import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Moving:

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.ui.pbButon1.clicked.connect(self.copyText)
        sys.exit(app.exec_())

    def copyText(self):
        msgText = self.ui.leText.text()
        self.ui.tbTextOut.append(msgText)


if __name__ == "__main__":
    Moving()
