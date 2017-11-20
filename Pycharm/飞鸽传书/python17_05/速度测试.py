import time


def sudu(num):
    for i in range(num):
        for j in range(num):
            for k in range(num):
                pass

t_start = time.time()
sudu(1000)
t_stop = time.time()

# 遍历1000**3次耗时: 25.14
print("执行时间： %.2f" % (t_stop - t_start))    # 执行时间： 25.14
