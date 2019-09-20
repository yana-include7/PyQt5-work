# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_podbor.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 16pt \"Microsoft YaHei\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setStyleSheet("font: 14pt \"Microsoft YaHei\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("font: 14pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"color: rgb(255, 31, 11);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);")
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "Поиск"))
        self.label_2.setText(_translate("Dialog", "Товар не найден!"))


