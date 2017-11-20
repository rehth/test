import socket
import threading
import re
import sys
# import select
# from gevent import monkey
# monkey.patch_all()

g_static_path = './static'


class HttpServer(object):
    def __init__(self, port, apps):
        # 创建一个server,并进行设置
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        self.server_socket.listen(100)
        self.app = app
        self.response_data = ''
        self.env = None

    def start(self):
        while True:
            client_socket, client_id = self.server_socket.accept()
            client_thr = threading.Thread(target=self.deal_client, args=(client_socket, client_id))
            client_thr.start()

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
        match_obj = re.match("\w+\s+([^ ]+(\?)?[^ ]*)", client_data)
        #  "GET /index.html?user=python HTTP/1.1"
        if not match_obj:
            client_socket.close()
            return
        path = match_obj.group(1)
        if path == "/":
            path = "/index.html"

        self.env = {"path": path, "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Server": "PythonWeb2.0", "Accept-Encoding": "gzip, deflate"
                    }
        if re.search("\.html", path):
            response = self.dynamic_html()
        else:
            # print("静态网页")
            response = self.static_html()

        response_len = len(response)
        send_len = 0
        while send_len < response_len:
            send_len += client_socket.send(response[send_len:])

        client_socket.close()

    def dynamic_html(self):
        response_body = self.app(self.env, self.start_response)
        response = self.response_data.encode() + response_body
        return response

    def static_html(self):
        path = self.env.pop("path")
        head_list = list(self.env.items())
        try:
            with open(g_static_path + path, "rb") as f:
                file_data = f.read()
        except Exception as e:
            self.start_response("404 Not Found", head_list)
            response_body = str(e).encode('gbk')
        else:
            self.start_response("200 OK", head_list)
            response_body = file_data
        response = self.response_data.encode() + response_body
        return response

    def start_response(self, status, head_list):
        response_line = "HTTP/1.1 %s\r\n" % status
        response_head = ""
        for head in head_list:
            response_head += "%s:%s\r\n" % (head[0], head[1])
        self.response_data = response_line + response_head + "\r\n"
        # print(type(self.response_data))

# sys.path.append('./dynamic')
sys.path.insert(0, "./dynamic")
application = __import__("application")
app = getattr(application, "app")
http = HttpServer(10010, app)
http.start()