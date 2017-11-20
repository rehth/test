import multiprocessing
import os


def work(num):
    for i in range(1, 4):
        print("----pid=%d----num=%d----i=%d" % (os.getpid(), num, i))

# 创建进程池po, 进程数的最多可有3个
po = multiprocessing.Pool(3)

for j in range(10):
    # 向进程池中添加任务
    po.apply_async(work, (j,))
# 关闭进程池的任务添加功能
po.close()
# 使主进程等待进程池中的任务执行结束(默认不等待)
po.join()
