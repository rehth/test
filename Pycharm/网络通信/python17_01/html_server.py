import socket
import threading


def main():
    # 创建一个socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口设置
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    server_socket.bind(("", 10086))
    # 设置监听模式
    server_socket.listen(108)
    # 构建循环
    while True:
        client_socket, client_addr = server_socket.accept()
        # 建立线程
        client_the = threading.Thread(target=client_server, args=(client_socket, client_addr))
        client_the.start()


def client_server(client_socket, addr):
    print("%s的链接建立成功" % str(addr))
    # 接收客服端的数据请求
    recv_data = client_socket.recv(4096).decode()
    print(recv_data)  # 测试输出
    """
    GET / HTTP/1.1
    Host: 192.168.93.116:10086
    """
    # recv_data.split()
    response_line = "HTTP/1.1 200 OK\r\n"
    response_heared = "server: python web\r\n"
    response_body = "欢迎进入我的世界".encode("gbk")
    response = (response_line + response_heared + "\r\n").encode("gbk") + response_body

    client_socket.send(response)
    client_socket.close()


if __name__ == '__main__':
    main()