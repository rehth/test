"""
test1:
    什么是HTTP协议?
    HTTP是在网络上传输HTML的协议

    什么是HTML?
    HTML是一种用来定义网页的文本

    HTTP协议中常见响应状态码有哪些,分别代表什么意思?
    200 OK
    3xx 重定向
    404 NOT FOUND
    响应代码：200表示成功，3xx表示重定向
    4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误

    HTTP协议中常见请求方式有哪几个,分别代表什么意思?
    GET POST  GET还是POST，GET仅请求资源，POST会附带用户数据

    用socket实现一个简单web服务器的时候,用什么方法可以让端口立即重用
    sock.setsockopt(socket.soL_SOCKET, socket.SO_REUSEADDR, True)

    用户浏览器向服务器请求没有这个文件会返回什么？

         状态码:404
         页面:NOT FOUND

    用谷歌浏览器浏览http://nsdual.boxuegu.com,找出login_logo.png文件的请求方式,状态码,请求url地址
    Request URL:http://nsdual.boxuegu.com/images/login_logo.png
    Request Method:GET
    Status Code:200 OK
    Remote Address:192.168.50.187:80

    用正则匹配出上一题中Request URL中的请求地址和请求文件
import re
sss = Request URL:http://nsdual.boxuegu.com/images/login_logo.png
Request Method:GET
Status Code:200 OK
Remote Address:192.168.50.187:80

search_obj = re.search("[\w ]*(URL:.*/(.*\.png))", sss)
if search_obj:
    print(search_obj.group(1))
    print(search_obj.group(2))

    完成简单的HTTP服务器,静态文件的获取,404错误页面的呈现

"""
"""
test2:
    实现一个简单多线程HTTP静态服务器(用类)
    实现一个简单多进程HTTP静态服务器(用类)
    sys.argv的作用
"""
import socket
import sys
import re
import multiprocessing


class HttpServer(object):
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_socket.bind(("", port))

        self.server_socket.listen(100)

        self.client_num = 0

    def run(self):
        while True:
            try:
                client_socket, client_addr = self.server_socket.accept()
                client_pro = multiprocessing.Process(target=self.handler_client, args=(client_socket, client_addr))
                self.client_num += 1
                client_pro.start()
                # 关闭主进程中的client_socket
                client_socket.close()
            except KeyboardInterrupt or OSError:
                print("http服务器开始关闭")
                self.server_socket.close()

    def handler_client(self, client_socket, addr):
        response_line = "HTTP/1.1 200 OK\r\n"
        response_head = "Server: PythonWeb\r\n"
        response_body = None
        print("编号<%d>: 开始与客服端%s进行数据通信" % (self.client_num, addr))
        client_data = client_socket.recv(4096).decode()
        """
        GET / HTTP/1.1
        Host: 192.168.93.116:10086
        """
        search_data = re.search("(\w+)\s+([^ ]+)", client_data)
        if not search_data:
            client_socket.close()
            return
        path = search_data.group(2)
        if path == "/":
            path = "/003.jpg"
        print("编号<%d>: 客服端%s请求路径为:%s" % (self.client_num, addr, path))
        try:
            with open("."+path, "rb") as f:
                f_data = f.read()
        except FileNotFoundError as e:
            response_line = "HTTP/1.1 404 NOT FOUND\r\n"
            response_body = str(e).encode()
        else:
            response_body = f_data
        finally:
            response = (response_line + response_head + "\r\n").encode() + response_body
            response_len = len(response)
            send_len = 0
            if send_len < response_len:
                send_len += client_socket.send(response[send_len:])

        client_socket.close()
        self.client_num -= 1


def main():
    port0 = 10010
    argv_list = sys.argv
    if len(argv_list) == 2:
        try:
            port = int(argv_list[1])
            if port > 1023:
                port0 = port
            else:
                print("[ERRO]:参数应大于1023")
                return
        except ValueError or Exception:
            print("[INFO]:运行方式：python3 test_miniweb.py [10010]")
            return
    elif len(argv_list) > 2:
        print("[INFO]:运行方式：python3 test_miniweb.py [10010]")
        return
    http = HttpServer(port0)
    http.run()

if __name__ == '__main__':
    main()