import socket
import threading


def client_server_tcp(tcp_client_socket):
    while True:
        recv_info = tcp_client_socket.recv(1024)
        if len(recv_info) == 0:
            tcp_client_socket.close()
            break
        print(recv_info.decode("gbk"))
        tcp_client_socket.send("请求已收到，正在处理".encode("gbk"))


tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("", 10010))

tcp_server_socket.listen(10)

while True:
    tcp_client_socket, ip_port = tcp_server_socket.accept()
    print(tcp_client_socket)    # <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM,
    #                             # proto=0, laddr=('192.168.93.100', 10086), raddr=('192.168.93.89', 62169)>
    # print(ip_port)      # ('192.168.93.89', 62169)
    client_thread = threading.Thread(target=client_server_tcp, args=(tcp_client_socket,))
    client_thread.setDaemon(True)
    client_thread.start()


