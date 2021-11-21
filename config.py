# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Clear.setGeometry(QtCore.QRect(190, 340, 80, 24))
        self.pb_Clear.setObjectName("pb_Clear")
        self.pb_Connect = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Connect.setGeometry(QtCore.QRect(280, 170, 80, 24))
        self.pb_Connect.setStyleSheet("#pb_Connect:checked{\n"
"background-color: rgb(0, 255, 0);\n"
"}")
        self.pb_Connect.setCheckable(True)
        self.pb_Connect.setObjectName("pb_Connect")
        self.txt_Result = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_Result.setGeometry(QtCore.QRect(10, 30, 256, 301))
        self.txt_Result.setObjectName("txt_Result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.pb_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Refresh.setGeometry(QtCore.QRect(480, 40, 80, 24))
        self.pb_Refresh.setObjectName("pb_Refresh")
        self.pb_Send = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Send.setGeometry(QtCore.QRect(380, 170, 80, 24))
        self.pb_Send.setObjectName("pb_Send")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(280, 40, 191, 116))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_Port = QtWidgets.QComboBox(self.layoutWidget1)
        self.cb_Port.setObjectName("cb_Port")
        self.verticalLayout.addWidget(self.cb_Port)
        self.cb_BaudRate = QtWidgets.QComboBox(self.layoutWidget1)
        self.cb_BaudRate.setObjectName("cb_BaudRate")
        self.verticalLayout.addWidget(self.cb_BaudRate)
        self.lineEdit_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.verticalLayout.addWidget(self.lineEdit_ID)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.verticalLayout.addWidget(self.lineEdit_IP)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(480, 130, 91, 24))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.PORT = QtWidgets.QLabel(self.splitter_2)
        self.PORT.setObjectName("PORT")
        self.lineEdit_Port = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_Clear.setText(_translate("MainWindow", "Clear"))
        self.pb_Connect.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Tag Result"))
        self.pb_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.pb_Send.setText(_translate("MainWindow", "Send"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.label_3.setText(_translate("MainWindow", "Baud Rate"))
        self.label_4.setText(_translate("MainWindow", "ID"))
        self.label_5.setText(_translate("MainWindow", "IP"))
        self.PORT.setText(_translate("MainWindow", "PORT"))