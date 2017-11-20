from collections import Iterable, Iterator

# 判断是否为可迭代序列
result = isinstance([12, 13, 14], Iterable)
print(result)

# 自定义可迭代对象　有__iter__()方法
# 仿 list


class MyList:
    def __init__(self):
        self.list = list()

    def __iter__(self):
        """返回一个迭代器"""
        my_iterator = MyIterator(self.list)
        return my_iterator

    def add_items(self, num):
        self.list.append(num)


# 自定义迭代器　有__iter__()\__next__()方法
class MyIterator:
    def __init__(self, mylist):
        self.list = mylist
        self.current = 0

    def __iter__(self):
        # 自己就是迭代器　故返回自己
        return self

    def __next__(self):
        if self.current < len(self.list):
            self.current += 1
            return self.list[self.current-1]
        else:
            raise StopIteration


my_list = MyList()

# 判断是否为可迭代对象
print(isinstance(my_list, Iterable))

my_list.add_items(12)
my_list.add_items(11)
my_list.add_items(10)

# 获取迭代器　调用的是__iter__()方法
my_iter = iter(my_list)

# 判断是否为迭代器
print(isinstance(my_iter, Iterator))

print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
while True:
    try:
        # 调用的是__next__()方法
        print(next(my_iter))
    except StopIteration:
        print("遍历结束")
        break


