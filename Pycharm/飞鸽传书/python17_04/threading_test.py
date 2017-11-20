import threading
import time


def dance(num):
    for i in range(num):
        print("dance")
        time.sleep(0.01)


def sing(num):
    for i in range(num):
        print("sing")
        time.sleep(0.01)

def main():
    sing_thread = threading.Thread(target=sing, args=(5,))
    dance_thread = threading.Thread(target=dance, args=(6,))
    sing_thread.setDaemon(True)
    sing_thread.start()
    dance_thread.start()

main()