import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 20500                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
i=0
#SQL={0:{"number":"0","car":"AAAAA"}}
while True:
    c, addr = s.accept()     # 建立客户端连接。
    #i+=1
    #print('连接地址：', addr)
    #c.send('go'.encode(encoding="utf-8"))
    msg1 = c.recv(1024)
    msg=msg1.decode('utf-8')
    #if '#' in msg:
  
    #if "*" in msg:
    #  SQL[i]={"number":i,"car":msg}
    print(msg)

