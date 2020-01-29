import socket
import sys
import threading
from chatwindow import *


def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('2.2.2.2', 1))
    return s.getsockname()[0]


class Server:

    def __init__(self, output):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0', 6001))
        self.sock.listen(1)
        self.output = output
        self.output.append("Server started...")
        cThread = threading.Thread(target=self.handler)
        cThread.daemon = True
        cThread.start()

    def handler(self):
        while True:
            c, a = self.sock.accept()
            data = c.recv(1024)
            self.output.append("Other: " + str(data, 'utf-8'))
            if not data:
                self.output.append(str(a[0]) + ":" +
                                   str(a[1]) + "disconnected")
                c.close()
                break


class Client:

    def __init__(self, output):
        self.output = output
        self.sock = None

    def connect(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address, 6001))
        self.output.append("Client connected to " + address)
        rThread = threading.Thread(target=self.rcvMsg)
        rThread.daemon = True
        rThread.start()

    def rcvMsg(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            else:
                self.output.append(str(data, 'utf-8'))

    def sendMsg(self, message):
        self.sock.sendall(bytes(message, 'utf-8'))

    def disconnect(self):
        self.sock.close()
        self.output.append("Client disconnected")


class Chat:

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButtonConnect.clicked.connect(self.connect)
        self.ui.pushButtonSend.clicked.connect(self.sendMessage)
        self.server = Server(self.ui.textBrowserReceivedMessages)
        self.client = Client(self.ui.textBrowserReceivedMessages)
        MainWindow.statusBar().showMessage("Your IP is: " + str(getIPAddress()))
        MainWindow.show()
        sys.exit(app.exec_())

    def connect(self):
        if self.ui.pushButtonConnect.text() == "Connect":
            address = self.ui.lineEditAddress.text()
            if address == "":
                address = "127.0.0.1"
            self.client.connect(address)
            self.ui.pushButtonConnect.setText("Disconnect")
        else:
            self.client.disconnect()
            self.ui.pushButtonConnect.setText("Connect")


    def sendMessage(self):
        message = self.ui.plainTextEditMessage.toPlainText()
        self.ui.textBrowserReceivedMessages.append("Me: " + message)
        self.ui.plainTextEditMessage.clear()
        if self.client and message:
            self.client.sendMsg(message)


if __name__ == "__main__":
    chat = Chat()
