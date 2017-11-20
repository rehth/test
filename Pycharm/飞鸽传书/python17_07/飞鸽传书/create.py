# 完成 socket 和 msg 的创建, 以及打印功能目录
import socket
import CoreData
import time


def create_udp_socket():
    """创建一个 socket  并开启广播权限"""
    CoreData.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    CoreData.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    CoreData.udp_socket.bind(("", 2425))


def create_msg(command, option=""):
    CoreData.package_id = int(time.time())
    return "%d:%d:%s:%s:%d:%s" % (CoreData.feiq_version, CoreData.package_id,
                                  CoreData.feiq_user, CoreData.feiq_hostname, command, option)


def print_menu():
    print("飞秋在线V1.0".center(30))
    print("1.上线提醒".center(30))
    print("2.下线提醒".center(30))
    print("3.发送消息".center(30))
    print("4.群发消息".center(30))
    print("5.在线列表".center(30))
    print("6.发送文件".center(30))
    print("0.退出应用".center(30))
    return input("请输入操作号:")


def print_user_list():
    print("=" * 50)
    for i, user_info in enumerate(CoreData.user_list):
        print(i, user_info)
    print("=" * 50)
