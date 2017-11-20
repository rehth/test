import time


def factory(flag=None):
    def func(fun):
        def inner(*args, **kwargs):
            if flag:
                print("%s begin in %s" % (fun.__name__, time.ctime()))
                result = fun(*args, **kwargs)
                print("%s end in %s" % (fun.__name__, time.ctime()))
                return result
            else:
                return fun(*args, **kwargs)
        return inner
    return func


@factory(1)
def hello():
    return "hello"

print(hello())