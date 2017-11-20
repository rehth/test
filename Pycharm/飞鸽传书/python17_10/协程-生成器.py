# 协程是python个中另外一种实现多任务的方式

import time


def work1():
    for i in range(6):
        print("work1:", i)
        yield
        time.sleep(2)


def work2():
    for i in range(6):
        print("work2:", i)
        yield
        time.sleep(2)

if __name__ == "__main__":
    w1 = work1()
    w2 = work2()
    while True:
        try:
            next(w1)
            next(w2)
        except StopIteration:
            break
