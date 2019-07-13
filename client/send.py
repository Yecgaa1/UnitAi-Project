import socket
from threading import Thread
#登录程序


def login():

	#print(123)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 19150
    try:
        s.connect((host, port))  # ip和端口
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
        if (so == "S"):
            loginButton.setText("登录成功")
            loginapp.close()
            Imapp.show()
            Im_reload(acc)
        else:
            loginButton.setEnabled(True)
            loginButton.setText("密码错误")
        s.close()
        # login触发事件
    except:
        print("No server")

#发送文件函数
#标准文件发送函数(带检查，全加载式检查文件，不带进度，适用于10m以下）
def sendfile1(int ip,int port,str head,str whfile)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.send(head.encode('utf-8'))
        time.sleep(0.5)
        msg1 = c.recv(1)
        msg = msg1.decode('utf-8')
        while:
            if(msg=="A")
                print("Access denine")
                s.close()
                return 1
            elif:(msg=="O")
                file = {'file': open(whfile, 'rb')}
                s.send(file.encode('utf-8'))
                time.sleep(0.5)
                msg1 = c.recv(1)
                msg = msg1.decode('utf-8')
                while:
                    if(msg=="E")
                        print("Send Error")
                        s.close()
                        return 2
                    elif(msg=="C")
                        print("Success")
                        break
                    else:
                        time.sleep(0.5)
                        msg1 = c.recv(1)
                        msg = msg1.decode('utf-8')
                s.close()
                return 0
            else:
                time.sleep(0.5)
                msg1 = c.recv(1)
                msg = msg1.decode('utf-8')

    except:
        print("No server")
        return 3
#标准文件发送函数(带检查，分段式检查文件，不带进度，适用于10m以上，1m每块）
def sendfile2(int ip,int port,str head,str whfile)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.send(head.encode('utf-8'))
        time.sleep(0.5)
        msg1 = c.recv(1)
        msg = msg1.decode('utf-8')
        if(msg=="A")
            print("Access denine")
            s.close()
            return 1
        elif:(msg=="O")
            file = {'file': open(whfile, 'rb')}
            block=int(file/1024)
            if(file%1024!=0)
                block+=1
            i=1
            t=0
            while i<=block:
                s.send(file[t:t+1025].encode('utf-8'))
                t+=1024
            time.sleep(0.5)
            msg1 = c.recv(1)
            msg = msg1.decode('utf-8')
            while:
                if(msg=="E")
                    print("Send Error")
                    s.close()
                    return 2
                elif(msg=="C")
                    print("Success")
                    break
                else:
                    time.sleep(0.5)
                    msg1 = c.recv(1)
                    msg = msg1.decode('utf-8')
            s.close()
            return 0
        else:
            time.sleep(0.5)
            msg1 = c.recv(1)
            msg = msg1.decode('utf-8')

    except:
        print("No server")
        return 0
print("123")
