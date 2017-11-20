import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 开启广播权限
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

"""
    1:123456789:itcast-python:localhost:32:hello

说明:
    1 版本号，一般为1，较高版本的飞秋则较为复杂
    123456789 数据包编号，主要用来标记这个数据包，一般不重复，所以可以使用time来得到一个
    itcast-python 电脑的用户名
    localhost 主机名
    32 发送消息的命令 (1-上线提醒  2-下线提醒)
    hello 发送的消息内容
"""
udp_info = "1:123456789:user:dell-pc:1:666"

udp_socket.sendto(udp_info.encode("gbk"), ("255.255.255.255", 2425))

udp_socket.close()
