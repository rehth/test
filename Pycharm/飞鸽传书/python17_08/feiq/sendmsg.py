# 发送消息并处理
import coredata
import main
import os
"""
    send_msg_online()
    send_msg_offline()
    send_msg_2_ip()
    send_msg_2_all()
    send_msg_file()
"""


def create_msg(command, option=""):
    # 制作符合飞秋规范的 msg
    msg = "%d:%d:%s:%s:%d:%s" % (coredata.fq_version, coredata.fq_package, coredata.fq_user,
                                 coredata.fq_host, command, option)
    return msg


def send_msg(msg, ip):
    # 发送消息
    coredata.udp_socket.sendto(msg.encode("gbk"), (ip, coredata.fq_port))


def send_msg_online():
    # 发送上线提醒给所有人
    online_msg = create_msg(coredata.IPMSG_BR_ENTRY, coredata.fq_user)
    send_msg(online_msg, coredata.fq_broadcast)


def send_msg_offline():
    # 发送上线提醒给所有人
    offline_msg = create_msg(coredata.IPMSG_BR_EXIT, coredata.fq_user)
    send_msg(offline_msg, coredata.fq_broadcast)


def send_msg_2_ip():
    # 通过指定ip发送消息
    send_ip = input("请输入ip(按0可显示在线列表):")
    if send_ip == "0":
        main.print_online_user()
        index = int(input("请输入对应序号:"))
        send_ip = coredata.user_list[index]["ip"]
    msg = input("请输入内容:")
    if msg and send_ip:
        msg = create_msg(coredata.IPMSG_SENDMSG, msg)
        send_msg(msg, send_ip)


def send_msg_2_all():
    # 通过广播发消息给所有人
    msg = input("请输入内容:")
    if msg:
        msg = create_msg(coredata.IPMSG_SENDMSG, msg)
        send_msg(msg, coredata.fq_broadcast)


def send_msg_answer(command, ip):
    # 发送回复消息
    answer_msg = create_msg(command)
    send_msg(answer_msg, ip)


def send_msg_file():
    # 发送文件消息给指定ip
    # 发送的文件最后不能是空行，如果是则发送失败
    # 原因: linux 和 windows 的换行符不一致
    send_ip = input("请输入ip(按0可显示在线列表):")
    if send_ip == "0":
        main.print_online_user()
        index = int(input("请输入对应序号:"))
        send_ip = coredata.user_list[index]["ip"]

    name = input("请输入文件名(按0可显示当前目录):")
    if name == "0":
        file_list = os.listdir(".")
        for num, file in enumerate(file_list):
            print("%d: %s" % (num, file))
        index = int(input("请输入对应序号:"))
        name = file_list[index]

    if name and send_ip:
        # 创建对应消息并发送
        # "%d:%s:%x:%x:%x:"
        # % (0, file_name, file_size, int(file_ctime), FeiQCoreData.IPMSG_FILE_REGULAR)
        msg = "%d:%s:%x:%x:%x:" % \
              (0, name, os.path.getsize(name), int(os.path.getctime(name)), coredata.IPMSG_FILE_REGULAR)
        msg = "\0" + msg
        print(msg)
        command = coredata.IPMSG_SENDMSG | coredata.IPMSG_FILEATTACHOPT
        file_msg = create_msg(command, msg)
        send_msg(file_msg, send_ip)

        # 制作文件发送的信息字典,并放入队列
        file_info_dict = dict()
        file_info_dict["name"] = name
        file_info_dict["package"] = coredata.fq_package
        file_info_dict["index"] = 0
        coredata.queue.put(file_info_dict)