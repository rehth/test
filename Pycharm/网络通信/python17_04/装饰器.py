import time


def test(fun):
    # 开放封闭原则,适用于面向对象开发，但是也适用于函数式编程
    # 规定已经实现的功能代码不允许被修改，但可以被扩展
    def inner(*args, **kwargs):
        print("%s in inner @ %s" % (fun.__name__, time.ctime()))
        return fun(*args, **kwargs)
    return inner


@test   # @函数名 是python的一种语法糖 === func = test(func)
def func(a, b):
    return a*b+a

print(func(2, 3))


def makebold(fun):
    def inner():
        return "<b>" + fun() + "</b>"
    return inner


@makebold
def hello():
    return "hello world"

print(hello())