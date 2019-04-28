#导入必要包
import json
import socket
#导入自定义函数

#内函数


#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 20500          # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接

while True:
    tctimeClient, addr = s.accept()
