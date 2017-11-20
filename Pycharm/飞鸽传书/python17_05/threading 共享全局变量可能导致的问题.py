import threading

g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("work1:", g_num)      # work1: 1224242


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("work2:", g_num)      # work2: 1338459

work1_thread = threading.Thread(target=work1, args=(1000000,))
work2_thread = threading.Thread(target=work2, args=(1000000,))
work1_thread.start()
work2_thread.start()
