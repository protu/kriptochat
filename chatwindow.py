# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\chatwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButtonSend.setMaximumSize(QtCore.QSize(80, 50))
        self.pushButtonSend.setBaseSize(QtCore.QSize(50, 50))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.gridLayout.addWidget(self.pushButtonSend, 2, 2, 1, 1)
        self.lineEditAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.gridLayout.addWidget(self.lineEditAddress, 0, 1, 1, 1)
        self.labelPeerHost = QtWidgets.QLabel(self.centralwidget)
        self.labelPeerHost.setObjectName("labelPeerHost")
        self.gridLayout.addWidget(self.labelPeerHost, 0, 0, 1, 1)
        self.pushButtonConnect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.gridLayout.addWidget(self.pushButtonConnect, 0, 2, 1, 1)
        self.textBrowserReceivedMessages = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserReceivedMessages.setMinimumSize(QtCore.QSize(300, 400))
        self.textBrowserReceivedMessages.setBaseSize(QtCore.QSize(400, 0))
        self.textBrowserReceivedMessages.setObjectName("textBrowserReceivedMessages")
        self.gridLayout.addWidget(self.textBrowserReceivedMessages, 1, 0, 1, 3)
        self.plainTextEditMessage = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditMessage.setMinimumSize(QtCore.QSize(300, 80))
        self.plainTextEditMessage.setMaximumSize(QtCore.QSize(16777215, 80))
        self.plainTextEditMessage.setBaseSize(QtCore.QSize(0, 100))
        self.plainTextEditMessage.setObjectName("plainTextEditMessage")
        self.gridLayout.addWidget(self.plainTextEditMessage, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.menuUser.addAction(self.actionLogin)
        self.menubar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSend.setText(_translate("MainWindow", "Send"))
        self.labelPeerHost.setText(_translate("MainWindow", "Peer\'s host name or  ip address: "))
        self.pushButtonConnect.setText(_translate("MainWindow", "Connect"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
