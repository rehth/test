import socket
import select


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8888))
    server_socket.listen(100)
    # 设置为非堵塞
    server_socket.setblocking(False)
    # 创建一个　epoll 对象
    myepoll = select.epoll()
    # 将创建的　socket 添加到 epoll 的事件监听中
    myepoll.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)
    # 定义一个字典, 用作存储连接的客户端
    client_dict = dict()
    while True:
        # client_socket, client_id = server_socket.accept()
        # 通过调用创建的epoll对象的方法poll(), 会返回一个列表(符合监听要求的)
        epoll_list = myepoll.poll()
        # epoll_list 的元素　(文件描述符fb, 事件(select.EPOLL..))
        for fb, event in epoll_list:
            # 如果是socket创建的套接字(server_socket)被激活
            if fb == server_socket.fileno():
                client_socket, client_id = server_socket.accept()
                print("开始与客户端%s建立连接" % str(client_id))

                client_socket.setblocking(False)

                client_dict[client_socket.fileno()] = (client_socket, client_id)

                myepoll.register(client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
            elif event == select.EPOLLIN:
                client_socket = client_dict[fb][0]
                client_id = client_dict[fb][1]

                # 循环接收数据
                # print(client_id)
                try:
                    rcv_data = ""
                    while True:
                        rcv_data += client_socket.recv(10).decode("gbk")
                        # 客服端断开连接的退出条件
                        if not len(rcv_data):
                            break
                        # rcv_data += data
                    # print(rcv_data)
                except BlockingIOError:
                    pass
                    # print(bool(rcv_data))

                # rcv_data = client_socket.recv(1024).decode("gbk")

                if not rcv_data:
                    print("客户端%s已断开连接" % str(client_id))
                    # 从 epoll 中移除该 连接 fd
                    myepoll.unregister(fb)
                    client_socket.close()
                    del client_dict[fb]
                else:
                    print("%s:%s" % (client_id, rcv_data))


if __name__ == '__main__':
    main()