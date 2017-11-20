import socket

# udp 协议的数据发送
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_info = input("请输入要发送的消息：")

# 数据的发送 数据发送的参数形式：("数据", (ip, port))
udp_socket.sendto(send_info.encode("gbk"), ("192.168.93.75", 8080))

udp_recv, ip_prot = udp_socket.recvfrom(1024)
print(udp_recv.decode("gbk"))
# 关闭
udp_socket.close()
