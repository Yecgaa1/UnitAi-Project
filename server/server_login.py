#导入必要包
import json
import socket,pymysql
#导入自定义函数

#内函数






#建立连接
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 19150             # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
def login():
    msg1 = c.recv(16)
    ac = msg1.decode('utf-8')
    print(ac)
    msg1 = c.recv(64)
    pd = msg1.decode('utf-8')
    print(pd)
    #json 校验
    db = pymysql.connect("192.168.0.3", "account", "019150", "account")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql ="select*from acc where name='"+ac+"'"
    #print(sql)
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    #print(data)
    if str(data)!="()":
        for row in data:
            if row[4]==pd:
                c.send("S".encode('utf-8'))
            else:
                c.send("N".encode('utf-8'))
    else:
        c.send("A".encode('utf-8'))


while True:
    c, addr = s.accept()     # 建立客户端连接。
    msg1 = c.recv(2)
    msg = msg1.decode('utf-8')
    if(msg=="lo"):
        login()

