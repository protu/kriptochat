# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 230)
        Dialog.setMinimumSize(QtCore.QSize(385, 230))
        Dialog.setMaximumSize(QtCore.QSize(385, 230))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 150, 174, 38))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelUsername = QtWidgets.QLabel(Dialog)
        self.labelUsername.setGeometry(QtCore.QRect(18, 48, 77, 22))
        self.labelUsername.setObjectName("labelUsername")
        self.lineEditUsername = QtWidgets.QLineEdit(Dialog)
        self.lineEditUsername.setGeometry(QtCore.QRect(100, 50, 251, 36))
        self.lineEditUsername.setText("")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setGeometry(QtCore.QRect(18, 92, 72, 22))
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(100, 90, 251, 36))
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelUsername.setText(_translate("Dialog", "Username:"))
        self.labelPassword.setText(_translate("Dialog", "Password:"))
