import socket
import time
# import select


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.93.47", 8888))

# 设置为非堵塞模式
client_socket.setblocking(False)

while True:
    # 在非堵塞模式下, 没有接收到消息会报错BlockingIOError
    # 故这里使用异常处理
    try:
        rcv_data = client_socket.recv(10).decode()
    except BlockingIOError:
        print("本次没有接收到数据")
        time.sleep(1)
        # continue
    else:
        if not rcv_data:
            client_socket.close()
        print(rcv_data)

