import socket

# 创建一个tcp socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接与服务器
tcp_socket.connect(("192.168.93.96", 8080))

# 给服务器发送消息
tcp_socket.send("客户端发送消息测试！".encode("gbk"))

# 等待服务器的回复
recv_data = tcp_socket.recv(1024)
print(recv_data.decode("gbk"))

# 关闭socket
tcp_socket.close()

