# Multithreading is a technique to execute multiple threads concurrently within a process, allowing for better performance by utilizing multiple CPUs or CPU cores.

import threading

def do():
    for i in range(10):
        print(i)


thread=threading.Thread(target=do)

thread.start()
