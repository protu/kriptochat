from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QAction, QToolBar, QStatusBar, QTextBrowser, QTextEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor
import sys
import socket


def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('2.2.2.2', 1))
    return s.getsockname()[0]


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.title = "Probably secure chate"
        self.width = 480
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QTextBrowser(self))
        inputForm = InputForm()
        layout.addLayout(inputForm)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("User", self)
        button_action.triggered.connect(self.onToolBarButton1Click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def onToolBarButton1Click(self, s):
        print("click", s)


class InputForm(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__()

        textedit = QTextEdit()
        sendButton = QPushButton()
        self.addWidget(textedit)
        self.addWidget(sendButton)


app = QApplication(sys.argv)
window = MainWindow()
window.statusBar.showMessage("Your IP is: " + str(getIPAddress()))
window.show()

app.exec_()
