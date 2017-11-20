# 元类　type

# 使用　元类创建一个类


@classmethod
def class_test(cls):
    print('class_test')


@staticmethod
def static_test():
    print('static_test')


def self_test(self):
    print("self_test")

# type(名, (父类,), {属性, 方法}

TT = type("TT", (object,), {'class_attr': 'test', 'class_test': class_test, 'static_test': static_test,
                            'self_test': self_test})
help(TT)

# TT.class_test()    # class_test
# TT.static_test()    # static_test
# TT.self_test()    # 报错
tt = TT()
tt.class_test()
tt.static_test()
tt.self_test()
