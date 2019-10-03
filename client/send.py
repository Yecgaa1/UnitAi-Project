# code:utf-8
import socket
import hashlib,time,os
from threading import Thread
#登录程序


def login(acc,pd):

	#print(123)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 19150
    try:
        s.connect((host, port))  # ip和端口

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
        #print(so)
        s.close()
        if (so == "S"):
            return 0
        elif(so=="A"):
            return 2
        else:
            return 1

        # login触发事件
    except:
        print("No server")

#发送文件函数
#标准文件发送函数(带检查，全加载式检查文件，不带进度，适用于10m以下）
def sendfile1(ip,port,head,whfile):
    s = socket.socket()
    ip = socket.gethostname()
    print(ip)
    print(port)
    s.connect((ip, port))
    print(1)
    s.send(head.encode('utf-8'))
    time.sleep(0.5)
    msg1 = s.recv(1)
    msg = msg1.decode('utf-8')
    while 1:
        if (msg == "A"):
            print("Access denine")
            s.close()
            return 1
        elif (msg == "O"):
            file = open(whfile, 'rb')
            f=file.read()
            s.send(f)
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')
            while 1:
                if (msg == "E"):
                    print("Send Error")
                    s.close()
                    return 2
                elif (msg == "C"):
                    print("Success")
                    break
                else:
                    time.sleep(0.5)
                    msg1 = s.recv(1)
                    msg = msg1.decode('utf-8')
            s.close()
            return 0
        else:
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')
    #try:


    #except:
        #print("No server")
        #return 3
#标准文件发送函数(带检查，分段式检查文件，不带进度，适用于10m以上，1m每块）
def sendfile2(ip,port,head,whfile):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.send(head.encode('utf-8'))
        time.sleep(0.5)
        msg1 = s.recv(1)
        msg = msg1.decode('utf-8')
        if(msg=="A"):
            print("Access denine")
            s.close()
            return 1
        elif(msg=="O"):
            file = {'file': open(whfile, 'rb')}
            block=int(file/1024)
            if(file%1024!=0):
                block+=1
            i=1
            t=0
            while i<=block:
                s.send(file[t:t+1025].encode('utf-8'))
                t+=1024
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')
            while 1:
                if(msg=="E"):
                    print("Send Error")
                    s.close()
                    return 2
                elif(msg=="C"):
                    print("Success")
                    break
                else:
                    time.sleep(0.5)
                    msg1 = s.recv(1)
                    msg = msg1.decode('utf-8')
            s.close()
            return 0
        else:
            time.sleep(0.5)
            msg1 = s.recv(1)
            msg = msg1.decode('utf-8')

    except:
        print("No server")
        return 0


def waitback(ip,port):
    s = socket.socket()
    s.connect((ip, port))
