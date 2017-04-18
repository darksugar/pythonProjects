#Author:Ivor
from multiprocessing import Process,Queue
import os
# threading.queue.Queue()
def run(q):
    q.put("---in the Child process---")
    print("parent_pid:",os.getppid())
    print("current_pid:",os.getpid())
    print("------------------")


if __name__ == '__main__':
    q = Queue()
    print("---main process---")
    print("parent_pid:",os.getppid())
    print("current_pid:",os.getpid())
    print("------------------")
    p = Process(target=run,args=(q,))
    p.start()
    print(q.get())
    p.join()

