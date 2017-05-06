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
    pool.close()
    pool.join()