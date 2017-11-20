import socket
import threading
import recvmsg
import sendmsg
send_file_list = list()


def send_file_tcp(queue):
    # 开辟子线程用作queue的数据处理
    que_thread = threading.Thread(target=deal_queue, args=(queue,))
    # que_thread.setDaemon(True)
    que_thread.start()

    server_socket = create_tcp_socket()
    server_socket.bind(("", 2425))
    server_socket.listen(5)
    while True:
        client_socket, ip_port = server_socket.accept()
        client_thread = threading.Thread(target=client, args=(client_socket,))
        # client_thread.setDaemon(True)
        client_thread.start()


def create_tcp_socket():
    """创建一个tcp 套接字， 并返回"""
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return tcp_socket


def client(client_socket):
    recv_data = client_socket.recv(1024)
    # print(recv_data.decode("gbk"))  # 1:1505833732:king:KING-PC:96:59c0d595:0:0:
    # recv_dict = recvmsg.deal_msg(recv_data.decode("gbk"))
    # print(type(recv_dict["option"]))
    recv_list = recv_data.decode("gbk").split(":", 7)
    recv_info_dict = dict()
    recv_info_dict["id"] = int(recv_list[-3], 16)
    for info in send_file_list:
        if recv_info_dict["id"] == info["packageid"]:
            # print("%s, %s" % (recv_info_dict["id"], type(recv_info_dict["id"]))
            print("%s, %s" % (info["packageid"], type(info["packageid"])))

            print(info["filename"])
            with open(info["filename"], "rb") as f:
                while True:
                    line_info = f.readline(1024)
                    if line_info:
                        print(line_info)
                        # 发送失败 原因未知
                        client_socket.send(line_info)
                    else:
                        break
            break
            # file_name = info["filename"]
            # try:
            #     f = open(file_name, "rb")
            #     while True:
            #         info = f.readline(1024)
            #         if info:
            #             print(info)
            #             client_socket.send(info)
            #         else:
            #             break
            #     f.close()
            # except Exception as e:
            #     print("异常：", e)
            # else:
            #     print("发送成功")
            # break
    client_socket.close()


def deal_queue(queue):
    while True:
        send_file_list.append(queue.get())

