import time


def test(a, b):
    def inner(x):
        # 使用关键字　nonlocal 对参数进行声明
        # 使其可以被修改
        # LEGB 原则
        print(inner.__closure__)
        nonlocal a
        a += 1
        print("a is %d" % a)
        print("in inner @ %s" % time.ctime())
        # 闭包使用的环境变量存储在闭包函数的属性 --- 元组对象__closure__属性中
        # 比如需要访问第0个环境变量的值时 __closure__[0].cell_contents
        print(inner)
        print(inner.__closure__)
        print(type(inner.__closure__))
        print(inner.__closure__[0].cell_contents)
        print(type(inner.__closure__[0]))   # <class 'cell'>
        return a*x + b
    return inner


t = test(3, 5)
print(t(4))

