# 线程实现　web server 的多任务
# 如果　response body　的数据过大，可能导致发放数据不完整
# 可采用多次循环发送　解决　
# socket.send 有一个返回值　表示发送的数据大小(字节)
import gevent
import socket
import re
from gevent import monkey
monkey.patch_all()
port = 10086


def handler_client(client_socket):
    client_data = client_socket.recv(4096).decode()
    """
     GET / HTTP/1.1
     Host: 192.168.93.110:10086
     """
    search_path = re.search("\w+\s+([^ ]+)", client_data)
    if not search_path:
        client_socket.close()
        return
    path_data = search_path.group(1)
    if path_data == "/":
        path_data = "/index.html"
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server: PythonWeb 1.1+\r\n"
    response_body = None
    try:
        with open("."+path_data, "rb") as f:
            f_data = f.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = str(e).encode()
    else:
        response_body = f_data
    finally:
        # 如果数据过大将导致数据发送不完整
        response = (response_line + response_header + "\r\n").encode() + response_body
        response_len = len(response)
        send_len = 0
        while send_len < response_len:
            send_len += client_socket.send(response[send_len:])
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("", port))

    server_socket.listen(100)

    while True:
        client_socket, client_addr = server_socket.accept()

        gevent.spawn(handler_client, client_socket)

if __name__ == '__main__':
    main()