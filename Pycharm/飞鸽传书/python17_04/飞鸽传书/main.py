# 主程序：控制程序的进行
import CoreData
import create
import recvmsg
import sendmsg
import threading


if __name__ == '__main__':
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
        elif num == "0":
            sendmsg.send_msg_offline()
            break
    CoreData.udp_socket.close()




