# 即　重写type
# python3 中类对象有一个属性
# metaclass=type 默认为type
import multiprocessing
# multiprocessing.Manager().Queue()


def change_type(name, parents, attr):
    print(name, parents, attr)
    for key, value in attr.items():
        if not key.startswith('__'):
            # print(key, value)
            attr[key.upper()] = attr.pop(key)

    return type(name, parents, attr)


class T(object, metaclass=change_type):
    a = 12
    bar = True

    def __init__(self):
        self.b = 21

    @classmethod
    def class_test(cls):
        cls.a += 1

    @staticmethod
    def static():
        print('static')

# 查看类结果
help(T)
t = T()
# print(t.a)      # 'T' object has no attribute 'a'
print(t.A)
print(hasattr(T, 'STATIC'))     # True



