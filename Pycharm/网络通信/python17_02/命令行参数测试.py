# 测试命令行参数
import sys
print(sys.argv)
print(len(sys.argv))


try:
    f = open("dsss", "rb")
except Exception as e:
    print(type(e))
    print(e)
