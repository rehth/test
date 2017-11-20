# 完成信息的发送的模块
# import socket
import CoreData
import create
import os


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


def send_msg_file():
    """
    版本号:包编号:用户名:主机名:命令字:消息\0文件序号:文件名:文件大小:文件修改时间:文件类型:
    1:123123:dongge:ubuntu:文件消息命令字:消息内容(可以没有) \0 0:hello.py:123:12123:文件类型:
    命令字: IPMSG_SENDMSG | IPMSG_FILEATTACHOPT IPMSG_FILEATTACHOPT = 0x00200000
    文件类型: IPMSG_FILE_REGULAR
    """
    send_ip = input("请输入ip(输入0显示在线列表):")
    if send_ip == "0":
        create.print_user_list()
        index = input("请输入序号:")
        send_ip = CoreData.user_list[int(index)]["ip"]

    file_name = input("文件名(输入0显示当前列表):")
    if file_name == "0":
        print("="*50)
        file_list = os.listdir(".")
        for i in enumerate(file_list):
            print(i)
        print("="*50)
        index = input("请输入序号:")
        file_name = file_list[int(index)]

    command = CoreData.IPMSG_SENDMSG | CoreData.IPMSG_FILEATTACHOPT
    print(command)
    option = "\0 " + "0:" + file_name + ":" + str(os.path.getsize(file_name))\
             + ":" + str(os.path.getctime(file_name)) + ":" + str(CoreData.IPMSG_FILE_REGULAR)
    file_msg = create.create_msg(command, option)
    send_msg(file_msg, send_ip)
    # 制作queue
    file_info = dict()
    file_info["packageid"] = CoreData.package_id
    file_info["filename"] = file_name
    file_info["index"] = 0
    print(file_info)
    CoreData.queue.put(file_info)
