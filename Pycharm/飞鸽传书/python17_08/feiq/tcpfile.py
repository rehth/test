# 创建tcp 用作文件的收发
import socket
import coredata
import threading

file_list = list()


def tcp_file(queue):
    # 创建一个线程用作接收处理queue的数据, 并设定为守护主线程
    que_thread = threading.Thread(target=recv_queue_info, args=(queue,))
    que_thread.setDaemon(True)
    que_thread.start()
    # 生成一个服务器socket，并绑定端口
    server_tcp_socket = create_tcp_socket()
    server_tcp_socket.bind(("", coredata.fq_port))
    # 端口复用
    server_tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 设置监听模式，变主动 为被动, 参数为最大监听数
    server_tcp_socket.listen(128)
    while True:
        client_socket, ip_port = server_tcp_socket.accept()
        # 创建一个线程，用作与客服端的数据通信(传递文件)
        client_socket = threading.Thread(target=client_server_socket, args=(client_socket,))
        client_socket.start()


def create_tcp_socket():
    # 创建一个tcp socket,并返回
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return tcp_socket


def client_server_socket(client_socket):
    # 一个线程，用作与客服端的数据通信(传递文件)
    recv_data = client_socket.recv(1024)
    # print(recv_data.decode("gbk"))    # 测试输出
    # 对数据进行处理，得到请求的文件信息
    ask_file_dict = deal_client_data(recv_data)
    # 遍历已发送的文件消息列表
    for file_info in file_list:
        # 判断已发送的文件消息编号和请求文件编号是否相等
        if file_info["package"] == ask_file_dict["package"]:
            # print(file_info["name"])  # 测试输出
            file_name = file_info["name"]
            # 打开对应文件 以rb模式
            # 发送的文件最后不能是空行，如果是则发送失败 原因: linux 和 windows 的换行符不一致
            with open(file_name, "rb") as f:
                while True:
                    read_info = f.readline(1024)
                    if not read_info:
                        break
                    client_socket.send(read_info)
            break


def recv_queue_info(queue):
    # 循环接收 queue 的信息并放入一个列表中
    while True:
        file_info_dict = queue.get()
        file_list.append(file_info_dict)
        # print(file_list)  # 测试输出


def deal_client_data(recv_data):
    # 对数据进行处理，得到字典形式的请求文件信息
    # 1_lbt80_47#128#74E6E238FE3E#0#0#0#4000#9:1505921577:king:KING-PC:96:59c21f39:0:0:
    recv_info = recv_data.decode("gbk")
    recv_info_list = recv_info.split(":", 8)
    recv_info_dict = dict()
    recv_info_dict["package"] = int(recv_info_list[5], 16)
    recv_info_dict["index"] = recv_info_list[6]
    return recv_info_dict