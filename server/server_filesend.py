import json
import socket
from threading import Thread
#导入自定义函数
#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 11171            # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(5)                 # 等待客户端连接
while True:
    connect_socket, client_addr = s.accept()
    thread_do_service = Thread(target=do_service, args=(connect_socket,))
    thread_do_service.start()
