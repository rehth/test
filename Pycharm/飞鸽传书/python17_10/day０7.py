"""
test1:
    定义一个列表，里面的元素为1~10000
    mylist = [i for i in range(1, 10001)]
    如果列表中包含了很多个元素，会有什么问题吗？
    什么是列表生成式
    使用列表生成式完成一个列表，其中的元素为1~100之间的偶数
    list1 = [i for i in range(1, 101) if i % 2 == 0]
    生成器是什么
    一种特殊的迭代器　在函数(def)中包含关键字　yield 即为生成器

    创建一个生成器的方式有哪些？
    1.g = (i for i in range(5))
    2.在函数(def)中包含关键字　yield

    斐波那契数列是什么？

    将一个函数改为生成器需要什么？
    yield

    yield的作用是什么？
    暂停执行，并返回

    程序执行到yield时会怎样？

    如果变量A是一个生成器，那么怎样生成一个数据？

    当用next取到最后一个数据后，如果再用next会怎样？
    raise Stop...  抛出异常

    send和next有什么区别？
    yield 的唤醒方式
    next:启动　next(f)相当于f.send(None)
    send:启动　可传递参数

    什么是可迭代对象

    列举2个可迭代对象
    str list tuple set dict range

    什么是迭代器

    怎样获取可迭代对象中的迭代器
    iter(items)

"""
# mylist = [i for i in range(1, 10001)]
# print(mylist)
# list1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list1)

"""
test2:
    将 a = [x for x in range(100)]改为生成器
    a = (x for x in range(100))
    使用yield创建一个生成器，并完成上题目中效果，即0~99
def yi_num():
    for num in range(100):
        yield num
yi = yi_num()
while True:
    try:
        print(yi.send(None))
    except StopIteration:
        break

    使用iter将[11,22,33,44]变为迭代器
    my_iterator = iter([11,22,33,44])

    使用gevent、urllib模块，完成5个视频文件的下载


import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()


def download_video(video_url, video_name):
    response = urllib.request.urlopen(video_url)
    with open(video_name, "wb") as file:
        while True:
            video_data = response.read(10240)
            if not video_data:
                break
            file.write(video_data)
url1 = 1
url2 = 2
url3 = 3
url4 = 4
url5 = 5
gevent.joinall([gevent.spawn(download_video, url1, "1.mp4"),
                gevent.spawn(download_video, url2, "2.mp4"),
                gevent.spawn(download_video, url3, "3.mp4"),
                gevent.spawn(download_video, url4, "4.mp4"),
                gevent.spawn(download_video, url5, "5.mp4")])
"""
"""
test:
    定义一个迭代器类，完成斐波那契数列的基本功能

    使用yield创建一个生成器，完成斐波那契数列的基本功能

    通过浏览器的检查某个网站的所有图片url，并使用协程完成这些图片的下载
"""


class Fibonacci(object):
    def __init__(self, num):
        self.len = num
        self.current = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        # if/while 都可以，这里起判断作用
        if self.current < self.len:
            result = self.a
            self.a, self.b = self.b, self.a+self.b
            self.current += 1
            return result   # return 作用是　结束并返回
        else:
            raise StopIteration

fib = Fibonacci(10)

# print(list(fib))

while True:
    try:
        print(next(fib))
    except StopIteration:
        break


def fibonacci(num):
    a, b = 0, 1
    current = 0
    while current < num:
        result = a
        a, b = b, a+b
        current += 1
        yield result

fi = fibonacci(10)
# print(tuple(fi))
while True:
    try:
        print(fi.send(None))
    except StopIteration:
        break


import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def down_image(image_url, image_name):
    response = urllib.request.urlopen(image_url)
    image_data = response.read()
    with open(image_name, "wb") as file:
        file.write(image_data)


def main():
    url1 = 1
    url2 = 2
    gevent.joinall([gevent.spawn(down_image, url1, "1.jpg"),
                    gevent.spawn(down_image, url2, "2.jpg")])
if __name__ == '__main__':
    main()