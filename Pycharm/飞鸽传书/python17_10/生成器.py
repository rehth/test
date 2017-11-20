# 生成器是一种特殊的迭代器
# 简单来说：只要在 def 中有 yield 关键字的 就称为 生成器
import time


def fibonacci(i):
    a, b = 0, 1
    current = 0
    while current < i:
        num = a
        a, b = b, a+b
        current += 1
        # 暂停执行，如果有返回值先返回　等待启动
        # 在函数中出现　yield 表示生成器
        yield num
        time.sleep(1)

# 返回一个迭代器(生成器)　有__next__()方法
# 生成器是一种特殊的迭代器
f = fibonacci(10)

while True:
    try:
        print(next(f))
        # print(f.send(None))
        # print(f.send())
    except StopIteration:
        break


# f = fibonacci(10)
#
# print(next(f))
# print(next(f))


