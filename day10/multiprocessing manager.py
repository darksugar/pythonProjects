#Author:Ivor
from multiprocessing import Process,Manager
import os
def run(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)

pro_list = []
if __name__ == '__main__':
    manager = Manager()
    d = manager.dict()
    l = manager.list()
    for i in range(10):
        p = Process(target=run,args=(d,l))
        pro_list.append(p)
        p.start()
    for i in pro_list:
        i.join()
    print(d)
    print(l)
