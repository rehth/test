# 完成信息的发送的模块
# import socket
import CoreData
import create


def send_msg(msg, aim_ip):
    CoreData.udp_socket.sendto(msg.encode("gbk"), (aim_ip, CoreData.feiq_port))


def send_msg_online():
    online_msg = create.create_msg(CoreData.IPMSG_BR_ENTRY, CoreData.feiq_user)
    send_msg(online_msg, CoreData.feiq_broadcast)


def send_msg_offline():
    offline_msg = create.create_msg(CoreData.IPMSG_BR_EXIT, CoreData.feiq_user)
    send_msg(offline_msg, CoreData.feiq_broadcast)


def send_msg_2_ip():
    send_ip = input("请输入ip(输入0显示在线列表):")
    if send_ip == "0":
        create.print_user_list()
        index = input("请输入序号:")
        send_ip = CoreData.user_list[int(index)]["ip"]
    msg = input("请输入你要发送的消息:")
    msg = create.create_msg(CoreData.IPMSG_SENDMSG, msg)
    send_msg(msg, send_ip)


def send_msg_2_all():
    msg = input("请输入你要发送的消息:")
    msg = create.create_msg(CoreData.IPMSG_SENDMSG, msg)
    send_msg(msg, CoreData.feiq_broadcast)


def send_msg_ok(command, recv_ip):
    ok_msg = create.create_msg(command)
    send_msg(ok_msg, recv_ip)
