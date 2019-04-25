
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
from login1 import  Ui_login
from Im import Ui_IM


with open("./config/config.json", 'r') as load_f:
    load_dict = json.load(load_f)



class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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
def root():
    if(lo_textaccount.text()=="xutongxin"):
        print("a")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/xlogin.jpg")))
        loginapp.setPalette(palette)
def login():
    print(123)
    loginButton.setEnabled(False)
    acc = lo_textaccount.text()
    pd = lo_textpassword.text()
    # 获取密码和账号
    load = {}

    if lo_remember.isChecked():
        if "acc" in load_dict:
            load_dict["acc"] = acc
            load_dict["pd"] = pd
        else:
            load_dict.update({"acc": acc})
            load_dict.update({"pd": pd})
        if load_dict["loginmode"] == 0:
            load_dict["loginmode"] = 1
        # print(load_dict)
        with open("./config/config.json", "w") as f:
            json.dump(load_dict, f)
    if lo_Auto.isChecked() and load_dict["loginmode"] != 2:
        load_dict["loginmode"] = 2
        with open("./config/config.json", "w") as f:
            json.dump(load_dict, f)

    # 以下为建立tcp连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 20500
    s.connect((host, port))  # ip和端口
    s.send("lo".encode('utf-8'))
    sha256 = hashlib.sha256()
    s.send(acc.encode('utf-8'))
    time.sleep(1)
    sha256.update(pd.encode('utf-8'))
    res = sha256.hexdigest()
    s.send(res.encode('utf-8'))
    # time.sleep(1)

    msg1 = s.recv(1)
    so = msg1.decode('utf-8')
    print(so)
    if (so == "S"):
        loginButton.setText("登录成功")
        loginapp.close()
        Imapp.show()
        Im_reload(acc)
    else:
        loginButton.setEnabled(True)
        loginButton.setText("密码错误")
    s.close()
#login触发事件

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

