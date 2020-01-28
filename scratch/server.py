# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\server.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 510)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditMessages = QtWidgets.QTextEdit(Dialog)
        self.textEditMessages.setMinimumSize(QtCore.QSize(300, 400))
        self.textEditMessages.setObjectName("textEditMessages")
        self.gridLayout.addWidget(self.textEditMessages, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.gridLayout.addWidget(self.lineEditMessage, 1, 0, 1, 1)
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.gridLayout.addWidget(self.pushButtonSend, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Server"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
