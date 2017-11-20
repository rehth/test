# 主程序：控制程序的进行
import CoreData
import create
import recvmsg
import sendmsg
import tcpsocket
import threading
import multiprocessing


if __name__ == '__main__':
    # 创建一个队列 用作存储发送文件的信息
    CoreData.queue = multiprocessing.Queue()

    # 创建一个子进程 用于文件 的收发
    tcp_file = multiprocessing.Process(target=tcpsocket.send_file_tcp, args=(CoreData.queue,))
    tcp_file.daemon = True
    tcp_file.start()

    create.create_udp_socket()
    recv_thread = threading.Thread(target=recvmsg.recv_msg)
    recv_thread.setDaemon(True)
    recv_thread.start()
    while True:
        num = create.print_menu()
        if num == "1":
            sendmsg.send_msg_online()
        elif num == "2":
            sendmsg.send_msg_offline()
        elif num == "3":
            sendmsg.send_msg_2_ip()
        elif num == "4":
            sendmsg.send_msg_2_all()
        elif num == "5":
            create.print_user_list()
        elif num == "6":
            sendmsg.send_msg_file()
            # tcpsocket.send_file_tcp()
        elif num == "0":
            sendmsg.send_msg_offline()
            break
    CoreData.udp_socket.close()




