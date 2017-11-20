import socket
import gevent
import re
from gevent import monkey
monkey.patch_all()


class HttpServer(object):
    def __init__(self, port, app):
        # 创建一个server,并进行设置
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        self.server_socket.listen(100)
        self.app = app
        self.response_data = None

    def start(self):
        while True:
            client_socket, client_id = self.server_socket.accept()
            # print(client_id)
            gevent.spawn(self.deal_client, client_socket, client_id)
            # client_g.start()

    def deal_client(self, client_socket, client_id):
        print("开始与%s建立连接" % str(client_id))
        client_data = client_socket.recv(4096).decode()
        """
            GET / HTTP/1.1
            Host: 192.168.93.118:10010
            User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
            Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
            Accept-Encoding: gzip, deflate
            Connection: keep-alive
            Upgrade-Insecure-Requests: 1
        """
        match_obj = re.match("\w+\s+([^ ]+)", client_data)
        if not match_obj:
            client_socket.close()
            return
        path = match_obj.group(1)
        if path == "/":
            path = "/index.html"
        if path.endswith(".py"):
            env = {"Host": "%s:%s" % (client_id[0], client_id[1]), "path": path}
            response = self.dynamic_html(env)
        else:
            response = self.static_html(path)
        response_len = len(response)
        send_len = 0
        while send_len < response_len:
            send_len += client_socket.send(response[send_len:])
        client_socket.close()

    def dynamic_html(self, env):
        response_body = self.app(env, self.start_response)
        response = self.response_data.encode() + response_body
        return response

    def static_html(self, path):
        response_head = "Accept-Encoding: gzip, deflate\r\n"
        try:
            with open("./" + path, "rb") as f:
                file_data = f.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_body = str(e).encode()
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_body = file_data
        response = (response_line + response_head + "\r\n").encode() + response_body
        return response

    def start_response(self, status, head_list):
        response_line = "HTTP/1.1 %s\r\n" % status
        response_head = "%s:%s\r\n" % (head_list[0][0], head_list[0][1])
        response_head += "Server: PythonWeb2.0\r\n"
        response_head += "Accept-Encoding: gzip, deflate\r\n"
        self.response_data = response_line + response_head + "\r\n"


application = __import__("application")
app = getattr(application, "app")
http = HttpServer(10010, app)
http.start()