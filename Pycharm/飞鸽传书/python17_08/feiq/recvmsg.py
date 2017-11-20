# 接收消息并进行处理
import coredata
import sendmsg


def deal_recv_msg(recv_data):
    # 对数据进行解码
    recv_info = recv_data.decode("gbk", errors="ignore")
    # 把数据按 ":" 进行分割，得到一个由字符串组成的列表
    recv_info_list = recv_info.split(":", 5)
    # 新建一个字典 用作存储列表的相应数据
    recv_info_dict = dict()
    recv_info_dict["version"] = recv_info_list[0]
    recv_info_dict["package"] = recv_info_list[1]
    recv_info_dict["user"] = recv_info_list[2]
    recv_info_dict["host"] = recv_info_list[3]
    recv_info_dict["command"] = recv_info_list[4]
    recv_info_dict["option"] = recv_info_list[5]
    return recv_info_dict


def deal_recv_command(command):
    command_num = int(command) & 0x000000ff
    command_option = int(command) & 0xffffff00
    return command_num, command_option


def save_online_user(user, ip):
    # 遍历在线用户列表
    for user_info in coredata.user_list:
        # 如果列表中存在该ip，则退出，否则加入列表
        if user_info["ip"] == ip:
            break
    else:
        user_dict = dict()
        user_dict["user"] = user
        user_dict["ip"] = ip
        coredata.user_list.append(user_dict)


def remove_offline_user(ip):
    # 遍历在线用户列表
    for user_info in coredata.user_list:
        # 如果列表中存在该ip，则从列表中移除
        if user_info["ip"] == ip:
            coredata.user_list.remove(user_info)
            break


def recv_msg():
    # 接收消息是一直进行的，故应使用循环
    while True:
        # udp 接收消息
        recv_data, ip_port = coredata.udp_socket.recvfrom(1024)
        # 调用函数对接收的消息进行处理，得到一个字典
        recv_data_dict = deal_recv_msg(recv_data)
        # print(recv_data_dict)   # 测试输出 \rhahah\r  在linux中 \n 表示换行
        # 对得到的命令进行处理
        command_num, command_option = deal_recv_command(recv_data_dict["command"])
        # print(command_num)  # 测试输出
        # 根据命令进行划分
        if command_num == coredata.IPMSG_BR_ENTRY:
            print("[INFO]:<%s> 上线了" % (recv_data_dict["user"]))
            # 保存在在线用户列表中
            save_online_user(recv_data_dict["user"], ip_port[0])
            # 发送回复消息
            sendmsg.send_msg_answer(coredata.IPMSG_ANSENTRY, ip_port[0])

        elif command_num == coredata.IPMSG_BR_EXIT:
            print("[INFO]:<%s> 下线了" % (recv_data_dict["user"]))
            # 删除其在在线列表
            remove_offline_user(ip_port[0])

        elif command_num == coredata.IPMSG_ANSENTRY:
            print("[INFO]:<%s> 也在线" % (recv_data_dict["user"]))
            save_online_user(recv_data_dict["user"], ip_port[0])

        elif command_num == coredata.IPMSG_SENDMSG:
            # print("接收到的消息：%s" % (recv_data_dict["option"]))
            print("[INFO]:<%s> %s" % (recv_data_dict["user"], recv_data_dict["option"]))
            sendmsg.send_msg_answer(coredata.IPMSG_RECVMSG, ip_port[0])