#Authon Ivor
import threading
import time

def run(n):
    semaphore.acquire()
    print(n)
    time.sleep(1)
    semaphore.release()

neq = threading.Semaphore(5)
semaphore = threading.BoundedSemaphore(5)
for i in range(10):
    t = threading.Thread(target=run,args=(i,))
    t.start()


