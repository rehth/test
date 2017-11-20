# 飞秋的发送消息模块
import variate
import create


def send_msg(msg, aim_ip):
    variate.udp_socket.sendto(msg.encode("gbk"), (aim_ip, variate.feiq_port))


def send_online_msg():
    online_msg = create.create_msg(variate.IPMSG_BR_ENTRY, variate.feiq_username)
    send_msg(online_msg, variate.feiq_broadcast)


def send_offline_msg():
    offline_msg = create.create_msg(variate.IPMSG_BR_EXIT, variate.feiq_username)
    send_msg(offline_msg, variate.feiq_broadcast)


def send_2_ip_msg():
    send_ip = input("请输入ip:")
    send_info = input("请输入要发送的内容:")
    if send_ip and send_info:
        msg = create.create_msg(variate.IPMSG_SENDMSG, send_info)
        send_msg(msg, send_ip)


def send_msg_all():
    send_info = input("请输入要发送的内容:")
    msg = create.create_msg(variate.IPMSG_SENDMSG, send_info)
    send_msg(msg, variate.feiq_broadcast)
