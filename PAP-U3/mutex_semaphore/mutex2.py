from time import sleep
from random import random
from threading import Thread
from threading import Lock


def task(lock, identifier, value):
    with lock:
        print(f'thread{identifier} locked, sleeping for{value}')
        sleep(value)


lock = Lock()

for i in range(10):
    Thread(target=task, args=(lock, i, random())).start()
