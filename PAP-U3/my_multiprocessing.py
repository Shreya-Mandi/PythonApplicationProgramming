# Multiprocessing involves executing multiple processes simultaneously, enabling efficient utilization of multiple CPU cores. Unlike threads, processes have separate memory spaces.

from multiprocessing import Process

def  func(numbers):
    for i in numbers:
        print(i*i)

if __name__=='__main__':
    num=[1,2,3]
    process=Process(target=func, args=(num))

    process.start()
    process.join()