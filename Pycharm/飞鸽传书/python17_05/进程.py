# multiprocessing模块就是跨平台版本的多进程模块
# 提供了一个Process类来代表一个进程对象

from multiprocessing import Process
import time


def work():
    while True:
        print("=====1======")
        time.sleep(1)

p1 = Process(target=work)
p1.start()
for i in range(5):
    print("======2======")
    time.sleep(1)

print(p1.is_alive())        # 判断子进程是否存活
p1.terminate()      # 终止子进程
