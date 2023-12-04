# mutex prevents reace condition for 2 threads
# locks protect shared variables, resources
# mutual exclusion- only one thread can execute on the given code at once
# threading.Lock()
# threading.RLock() reentrant lock


from threading import Lock
lock=Lock()
# lock.acquire()
lock.acquire(timeout=10)
# lock.release()