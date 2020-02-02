import socket
import sys
import threading
import time
import criptoLib
from chatwindow import *
from logindialog import *


def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('2.2.2.2', 1))
    return s.getsockname()[0]


class Server:
    conn = None
    chost = None
    symKey = None

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
                self.output.append("Client connected from " + self.chost[0])
                self.chat.ui.pushButtonSend.setEnabled(True)
                self.chat.ui.pushButtonConnect.setText("Disconnect")
                self.chat.ui.lineEditAddress.setText(self.chost[0])
                break
        while True:
            if self.conn is None:
                break
            try:
                data = self.conn.recv(1024)
                if data == b'\x11Disconnect' or not data:
                    self.disconnect()
                elif data.find(b"\x11Hello") == 0:
                    self.helloClient(data)
                else:
                    message = criptoLib.dec_msg(data, self.symKey)
                    self.output.append("Other: " + message)
            except Exception as e:
                print(e)
                pass

    def helloClient(self, clientHello):
        keyStart = clientHello.find(b"-----B")
        user = clientHello[6:keyStart]
        pubKey = clientHello[keyStart:]
        self.symKey = criptoLib.create_sym_key()
        iv = criptoLib.get_iv()
        encSymKey = criptoLib.encrypt_key(self.symKey, pk=pubKey)
        self.conn.sendall(b"\x11Hello" + encSymKey)

    def sendMsg(self, message):
        encMsg = criptoLib.enc_msg(message, self.symKey, criptoLib.get_iv())
        self.conn.sendall(encMsg)

    def disconnect(self):
        self.output.append("Server disconnected")
        self.conn.close()
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        self.chat.restartServer()


class Client:

    symKey = None

    def __init__(self, output):
        self.output = output
        self.sock = None

    def connectServer(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.output.append("Client connected to " + address)
        self.sock.connect((address, 6001))
        rThread = threading.Thread(target=self.rcvMsg)
        rThread.daemon = True
        rThread.start()
        self.helloServer()

    def helloServer(self):
        """Send authorization and public key to server"""
        hello_msg = b"\x11Hello" + b"user"
        hello_msg += self.getPublicKey()
        self.sock.sendall(hello_msg)

    def rcvMsg(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            elif data.find(b'\x11Hello') == 0:
                self.getSynKey(data)
            else:
                message = criptoLib.dec_msg(data, self.symKey)
                self.output.append("Other: " + message)

    def getSynKey(self, data):
        secKeyFile = open("seckey.pem", 'rb')
        synKey = criptoLib.decrypt_key(data[6:], sk=secKeyFile.read())
        self.symKey = synKey

    def sendMsg(self, message):
        encMsg = criptoLib.enc_msg(message, self.symKey, criptoLib.get_iv())
        self.sock.sendall(encMsg)

    def disconnect(self):
        self.sock.sendall(b'\x11Disconnect')
        # self.sock.shutdown(socket.SHUT_RDWR)
        # self.sock.close()
        self.output.append("Client disconnected")

    def getPublicKey(self):
        try:
            pubKeyFile = open("pubkey.pem", "rb")
            pubKeybytes = pubKeyFile.read()
            return pubKeybytes
        except Exception as e:
            print(e)


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
        self.ui.actionLogin.triggered.connect(self.login)
        self.server = Server(self.ui.textBrowserReceivedMessages, self)
        self.client = Client(self.ui.textBrowserReceivedMessages)
        MainWindow.statusBar().showMessage("Your IP is: " + str(getIPAddress()))
        MainWindow.show()
        sys.exit(app.exec_())

    def login(self):
        dialog = QtWidgets.QDialog()
        dui = Ui_Dialog()
        dui.setupUi(dialog)
        dialog.exec()

    def restartServer(self):
        self.server = Server(self.ui.textBrowserReceivedMessages, self)

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
            self.client.connectServer(address)
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
