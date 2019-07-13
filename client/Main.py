import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import  QApplication, QPushButton, QMenu,QLineEdit,QMainWindow,QDialog
from PyQt5.QtCore import QCoreApplication,QTimer,QThread,pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QPixmap,QPalette,QBrush
import sys

#基本五大包导入

#以下为导入功能包
import hashlib
import socket
import json
import time

#以下为导入自定义函数
#窗口
from login import  Ui_login
from Im import Ui_IM
#发送数据程序
from send import login


with open("./config/config.json", 'r') as load_f:
    load_dict = json.load(load_f)



class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('登录')
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 系统图标
        self.setWindowIcon(QIcon('.\images\Iron.png'))

        self.main_ui = Ui_login()
        self.main_ui.setupUi(self)

class ImWindow(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)

        self.child=Ui_IM()
        self.child.setupUi(self)

def login_action():
    #loginButton = loginapp.main_ui.loginButton
    loginButton.clicked.connect(login)

    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/normal.jpg")))
    loginapp.setPalette(palette)

    lo_textaccount.editingFinished.connect(root)
#login事件总线
def Im_reload(sacc):
    Im_account.setText(sacc)
    if sacc=="xutongxin":
        Im_account.setStyleSheet("font: 12pt \"萝莉体 第二版\";\n"
                              "color: rgb(102, 204, 255);")



def root():
    if(lo_textaccount.text()=="xutongxin"):
        print("a")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/xlogin.jpg")))
        loginapp.setPalette(palette)
def login():
    login()

if __name__=='__main__':

    app=QApplication(sys.argv)
    loginapp=LoginWindow()
    Imapp=ImWindow()

    lo_textpassword = loginapp.main_ui.textpassword
    lo_remember = loginapp.main_ui.remember
    lo_Auto = loginapp.main_ui.Auto
    lo_textaccount = loginapp.main_ui.textaccount
    loginButton = loginapp.main_ui.loginButton
    #login类继承

    login_action()#login事件总线

    Im_account =Imapp.child.account


    loginapp.show()



    sys.exit(app.exec_())


