# A semaphore is a concurrency primitive that allows a limit on the number of threads that can acquire a lock protecting a critical section.
#limiting concurrent connections to a server, concurrent hard drive operations, calculations happening concurrently

from threading import Semaphore

semaphore=Semaphore()

semaphore.acquire(blocking=False)
semaphore.acquire(timeout=10)
semaphore.release()

