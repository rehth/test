# 进程实现　web server 的多任务
import socket
# import threading
import re
import multiprocessing
import os

server_port = 9527


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    server_socket.bind(("", server_port))

    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        client_pro = multiprocessing.Process(target=handler_client, args=(client_socket,))
        # client_pro.daemon = True
        client_pro.start()
        # 关闭主进程中的client_socket
        client_socket.close()   # socket


def handler_client(client_socket):
    recv_data = client_socket.recv(4096).decode()
    print(recv_data)
    """
    GET / HTTP/1.1
    Host: 192.168.93.110:10086
    """

    search_url = re.search("[A-Z]+\s+([^ ]+)\s+HTTP+", recv_data)
    if not search_url:
        client_socket.close()
        return
    path = search_url.group(1)
    # print("----------")
    print(path)
    # print("-------------")
    if path == "/":
        path = "/index.html"

    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "server: PythonWeb 1.0\r\n"
    response_body = None

    try:
        f = open("."+path, "rb")
        print("."+path)
    except Exception as e:
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = str(e).encode()
    else:
        data = f.read()
        # print(data)
        f.close()
        response_body = data
        # f.close()
    finally:
        response = (response_line + response_header + "\r\n").encode() + response_body

        client_socket.send(response)
    client_socket.close()


if __name__ == '__main__':
    main()