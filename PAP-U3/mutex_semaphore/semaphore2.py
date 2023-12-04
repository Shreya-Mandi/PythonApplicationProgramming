from time import sleep
from random import random
from threading import Thread
from threading import Semaphore

def task(semaphore, identifier, value):
    with semaphore:
        print(f'the thread {identifier} has put semaphore for {value}')
        sleep(value)

if __name__=='__main__':
    semaphore=Semaphore(2)

    for i in range(10):
        thread=Thread(target=task, args=(semaphore,i,random())).start()

