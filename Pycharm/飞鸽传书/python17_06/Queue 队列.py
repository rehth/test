import multiprocessing


def write(q):
    l = list()
    for i in range(1, 10, 2):
        l.append(i)
    q.put(l)


def read(q):
    print(q.get())

if __name__ == '__main__':
    q = multiprocessing.Queue()

    w_p = multiprocessing.Process(target=write, args=(q,))
    r_q = multiprocessing.Process(target=read, args=(q, ))
    w_p.start()
    w_p.join()
    r_q.start()
