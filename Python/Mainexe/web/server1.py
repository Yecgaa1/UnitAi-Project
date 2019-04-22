#导入必要包
import socket
#导入自定义函数

#内函数






#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 20500                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
def login():
    msg1 = c.recv(64)
    ac = msg1.decode('utf-8')
    msg1 = c.recv(64)
    pd = msg1.decode('utf-8')

    #json 校验

while True:
    c, addr = s.accept()     # 建立客户端连接。
    msg1 = c.recv(2)
    msg = msg1.decode('utf-8')
    if(msg=="lo"):
        login()

