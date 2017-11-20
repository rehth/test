import socket
import threading


# 1. 创建一个tcp 套接字
tcp_browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.　连接服务器
tcp_browser_socket.connect(("127.0.0.1", 10086))

# 3. 发送数据请求
request = "GET / HTTP/1.1\n"
Host = "Host: 127.0.0.1\n"
request_msg = request + Host + "\n"
tcp_browser_socket.send(request_msg.encode())

# 4. 接收服务器的数据
recv_data = tcp_browser_socket.recv(4096)
print(recv_data)
recv_info = recv_data.decode()
print(recv_info)

# 5. 关闭socket
tcp_browser_socket.close()
"""
HTTP/1.1 404 Not Found
Server: PythonWebServer2.0
"""

"""
HTTP/1.1 200 OK
Server: PythonWebServer2.0

<!DOCTYPE html>
<html>
<head>
<title>Welcome </title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to Our's Python Web Server!</h1>
<p>If you see this page, the python web server is successfully installed and
working. Further configuration is required.</p>


<p><em>Thank you for using.</em></p>
</body>
</html>


"""
threading.Thread(args=(12,))
