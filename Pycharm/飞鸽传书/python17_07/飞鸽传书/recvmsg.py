# 完成信息接收的模块
# import socket
import CoreData
import sendmsg


def save_user_info(username, ip):
    user_info = dict()
    for user in CoreData.user_list:
        if user["ip"] == ip:
            break
    else:
        user_info["user"] = username
        user_info["ip"] = ip
        CoreData.user_list.append(user_info)


def remove_user_info(ip):
    for user_info in CoreData.user_list:
        if user_info["ip"] == ip:
            CoreData.user_list.remove(user_info)


def recv_msg():
    while True:
        recv_info, ip_port = CoreData.udp_socket.recvfrom(1024)
        recv_info = recv_info.decode("gbk", errors="ignore")
        recv_info_dict = deal_msg(recv_info)
        # sendmsg.send_msg_ok(ip_port[0])
        # print(recv_info_dict)
        command_num, command_option = deal_command(recv_info_dict["command"])
        if command_num == CoreData.IPMSG_BR_ENTRY:
            print("[INFO]:%s上线了" % (recv_info_dict["option"]))
            sendmsg.send_msg_ok(CoreData.IPMSG_ANSENTRY, ip_port[0])
            save_user_info(recv_info_dict["user"], ip_port[0])

        elif command_num == CoreData.IPMSG_BR_EXIT:
            print("[INFO]:%s下线了" % (recv_info_dict["option"]))
            remove_user_info(ip_port[0])

        elif command_num == CoreData.IPMSG_ANSENTRY:
            print("[INFO]:%s也在线" % (recv_info_dict["user"]))
            save_user_info(recv_info_dict["user"], ip_port[0])

        elif command_num == CoreData.IPMSG_SENDMSG:
            print("[INFO]:%s: %s" % (recv_info_dict["user"], recv_info_dict["option"]))
            sendmsg.send_msg_ok(CoreData.IPMSG_RECVMSG, ip_port[0])


def deal_msg(info):
    #
    """
    1_lbt80_8#128#80FA5B42A569#0#0#0#4000#9:1505470103:
    hasee:DESKTOP-KG65FBS:6291459:35_孙志成
    """
    info_list = info.split(":", 5)
    if len(info_list) == 6:
        info_dict = dict()
        info_dict["version"] = info_list[0]
        info_dict["package"] = info_list[1]
        info_dict["user"] = info_list[2]
        info_dict["hostname"] = info_list[3]
        info_dict["command"] = info_list[4]
        info_dict["option"] = info_list[5]
        return info_dict
    else:
        return "消息不符合规范, 不予显示"


def deal_command(command):
    # 对命令进行处理, 提取命令num 和 命令option
    command_num = int(command) & 0x000000ff
    command_option = int(command) & 0xffffff00
    return command_num, command_option
