<<<<<<< HEAD
#Author:Ivor
from multiprocessing import Process,Pool,freeze_support
import os,time

def run(i):
    time.sleep(1)
    print("child process",os.getpid())

def back(arg):
    print("exec done--->",arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(processes=2)
    print("main process:",os.getpid())
    for i in range(10):
        # pool.apply(func=run,)
        # pool.apply_async(func=run,)
        pool.apply_async(func=run,args=(i,),callback=back)
=======
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
>>>>>>> 7ca1d9f6b599ea10a98d9ed022f6285f3688051d
    pool.close()
    pool.join()