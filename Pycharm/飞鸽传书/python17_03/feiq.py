import time
import socket


def print_menu():
    print("飞秋在线V1.0")
    print("1.上线")
    print("2.广播消息")
    print("3.发送消息")
    print("4.发送消息")
    print("0.离线")


def out_feiq():
    msg = "1:" + str(time.time()) + ":" + user_name + ":" + pc_name + ":2:" + user_name
    udp_socket.sendto(msg.encode("gbk"), (broadcast_ip, PORT))


def send_msg():
    send_ip = input("请输入ip:")
    msg0 = input("请输入要发送的内容：")
    msg = "1:" + str(time.time()) + ":" + user_name + ":" + pc_name + ":32:" + msg0
    udp_socket.sendto(msg.encode("gbk"), (send_ip, PORT))


def send_msg_all():
    msg0 = input("请输入要发送的内容：")
    msg = "1:" + str(time.time()) + ":" + user_name + ":" + pc_name + ":32:" + msg0
    udp_socket.sendto(msg.encode("gbk"), (broadcast_ip, PORT))


def on_feiq():
    msg = "1:" + str(time.time()) + ":" + user_name + ":" + pc_name + ":1:" + user_name
    udp_socket.sendto(msg.encode("gbk"), (broadcast_ip, PORT))


def recv_msg():
    # 结果失败 使用 udp socket 来接收消息时 如何指定ip接收
    # 或者接收想接收的数据 而不是接收上线信息就结束了
    while True:
        recv_info, ip_port = udp_socket.recvfrom(1024)
        recv_date = recv_info.decode("gbk")
        print(recv_date)
        print(type(recv_date))
        # if 失败
        if int(recv_date[recv_date.rindex(":", 0, recv_date.rindex(":")),recv_date.rindex(":")]) > 2:
            print(recv_info.decode("gbk"))
            break


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", 8888))
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
user_name = input("请输入用户名：")
pc_name = input("请输入pc名：")
broadcast_ip = "255.255.255.255"
PORT = 2425


def main():
    while True:
        print_menu()
        num = input("操作号：")
        if num == "1":
            on_feiq()
        elif num == "2":
            send_msg_all()
        elif num == "3":
            send_msg()
        elif num == "4":
            # pass
            recv_msg()
        elif num == "0":
            out_feiq()
            break

if __name__ == '__main__':
    main()
