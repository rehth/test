import multiprocessing
import threading
import queue
import os


def read_file(file_name, file_path, que):
    old_file = open(file_path + "/" + file_name, "rb")
    while True:
        info = old_file.readline()
        if len(info) == 0:
            break
        # print(info)
        que.put(info)
    old_file.close()


def write_file(file_name, copy_path, que):
    new_file = open(copy_path + "/" + file_name, "wb")
    while True:
        info = que.get()
        # print(info)
        new_file.write(info)
        if que.empty():
            print(que.qsize)
            break
    new_file.close()


def file_copy(file_name, file_path, copy_path):
    # 线程间数据的通信
    que = queue.Queue()
    r_t = threading.Thread(target=read_file, args=(file_name, file_path, que))
    w_t = threading.Thread(target=write_file, args=(file_name, copy_path, que))
    r_t.start()
    # r_t.join(0.01)
    w_t.start()


def dir_copy():
    file_path = input("路径")
    new_path = input("存储路径")
    copy_path = new_path + file_path[file_path.rfind("/"):] + "-附件"
    os.mkdir(copy_path)
    ls_file = [i for i in os.listdir(file_path) if i.endswith(".py")]
    pool = multiprocessing.Pool(8)
    for i in ls_file:
        pool.apply_async(file_copy, (i, file_path, copy_path))
    pool.close()
    pool.join()
    print("成功")
# 进程池中进程的通信
multiprocessing.Manager().Queue()

dir_copy()
