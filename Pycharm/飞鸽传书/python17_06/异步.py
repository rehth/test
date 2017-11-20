"""
我的理解
    异步：
        即知道要做某件事，但不确定什么时候做
        则可用异步处理
    同步：*协同步调*,按预定次序执行
"""

import multiprocessing
import time
import os


def work1():
    for j in range(3):
        print("----work1----%d----%d" % (os.getpid(), os.getppid()))
        time.sleep(1)
    return "hello"


def work2(*args):
    print("work2----%s----" % args)
    print("work2----%d----" % os.getpid())

po = multiprocessing.Pool(2)
po.apply_async(func=work1, callback=work2)

for i in range(10):
    time.sleep(1)
    print("-----main-----%d" % os.getpid())
print("over")

