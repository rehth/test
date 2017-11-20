# 利用　gevent 实现协程
# 最为常用　自动切换

from gevent import monkey
import gevent
import time


def work1(n, m):
    for i in range(n, m):
        # 获取当前的协程
        print(gevent.getcurrent())
        print("work1:", i)
        # 当打上补丁　可用time 模块延时
        time.sleep(0.2)
        # 用来模拟一个耗时操作，注意不是time模块中的sleep
        # gevent.sleep(0.2)


def work2(n, m):
    for i in range(n, m):
        print(gevent.getcurrent())
        print("work2:", i)
        gevent.sleep(0.2)

if __name__ == "__main__":
    monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

    # # 第一种写法:
    # # 使用gevent指派执行的任务
    # # 第一个参数就是指派的函数名
    # w1 = gevent.spawn(work1, 1, 10)
    # w2 = gevent.spawn(work2, 1, 10)
    # # 等待协程执行完
    # w1.join()
    # w2.join()

    # 写法二:
    # gevent.joinall([gevent.spawn(work1, 1, 10), gevent.spawn(work2, 1, 10)])