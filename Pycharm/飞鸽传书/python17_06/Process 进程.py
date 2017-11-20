import multiprocessing
import time
import os


def work():
    while True:
        print("work")
        time.sleep(1)

p1 = multiprocessing.Process(target=work)
p1.daemon = True

p1.start()

p1.join(5)

print(p1.is_alive())

print(p1.pid, os.getpid(), multiprocessing.cpu_count())

p1.terminate()

print(p1.is_alive())

print("over")

