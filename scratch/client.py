# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 510)
        self.textEditMessages = QtWidgets.QTextEdit(Dialog)
        self.textEditMessages.setGeometry(QtCore.QRect(10, 10, 341, 441))
        self.textEditMessages.setObjectName("textEditMessages")
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessage.setGeometry(QtCore.QRect(10, 460, 341, 32))
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(360, 460, 88, 34))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(380, 10, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
        self.label.setText(_translate("Dialog", "Client"))
