# In computer programming, threads are sequences of instructions that can be executed independently by a CPU. They are a fundamental part of concurrent programming, allowing programs to do multiple things at once.
#
# A race condition occurs when two or more threads are trying to access shared data or resources, and the outcome of their execution depends on the order in which they are scheduled by the operating system. This can lead to unpredictable behavior and bugs in your program.

import threading

def f1():
    print("Function 1")

def f2():
    print("Function 2")

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()