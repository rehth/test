# 斐波那契数列
# 迭代器的应用
# a, b = b, a+b


class Fibonacci(object):
    def __init__(self, num):
        self.num = num
        self.current = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.num:
            result = self.a
            self.a, self.b = self.b, self.a+self.b
            self.current += 1
            return result
        else:
            raise StopIteration

fb = Fibonacci(10)


# while True:
#     try:
#         print(next(fb))
#     except StopIteration:
#         break

# for i in fb:
#     print(i)

# fb_list = list(fb)
# print(fb_list)

fb_tuple = tuple(fb)
print(fb_tuple)
