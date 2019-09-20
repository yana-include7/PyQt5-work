# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_okno_opl.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 172)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 18pt \"Microsoft YaHei\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 24pt \"Microsoft YaHei\";\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.oplnal = QtWidgets.QPushButton(Dialog)
        self.oplnal.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ruble.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oplnal.setIcon(icon)
        self.oplnal.setIconSize(QtCore.QSize(30, 30))
        self.oplnal.setObjectName("oplnal")
        self.gridLayout.addWidget(self.oplnal, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Downloads/credit-card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Downloads/payment-method.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.oplnal.setText(_translate("Dialog", "   ОПЛАТА НАЛИЧНЫМИ   "))
        self.pushButton_2.setText(_translate("Dialog", "   ОПЛАТА ПО КАРТЕ   "))
        self.pushButton_3.setText(_translate("Dialog", "   СЛОЖНАЯ ОПЛАТА   "))


