#Authon Ivor
from multiprocessing import Process,Pool
import time,os
def run(n):
    print("Process %s is running.." % n)
    time.sleep(1)
    return os.getpid()

def bar(arg):
    print("exec done---",arg)

result = []
if __name__ == '__main__':
    pool = Pool(processes=2)
    for n in range(10):
        result.append(pool.apply_async(func=run,args=(n,),callback=bar))
    for res in result:
        print("res---",res.get())
    pool.close()
    pool.join()