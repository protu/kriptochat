import socket
import sys
import threading
from chatwindow import *


def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('2.2.2.2', 1))
    return s.getsockname()[0]


class Server:
    conn = None
    chost = None

    def __init__(self, output, chat):
        self.chat = chat
        self.output = output
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', 6001))
        self.sock.listen(1)
        self.startServer()

    def startServer(self):
        self.output.append("Server started...")
        self.cThread = threading.Thread(target=self.handler)
        self.cThread.daemon = True
        self.cThread.start()

    def handler(self):
        while True:
            self.conn, self.chost = self.sock.accept()
            if self.conn is not None:
                self.chat.clientAddress(self.chost[0])
                self.chat.connect()
                self.output.append("Client connected from " + self.chost[0])
                break
        while True:
            data = self.conn.recv(1024)
            if data == b'\x11Disconnect' or not data:
                self.disconnect()
                break
            else:
                self.output.append("Other: " + str(data, 'utf-8'))

    def sendMsg(self, message):
        self.conn.sendall(bytes(message, 'utf-8'))

    def disconnect(self):
        self.output.append("Disconnecting on client request")
        self.conn.close()
        self.startServer()


class Client:

    def __init__(self, output):
        self.output = output
        self.sock = None

    def connect(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.output.append("Client connected to " + address)
        self.sock.connect((address, 6001))
        rThread = threading.Thread(target=self.rcvMsg)
        rThread.daemon = True
        rThread.start()

    def rcvMsg(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            else:
                self.output.append("Other: " + str(data, 'utf-8'))

    def sendMsg(self, message):
        self.sock.sendall(bytes(message, 'utf-8'))

    def disconnect(self):
        self.sock.sendall(b'\x11Disconnect')
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        self.output.append("Client disconnected")


class Chat:
    clientMode = False

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButtonConnect.clicked.connect(self.connectToggle)
        self.ui.pushButtonSend.clicked.connect(self.sendMessage)
        self.ui.pushButtonSend.setEnabled(False)
        self.server = Server(self.ui.textBrowserReceivedMessages, self)
        self.client = Client(self.ui.textBrowserReceivedMessages)
        MainWindow.statusBar().showMessage("Your IP is: " + str(getIPAddress()))
        MainWindow.show()
        sys.exit(app.exec_())

    def clientAddress(self, address):
        self.ui.lineEditAddress.setText(address)
        self.ui.pushButtonConnect.setText("Disconnect")

    def connectToggle(self):
        if self.ui.pushButtonConnect.text().find("Connect") != -1:
            self.clientMode = True
            self.connect()
        else:
            self.disconnect()

    def connect(self):
        address = self.ui.lineEditAddress.text()
        if address == "":
            address = "127.0.0.1"
        if self.clientMode:
            self.client.connect(address)
        self.ui.pushButtonConnect.setText("Disconnect")
        self.ui.pushButtonSend.setEnabled(True)

    def disconnect(self):
        if self.clientMode:
            self.client.disconnect()
            self.ui.pushButtonConnect.setText("Connect")
            self.ui.pushButtonSend.setEnabled(False)
            self.clientMode = False
        else:
            self.server.disconnect()
            self.ui.pushButtonConnect.setText("Connect")
            self.ui.pushButtonSend.setEnabled(False)

    def sendMessage(self):
        message = self.ui.plainTextEditMessage.toPlainText()
        self.ui.textBrowserReceivedMessages.append("Me: " + message)
        self.ui.plainTextEditMessage.clear()
        if self.clientMode and message:
            self.client.sendMsg(message)
        else:
            self.server.sendMsg(message)


if __name__ == "__main__":
    chat = Chat()
