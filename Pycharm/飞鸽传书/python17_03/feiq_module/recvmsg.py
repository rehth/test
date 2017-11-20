# 飞秋接收消息模块
import variate


def recv_msg():
    while True:
        recv_info, ip_port = variate.udp_socket.recvfrom(1024)
        recv_msg_dict = deal_msg(recv_info)
        print(recv_msg_dict)


def deal_msg(recv_info):
    """
       对接收的消息进行处理
       接收的消息是1_lbt80_82#131200#F48E38F22501#0#0#0#4000#9
       :1505826164:84360:DESKTOP-DNAA8RA:6291459:你猜
    """
    recv_info = recv_info.decode("gbk")
    recv_msg_list = recv_info.split(":", 5)
    if len(recv_msg_list) == 6:
        recv_msg_dict = dict()
        recv_msg_dict["version"] = recv_msg_list[0]
        recv_msg_dict["packagenum"] = recv_msg_list[1]
        recv_msg_dict["user"] = recv_msg_list[2]
        recv_msg_dict["hostname"] = recv_msg_list[3]
        recv_msg_dict["command"] = recv_msg_list[4]
        recv_msg_dict["optional"] = recv_msg_list[5]
        return recv_msg_dict
