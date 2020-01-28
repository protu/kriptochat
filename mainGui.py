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

class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 6896
        BUFFER_SIZE = 1024
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        tcpServer.listen(1)
        while True:
            global conn
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, window)
            newthread.start()
            threads.append(newthread)
        for t in threads:
            t.join()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.statusBar().showMessage("Your IP is: " + str(getIPAddress()))
    MainWindow.show()
    sys.exit(app.exec_())
