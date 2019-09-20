# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pip.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 637)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 8pt \"Microsoft YaHei\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font: 12pt \"Microsoft YaHei\";\n"
"background-color: rgb(255, 31, 11);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255)\n"
"\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 20pt \"Microsoft YaHei\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"border-radius: 15px")
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 20pt \"Microsoft YaHei\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("font: 20pt \"Microsoft YaHei\";\n"
"border-radius: 15px")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Downloads/order.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Downloads/add-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Downloads/carrot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setStyleSheet("background-color:  rgb(250, 239, 214);\n"
"font: 16pt \"Microsoft YaHei\";\n"
"border-radius: 15px\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Downloads/down-chevron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setStyleSheet("background-color:  rgb(250, 239, 214);\n"
"font: 16pt \"Microsoft YaHei\";\n"
"border-radius: 15px\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Downloads/vverh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_4.addWidget(self.pushButton_25)
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_4.addWidget(self.pushButton_24)
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_4.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_4.addWidget(self.pushButton_27)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_5.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_5.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_5.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_5.addWidget(self.pushButton_31)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("font: 14pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px;\n"
"color:  rgb(185, 177, 159)")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(200)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color: rgb(255, 31, 11);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255)\n"
"")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("font: 14pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px;\n"
"color:  rgb(185, 177, 159)")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(200)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font: 16pt \"Microsoft YaHei\";\n"
"background-color: rgb(255, 31, 11);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 18pt \"Microsoft YaHei\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("font: 10pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 28pt \"Microsoft YaHei\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 40)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_11.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 0, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_12.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_14.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_13.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 1, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_15.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_16.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 1, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_17.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_18.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 2, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_19.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 2, 2, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_20.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 3, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_21.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 3, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_22.setStyleSheet("font: 18pt \"Microsoft YaHei\";\n"
"background-color:  rgb(250, 239, 214);\n"
"border-radius: 15px")
        self.pushButton_22.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Downloads/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setIcon(icon5)
        self.pushButton_22.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 3, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setStyleSheet("background-color:  rgb(250, 239, 214);\n"
"font: 28pt \"Microsoft YaHei\";\n"
"border-radius: 15px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Downloads/ruble.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon6)
        self.pushButton_23.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_3.addWidget(self.pushButton_23)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "касса"))
        self.pushButton_2.setText(_translate("MainWindow", "склад"))
        self.pushButton_3.setText(_translate("MainWindow", "настроки"))
        self.pushButton_4.setText(_translate("MainWindow", "техническая поддержка"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "Предупрждение"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "товар"))
        self.pushButton_6.setText(_translate("MainWindow", "новый"))
        self.pushButton_7.setText(_translate("MainWindow", "подбор"))
        self.pushButton_8.setText(_translate("MainWindow", "дополнительно"))
        self.pushButton_9.setText(_translate("MainWindow", "скрыть"))
        self.pushButton_25.setText(_translate("MainWindow", "возврат"))
        self.pushButton_24.setText(_translate("MainWindow", "внесение"))
        self.pushButton_26.setText(_translate("MainWindow", "выемка"))
        self.pushButton_27.setText(_translate("MainWindow", "X-отчёт"))
        self.pushButton_28.setText(_translate("MainWindow", "Z-отчёт"))
        self.pushButton_29.setText(_translate("MainWindow", "журнал продаж"))
        self.pushButton_30.setText(_translate("MainWindow", "отложить чек"))
        self.pushButton_31.setText(_translate("MainWindow", "продолжить чек"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Штрих-Код / Марка"))
        self.label_7.setText(_translate("MainWindow", "Ошибка"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Марка"))
        self.label_8.setText(_translate("MainWindow", "Ошибка"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_11.setText(_translate("MainWindow", "8"))
        self.pushButton_12.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "4"))
        self.pushButton_15.setText(_translate("MainWindow", "5"))
        self.pushButton_16.setText(_translate("MainWindow", "6"))
        self.pushButton_17.setText(_translate("MainWindow", "7"))
        self.pushButton_18.setText(_translate("MainWindow", "2"))
        self.pushButton_19.setText(_translate("MainWindow", "3"))
        self.pushButton_20.setText(_translate("MainWindow", "0"))
        self.pushButton_21.setText(_translate("MainWindow", "."))
        self.pushButton_23.setText(_translate("MainWindow", "   оплата   "))


