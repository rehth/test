# 互斥锁:线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。
"""
    互斥锁为资源引入一个状态：锁定/非锁定
    某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；
    直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。
    互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。

    锁的好处:
    确保了某段关键代码只能由一个线程从头到尾完整地执行

    锁的坏处:
    阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
    由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
"""
import threading

g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        my_lock.acquire()
        g_num += 1
        my_lock.release()
    print("work1:", g_num)      # work1: 1224242


def work2(num):
    global g_num
    for i in range(num):
        my_lock.acquire()
        g_num += 1
        my_lock.release()
    print("work2:", g_num)      # work2: 1338459
my_lock = threading.Lock()
work1_thread = threading.Thread(target=work1, args=(1000000,))
work2_thread = threading.Thread(target=work2, args=(1000000,))
work1_thread.start()
work2_thread.start()