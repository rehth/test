import multiprocessing as processing
import time
import os


class MyProcess(processing.Process):
    # def __init__(self, num):
    #     super().__init__(self)
    #     self.num = num

    def run(self):
        while True:
            print("====我的子进程====")
            time.sleep(1)

myprocess = MyProcess()
myprocess.start()

time.sleep(5)
print(myprocess.pid, os.getpid(), processing.current_process())

myprocess.join(2)
myprocess.terminate()

print("进程结束")
