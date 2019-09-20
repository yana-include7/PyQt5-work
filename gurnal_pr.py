# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gurnal_pr.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1296, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 40pt \"Microsoft YaHei\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"border-radius: 15px\n"
"")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"border-radius: 15px")
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("font: 20pt \"Microsoft YaHei\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("font: 24pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("font: 12pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Журнал продаж"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "показать"))


