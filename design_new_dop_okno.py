# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_new_dop_okno.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 243)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font:20pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))


