"""****************************************************
**********Python multiprocessing******************
****************************************************

#multiprocessing => running tasks in parallel on different cpu cores, bypasses GIL used for threading
multiprocessing is better for cpu bound tasks (heavy cpu usage)
multithreading => is better for IO bound tasks (waiting around)"""

from _multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a =Process(target=counter, args=(100000000,))
    a.start()
    a.join()

if __name__ == '__main__':
    main()

    class Process(object):
        pass


def cpu_count():
    return None