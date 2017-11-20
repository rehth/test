"""
练习题：
    什么线程？

    多线程用来做什么？

    threading模块中的Thread怎样创建一个子线程？
    threading.Thread(target=name)

    父线程和子线程的执行顺序确定么？

    编写代码实现“飞鸽传书”项目中同时收发数据


    使用threading模块中的Thread，创建2个子线程，线程1中每秒钟打印1个A，线程2中每2秒钟打印1个B
import threading
import time
def print_a():
    while True:
        print("A")
        time.sleep(1)
def print_b():
    while True:
        print("B")
        time.sleep(2)
a_thread = threading.Thread(target=print_a)
b_thread = threading.Thread(target=print_b)
a_thread.start()
b_thread.start()

    创建2个子线程，线程1、2同时对全局变量num各加100万次操作（num初始值为0），每次加1，最后执行完成打印结果

    请解释线程数大于cpu核数时，多任务是怎样实现的

    请解释并行、并发这2个词语


    在桌面上编写一个py文件，完成以下功能要求
    用多任务（多线程）的方式完成Test文件夹中的所有文件的复制
    新的文件夹的名字为“Test-附件”
    在复制文件的过程中，实时显示复制的进度
"""
import os
import threading


def file_copy(num, file_path):
    file_list = os.listdir(file_path)
    # 不能使用 len()-1 ,range 是取不到右边的数的
    for i in range(num, len(file_list), 2):
        old_file = file_path + "/" + file_list[i]
        new_file = file_path + "-附件" + "/" + file_list[i]
        """
            old_f = open(old_file, "rb", encoding="utf-8")
            ValueError: binary mode doesn't take an encoding argument
            使用 "b" 模式不需要进行编码操作
        """
        old_f = open(old_file, "rb")
        new_f = open(new_file, "wb")
        while True:
            info = old_f.readline(1024)
            if len(info) == 0:
                break
            new_f.write(info)
        new_f.close()
        old_f.close()


def dir_copy():
    """
        完成一个文件夹的复制
        但文件夹中仅能有文件,不能对文件夹的产生作用
        idea：判断文件还是文件夹 如果是文件夹递归调自己
    """
    file_path = input("文件的绝对路径：")
    if os.path.exists(file_path):
        new_path = file_path + "-附件"
        os.mkdir(new_path)
        # file_copy(num)
        copy0_thread = threading.Thread(target=file_copy, args=(0, file_path))
        copy1_thread = threading.Thread(target=file_copy, args=(1, file_path))
        copy0_thread.start()
        copy1_thread.start()
        while threading.active_count() != 1:
            if len(threading.enumerate()) == 1:
                break
        print("[INFO]:文件夹复制完成")
    else:
        print("[INFO]:该目录不存在")


if __name__ == '__main__':
    dir_copy()
