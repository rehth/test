import threading
import time

# 自定义线程用处不明
# 同自定义异常讲法不同,未讲具体用法
# 估计用法:创建一个线程,掩盖内部实现.
# 而不是创建多个线程,参数可通过init方法传入
class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def show(self):
        for i in range(self.num):
            print("show")
            time.sleep(1)

    # def sing(self):
    #     for i in range(5):
    #         print("sing")
    #         time.sleep(1)

    def run(self):
        self.show()
        # self.sing()

mythread = MyThread(5)
mythread.run()