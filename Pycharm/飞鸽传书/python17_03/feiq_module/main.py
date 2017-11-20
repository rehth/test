# 飞秋的主程序，控制程序的运行
import create
import threading
import variate
import sendmsg
import recvmsg



def print_menu():
    print("飞鸽传书".center(40))
    print("1:上线提醒".center(40))
    print("2:下线提醒".center(40))
    print("3:发送消息".center(40))
    print("4:群发消息".center(40))
    print("0:退出".center(40))

    return input("操作号:")


def main():
    create.create_udp_socket()
    recv_thread = threading.Thread(target=recvmsg.recv_msg)
    recv_thread.setDaemon(True)
    recv_thread.start()
    while True:
        num = print_menu()
        if num == "1":
            sendmsg.send_online_msg()
        elif num == "2":
            sendmsg.send_offline_msg()
        elif num == "3":
            sendmsg.send_2_ip_msg()
        elif num == "4":
            sendmsg.send_msg_all()
        elif num == "0":
            sendmsg.send_offline_msg()
            break
    variate.udp_socket.close()

if __name__ == '__main__':
    main()
