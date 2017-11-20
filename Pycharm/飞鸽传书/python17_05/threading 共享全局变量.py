import threading
import time

g_num = 100
g_list = list()


def work1():
    global g_num
    for i in range(5):
        g_num += i
        g_list.append(i)
    print(g_num)
    print(g_list)


def work2():
    time.sleep(1)
    print(g_num)
    print(g_list)

work1_thread = threading.Thread(target=work1)
work2_thread = threading.Thread(target=work2)
work1_thread.start()
work2_thread.start()

l = threading.Lock()
l.acquire()
l.release()
