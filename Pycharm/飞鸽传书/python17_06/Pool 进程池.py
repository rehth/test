import multiprocessing
import time
import os


def work():
    for i in range(5):
        print("----work----pid= %d" % os.getpid())
        time.sleep(1)

po = multiprocessing.Pool(3)
for i in range(5):
    po.apply_async(work)

po.close()
po.join()
print("流程结束")
