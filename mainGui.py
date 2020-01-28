import socket
import sys
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QStatusBar, QTextBrowser, QTextEdit,
                             QToolBar, QVBoxLayout, QWidget)
from chatwindow import *


def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('2.2.2.2', 1))
    return s.getsockname()[0]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.statusBar().showMessage("Your IP is: " + str(getIPAddress()))
    MainWindow.show()
    sys.exit(app.exec_())
