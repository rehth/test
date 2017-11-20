import time


class Adorn(object):
    def __init__(self, func):
        print("初始化开始")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("%s 开始执行" % self.func.__name__)
        return self.func() + " world"


@Adorn
def hello():
    return "hello"

time.sleep(3)

print(hello())
