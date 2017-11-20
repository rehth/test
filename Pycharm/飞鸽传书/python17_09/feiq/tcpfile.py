# 创建tcp 用作文件的收发
import socket
import coredata
import threading
import sendmsg

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
    # 关闭服务器socket
    # server_tcp_socket.close()


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
        if file_info["package"] == ask_file_dict["package"] and file_info["ip"] == 0:
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
    # 关闭socket
    client_socket.close()


def recv_queue_info(queue):
    # 循环接收 queue 的信息并放入一个列表中
    while True:
        file_info_dict = queue.get()
        # 如果是发送文件类型
        if file_info_dict["type"] == "send_file":
            file_list.append(file_info_dict["data"])
        # 如果是下载文件类型
        elif file_info_dict["type"] == "download_file":
            file_info = file_info_dict["data"]
            print("下载的文件为: %s" % file_info["name"])
            # 开启一个线程 开始文件下载
            download_thread = threading.Thread(target=download_file, args=(file_info,))
            download_thread.start()
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


def download_file(file_info):
    # 创建客户端tcp socket
    client_tcp_socket = create_tcp_socket()
    # 连接服务器的socket
    client_tcp_socket.connect((file_info["ip"], coredata.fq_port))
    # 制作文件下载的请求消息 注意命令为十六进制数 %x 不是 %d
    download_msg_option = "%x:%x:0:" % (file_info["package"], file_info["index"])
    download_msg = sendmsg.create_msg(coredata.IPMSG_GETFILEDATA, download_msg_option)
    # 发送请求给服务器
    client_tcp_socket.send(download_msg.encode("gbk"))
    """
        client_tcp_socket.send(download_msg)
        TypeError: a bytes-like object is required, not 'str'
        未进行编码, 导致异常出现
    """
    # 进行文件下载 并打印可能的异常信息
    try:
        # 以 wb 的模式打开一个文件(自动关闭)
        with open(file_info["name"], "wb") as f:
            write_data = 0  # 已写入文件的数据大小
            # 循环写入数据
            while True:
                # 堵塞式消息接收　注意
                f_info = client_tcp_socket.recv(1024)
                f.write(f_info)
                write_data += len(f_info)
                # print(f_info)     # 测试输出
                # 循环的退出条件：信息为空 或 大小
                if (not f_info) or (write_data >= file_info["size"]):
                    break
    # 出现异常的情况
    except Exception as e:
        print("文件<%s>下载失败, 出现异常%s" % (file_info["name"], e))
    # 没有异常的情况
    else:
        print("文件<%s>下载成功" % (file_info["name"]))
    # file = open(file_info["name"], "wb")
    # write_data = 0
    # while True:
    #     info = client_tcp_socket.recv(1024)
    #     if not info:
    #         break
    #     # print(info)
    #     file.write(info)
    #     write_data += len(info)
    #     if write_data >= file_info["size"]:
    #         break
    # file.close()
    # 关闭这个socket
    client_tcp_socket.close()
