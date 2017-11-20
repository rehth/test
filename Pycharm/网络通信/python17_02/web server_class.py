# 创建类来实现 web server
# 多任务实现是协程
import gevent
import socket
import re
import sys
from gevent import monkey
monkey.patch_all()
# port = 10086


class HttpServer(object):
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        self.server_socket.listen(100)

    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            gevent.spawn(self.handler_client, client_socket)

    def handler_client(self, client_socket):
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
        response_line, response_body = self.read_file(path_data)
        self.handler_client_response(client_socket, response_line, response_body)
        client_socket.close()

    @staticmethod
    def handler_client_response(client_socket, response_line, data):
        response_header = "Server: PythonWeb 1.1+\r\n"
        response_body = None
        if data:
            response_body = data
        # 如果数据过大将导致数据发送不完整
        response = (response_line + response_header + "\r\n").encode() + response_body
        response_len = len(response)
        send_len = 0
        while send_len < response_len:
            send_len += client_socket.send(response[send_len:])

    @staticmethod
    def read_file(path):
        if path == "/":
            path = "/index.html"
        try:
            with open("."+path, "rb") as f:
                f_data = f.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_body = str(e).encode()
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_body = f_data
        return response_line, response_body


def main():
    args = sys.argv
    port0 = 10086
    if len(args) == 2:
        try:
            port0 = int(args[1])
        except Exception as e:
            print("运行方式：python3 web\ server_class.py [10086]", e)
            # print(e)
            exit()
    elif len(args) > 2:
        print("运行方式：python3 web\ server_class.py [10086]")
        exit()
    http = HttpServer(port0)
    http.start()

if __name__ == '__main__':
    main()
