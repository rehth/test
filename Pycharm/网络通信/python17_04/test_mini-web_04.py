"""
关卡一

    练习题:

    1.简述你对闭包的理解？
    闭包：内置函数及自由变量(环境变量)的统称

    2.描述闭包的优点与注意点？
    提高了代码的可复用性

    3.什么是装饰器？

    4.简述装饰器的功能？

    5.一个函数同时使用两个装饰器，执行顺序是怎么执行的？

写出下面程序的结果，并解释

flist = []
for i in range(3):
     def foo(x):
        print x + i
    list.append(foo)
for f in flist:
     f(2)


"""


# def adorn(i):
#     def inner(x):
#         print(x + i)
#     return inner
#
# for num in range(3):
#     add = adorn(num)
#     add(2)

flist = []
for i in range(3):  # [0, 1, 2]
    def foo(x):         # def foo(x):print(x+0)
        print(x+i)
        print(foo)
        flist.append(foo)
    # 函数未被调用
    print(flist)
for f in flist:
    f(2)


