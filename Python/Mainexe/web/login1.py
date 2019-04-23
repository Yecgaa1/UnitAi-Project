# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import  QApplication, QPushButton, QMenu,QLineEdit,QMainWindow,QLabel
from PyQt5.QtCore import QCoreApplication,QTimer,QThread,pyqtSignal,Qt
from PyQt5.QtGui import QIcon, QPainter, QPixmap,QPalette,QBrush
import sys

#基本五大包导入

#基本四大类导入

# PyQt5.QtWidgets import*
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *

#以下为导入功能包
import socket
import os
import json
import hashlib
import time
import ctypes
#以下为导入自定义函数

import proxy




class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.test=123
        self.setupUi(self)
    def proxyon(self):
        proxy.proxy()
    def login(self):
        self.loginButton.setText("登陆中")
        self.loginButton.setEnabled(False)
        acc = self.textaccount.text()
        pd = self.textpassword.text()

        #获取密码和账号
        #以下为建立tcp连接
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 20500
        s.connect((host, port))#ip和端口
        s.send("lo".encode('utf-8'))
        sha256 = hashlib.sha256()
        s.send(acc.encode('utf-8'))
        time.sleep(1)
        sha256.update(pd.encode('utf-8'))
        res = sha256.hexdigest()
        s.send(res.encode('utf-8'))
        #time.sleep(1)

        msg1 = s.recv(1)
        so = msg1.decode('utf-8')
        print(so)
        if(so=="S"):
            self.loginButton.setText("登录成功")
        else:
            self.loginButton.setEnabled(True)
            self.loginButton.setText("密码错误")
        s.close()

    def root(self):
        if(self.textaccount.text()=="root"):
            print("a")
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/login.jpg")))
            self.setPalette(palette)

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        self.setWindowTitle('登录')
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")#系统图标
        self.setWindowIcon(QIcon('.\images\Iron.png'))
        Dialog.resize(400, 280)
        self.textaccount = QtWidgets.QLineEdit(Dialog)
        self.textaccount.setGeometry(QtCore.QRect(100, 60, 256, 31))
        self.textaccount.setObjectName("account")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 54, 20))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.textpassword = QtWidgets.QLineEdit(Dialog)
        self.textpassword.setGeometry(QtCore.QRect(100, 140, 256, 31))
        self.textpassword.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 54, 20))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(90, 200, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.visitButton = QtWidgets.QPushButton(Dialog)
        self.visitButton.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.visitButton.setObjectName("visitButton")
        self.proxyButton = QtWidgets.QPushButton(Dialog)
        self.proxyButton.setGeometry(QtCore.QRect(10, 250, 75, 23))
        self.proxyButton.setObjectName("proxyButton")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 200, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 250, 110, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #完成界面第一初始化
        #以下为修改界面参数

        # 设置文本框的默认浮现文本 https://blog.csdn.net/jia666666/article/details/81510502
        self.textaccount.setPlaceholderText("账号")
        self.textpassword.setPlaceholderText("密码")
        # QLineEdit.NoEcho：不显示任何输入的字符，常用于密码类型的输入，且长度保密
        self.textpassword.setEchoMode(QLineEdit.Password)
        #设置背景



        #无边框
        #self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint)

        #按钮事件绑定
        self.textaccount.editingFinished.connect(self.root)
        self.loginButton.clicked.connect(self.login)
        self.proxyButton.clicked.connect(self.proxyon)
        # 结束第二初始化
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "  账号 "))
        self.label_2.setText(_translate("Dialog", "  密码"))
        self.checkBox.setText(_translate("Dialog", "保存密码"))
        self.loginButton.setText(_translate("Dialog", "登录"))
        self.proxyButton.setText(_translate("Dialog", "代理设置"))
        self.checkBox_2.setText(_translate("Dialog", "自动登录"))
        self.comboBox.setItemText(0, _translate("Dialog", "Language:中文"))
        self.comboBox.setItemText(1, _translate("Dialog", "Language:English"))
        self.comboBox.setItemText(2, _translate("Dialog", "Language:"))
        self.visitButton.setText(_translate("Dialog", "普通使用"))
        #本地化


#以下为启动器
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui()

    sys.exit(loginapp.exec_())