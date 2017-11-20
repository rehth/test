import socket

# socket tcp 服务器的创建
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口 bind
tcp_socket.bind(("", 8080))

# 设置为监听模式
tcp_socket.listen(8)

# 等待客户端连接
client_socket, ip_port = tcp_socket.accept()

# 等待客户端数据
recv_data = client_socket.recv(1024)
print(recv_data.decode("gbk"))

# 给客户端发送数据
client_socket.send("请求已收到,正在处理".encode("gbk"))

# 关闭 socket
client_socket.close()
tcp_socket.close()
