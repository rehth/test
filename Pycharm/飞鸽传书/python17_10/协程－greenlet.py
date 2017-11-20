# 利用　greenlet 实现协程
# 需要手动切换
# 原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)
# 操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，
# 再在适当的时候切换回来继续执行
from greenlet import greenlet
import time


def work1():
    for i in range(6):
        print("work1:", i)
        time.sleep(0.2)
        # 切换到协程２中执行
        w2.switch()


def work2():
    for i in range(6):
        print("work2:", i)
        time.sleep(0.2)
        # 切换到协程１中执行
        w1.switch()

if __name__ == '__main__':
    # 创建两个协程对象
    w1 = greenlet(work1)
    w2 = greenlet(work2)
    # 启动greenlet 使用　switch
    w1.switch()