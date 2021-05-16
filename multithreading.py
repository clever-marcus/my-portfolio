"""A thread -> a flow of execution. Like a separate order of instructions.
    However each thread takes a turn running to achieve concurrency
    GIL = (global interpreter lock.)
    allows only one thread to hold the control of the Python interpreter at any one time
    
cpu bound => program/task spends most of it's time waiting for internal events (CPU intensive)
            use multiprocessing
            
io bound => program/task spends most of it's time waiting for external events (user input, web scraping)
            use multithreading"""


import threading
import time

def sleep():
    time.sleep(5)
    print("wake up! Time to go!!")

def breakfast():
    time.sleep(9)
    print("Time to study!! Put aside breakfast!")
def study():
    time.sleep(10)
    print("Take a nap!")

x = threading.Thread(target=sleep, args=())
x.start()

y = threading.Thread(target=breakfast, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

#sleep()
#breakfast()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())