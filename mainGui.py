from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtWidgets import QAction, QToolBar, QStatusBar
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
        self.setWindowTitle("Test Qt app")
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('green'))
        widget = QWidget()
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


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)
window = MainWindow()
window.statusBar.showMessage("Your IP is: " + str(getIPAddress()))
window.resize(480, 600)
window.show()

app.exec_()
