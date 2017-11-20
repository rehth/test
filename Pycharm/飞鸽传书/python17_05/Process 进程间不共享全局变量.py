from multiprocessing import Process
import time


def work():
    global g_list
    for i in range(5):
        g_list.append(i)
        print("in Process1,g_list=%s" % g_list)
        time.sleep(1)
    print("in Process1,g_list=%s" % g_list)


def work2():
    print("in Process2,g_list=%s" % g_list)

g_list = [10086, 10010]

p1 = Process(target=work)
p1.start()
p1.join()       # 等待

p2 = Process(target=work2)
p2.start()


# print(p1.is_alive())  # 判断子进程是否存活
# p1.terminate()  # 终止子进程
