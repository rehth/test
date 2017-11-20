import socket
import time


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8888))
    server_socket.listen(100)

    server_socket.setblocking(False)
    client_list = list()

    while True:
        try:
            client_socket, client_id = server_socket.accept()
        except BlockingIOError:
            print("本次循环没有新连接")
            time.sleep(1)
        else:
            print(client_id)
            client_socket.setblocking(False)
            client_list.append((client_socket, client_id))

        for client_socket, client_id in client_list:
            try:
                # rcv_data = ""
                # while True:
                #     data = client_socket.recv(10).decode()
                #     if not len(data):
                #         break
                #     rcv_data += data
                rcv_data = client_socket.recv(10).decode()
            except BlockingIOError:
                pass
            else:
                if not rcv_data:
                    print("%s客户端已关闭连接" % client_id)
                    client_socket.close()
                    client_list.remove((client_socket, client_id))
                print("%s:%s" % (client_id, rcv_data))

if __name__ == "__main__":
    main()