# 控制程序运行
import socket
import coredata
import recvmsg
import sendmsg
import threading
import tcpfile
import multiprocessing


def create_udp_socket():
    # 创建一个upd socket
    coredata.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    coredata.udp_socket.bind(("", coredata.fq_port))
    # 开启广播权限
    coredata.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # 端口复用
    coredata.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)


def print_menu():
    # 打印功能菜单
    print("飞秋在线V1.0".center(30))
    print("1.上线提醒".center(30))
    print("2.下线提醒".center(30))
    print("3.发送消息".center(30))
    print("4.群发消息".center(30))
    print("5.在线列表".center(30))
    print("6.发送文件".center(30))
    print("0.退出应用".center(30))
    return input("请输入操作号:")


def print_online_user():
    # 显示在线用户
    print("=" * 50)
    for index, user in enumerate(coredata.user_list):
        print("%d: %s" % (index, user))
    print("=" * 50)


def main():
    # 创建一个queue 用作进程间通信
    coredata.queue = multiprocessing.Queue()
    # 创建一个进程(设定为守护主进程) 处理文件的发送和接收
    tcp_process = multiprocessing.Process(target=tcpfile.tcp_file, args=(coredata.queue,))
    tcp_process.daemon = True
    tcp_process.start()

    # 创建一个 udp socket
    create_udp_socket()
    # 建立一个子线程 用作消息接收
    recv_thread = threading.Thread(target=recvmsg.recv_msg)
    # 设定守护主线程
    recv_thread.setDaemon(True)
    # 启动子线程
    recv_thread.start()
    while True:
        # 打印功能菜单
        num = int(print_menu())
        if num == 1:
            # 发送上线提醒给所有人
            sendmsg.send_msg_online()
        elif num == 2:
            # 发送下线提醒给所有人
            sendmsg.send_msg_offline()
        elif num == 3:
            # 通过指定ip发送消息
            sendmsg.send_msg_2_ip()
        elif num == 4:
            # 通过广播发消息给所有人
            sendmsg.send_msg_2_all()
        elif num == 5:
            # 显示在线用户
            print_online_user()
        elif num == 6:
            # 发送文件消息给指定ip
            # 发送的文件最后不能是空行，如果是则发送失败
            # 原因: linux 和 windows 的换行符不一致
            sendmsg.send_msg_file()
        elif num == 0:
            # 发送下线提醒给所有人并退出
            sendmsg.send_msg_offline()
            exit()
            break
    # 关闭udp socket
    coredata.udp_socket.close()

if __name__ == '__main__':
    main()