# 飞秋的创造模块 用来创建socket msg
import variate
import socket
import time


def create_udp_socket():
    variate.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    variate.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    variate.udp_socket.bind(("", 2425))


def create_msg(command, info):
    return "%d:%d:%s:%s:%d:%s" % (variate.feiq_version, int(time.time()), variate.feiq_username,
                                  variate.feiq_hostname, command, info)

