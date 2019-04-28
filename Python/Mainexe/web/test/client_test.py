import socket
import os

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 20500

# 连接服务，指定主机和端口
s.connect((host, port))
file_name="123.jpg"
# 接收小于 1024 字节的数据
new_file = open(file_name, "wb")

while True:
        size = s.recv(20)
        print(size)
        # 接收服务器端返回的内容
        mes = s.recv(int(size))
        # 如果内容不为空执行
        if mes:
            # 解码并向文件内写入
            print(1)
            new_file.write(mes)

            # 计算字节
            print(1)
        new_file.close()
        break