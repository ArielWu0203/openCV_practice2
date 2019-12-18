# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 80))
        self.groupBox.setObjectName("groupBox")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(10, 30, 191, 29))
        self.btn1.setObjectName("btn1")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 221, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn2.setGeometry(QtCore.QRect(0, 40, 221, 29))
        self.btn2.setObjectName("btn2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 10, 211, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn3_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn3_1.setGeometry(QtCore.QRect(10, 30, 191, 29))
        self.btn3_1.setObjectName("btn3_1")
        self.btn3_2 = QtWidgets.QPushButton(Dialog)
        self.btn3_2.setGeometry(QtCore.QRect(280, 80, 191, 29))
        self.btn3_2.setObjectName("btn3_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 130, 221, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn4 = QtWidgets.QPushButton(self.groupBox_4)
        self.btn4.setGeometry(QtCore.QRect(0, 40, 221, 29))
        self.btn4.setObjectName("btn4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "1. Stereo"))
        self.btn1.setText(_translate("Dialog", "1.1 Disparity"))
        self.groupBox_2.setTitle(_translate("Dialog", "2. Background subtraction"))
        self.btn2.setText(_translate("Dialog", "2.1 Background subtraction"))
        self.groupBox_3.setTitle(_translate("Dialog", "3. Feature Tracking"))
        self.btn3_1.setText(_translate("Dialog", "3.1 Preprocessing"))
        self.btn3_2.setText(_translate("Dialog", "3.2 Video tracking"))
        self.groupBox_4.setTitle(_translate("Dialog", "4. Augmented Reality"))
        self.btn4.setText(_translate("Dialog", "4.1 Augmented Reality"))
