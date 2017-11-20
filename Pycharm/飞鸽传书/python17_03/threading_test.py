import threading
import time


# def dance():
#     print("dance")
#     time.sleep(1)
#
#
# def sing():
#     print("sing")
#     time.sleep(1)
#
# for i in range(5):
#     t1 = threading.Thread(target=dance)
#     t2 = threading.Thread(target=sing)
#     t1.start()
#     t2.start()
# print("流程结束")


def work1():
    # 线程间共享全局变量测试
    global g_num
    g_num += 5
    print(g_num)


def work2():
    print(g_num)

g_num = 100
print(g_num)
n1_thread = threading.Thread(target=work1)
n1_thread.start()
# time.sleep(3)
n2 = threading.Thread(target=work2)
n2.start()
print(threading.enumerate())
print(threading.active_count())