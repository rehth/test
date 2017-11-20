import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口是以元祖的形式传入参数
udp_socket.bind(("", 9527))

udp_info = input("请输入:")

udp_socket.sendto(udp_info.encode("gbk"), ("192.168.93.75", 2425))

# 数据的接收, 数据的形式：（"数据", (ip, port))
udp_recv, ip_port = udp_socket.recvfrom(1024)

print(udp_recv.decode("gbk"), ip_port)

udp_socket.close()
