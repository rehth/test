import socket
import time

# 版本号
feiq_version = 1
# 用户名
feiq_username = "白起"
# 主机名
feiq_hostname = "杀神"
# 飞秋命令集
IPMSG_BR_ENTRY = 0x00000001
IPMSG_BR_EXIT = 0x00000002
IPMSG_SENDMSG = 0x00000020
# 广播ip地址
feiq_broadcast = "255.255.255.255"
# 飞秋的端口
feiq_port = 2425
# 全局变量
udp_socket = None


def create_udp_socket():
    global udp_socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)


def create_msg(command, info):
    return "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()), feiq_username,
                                  feiq_hostname, command, info)


def send_msg(msg, aim_ip):
    udp_socket.sendto(msg.encode("gbk"), (aim_ip, feiq_port))


def send_online_msg():
    online_msg = create_msg(IPMSG_BR_ENTRY, feiq_username)
    print(online_msg)
    send_msg(online_msg, feiq_broadcast)


def send_offline_msg():
    # offline_msg = "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()), feiq_username,
    #                                      feiq_hostname, IPMSG_BR_EXIT, feiq_username)
    #
    # udp_socket.sendto(offline_msg.encode("gbk"), (feiq_broadcast, feiq_port))
    offline_msg = create_msg(IPMSG_BR_EXIT, feiq_username)
    send_msg(offline_msg, feiq_broadcast)


def send_2_ip_msg():
    send_ip = input("请输入ip:")
    send_info = input("请输入要发送的内容:")
    if send_ip and send_info:
        msg = create_msg(IPMSG_SENDMSG, send_info)
        send_msg(msg, send_ip)


def send_msg_all():
    send_info = input("请输入要发送的内容:")
    msg = create_msg(IPMSG_SENDMSG, send_info)
    send_msg(msg, feiq_broadcast)


def recv_msg():
    while True:
        recv_info, ip_port = udp_socket.recvfrom(1024)
        recv_msg_dict = deal_msg(recv_info)
        print(recv_msg_dict)


def deal_msg(recv_info):
    """对接收的消息进行处理
       接收的消息是1_lbt80_82#131200#F48E38F22501#0#0#0#4000#9
       :1505826164:84360:DESKTOP-DNAA8RA:6291459:你猜
    """
    recv_msg_list = recv_info.decode("gbk").split(":")
    recv_msg_dict = dict()
    recv_msg_dict["version"] = recv_msg_list[0]
    recv_msg_dict["packagenum"] = recv_msg_list[1]
    recv_msg_dict["user"] = recv_msg_list[2]
    recv_msg_dict["hostname"] = recv_msg_list[3]
    recv_msg_dict["command"] = recv_msg_list[4]
    recv_msg_dict["optional"] = recv_msg_list[5]
    return recv_msg_dict


def print_menu():
    print("飞  鸽  传  书".center(40))
    print("1:上线提醒".center(40))
    print("2:发送消息".center(40))
    print("3:接收消息".center(40))
    print("4:群发消息".center(40))
    print("0:下线提醒".center(40))
    return input("操作号:")


def main():
    create_udp_socket()
    while True:
        num = print_menu()
        if num == "1":
            send_online_msg()
        elif num == "2":
            send_2_ip_msg()
        elif num == "3":
            recv_msg()
        elif num == "4":
            send_msg_all()
        elif num == "0":
            send_offline_msg()
            break
    udp_socket.close()

if __name__ == '__main__':
    main()
