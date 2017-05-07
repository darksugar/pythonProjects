#Authon Ivor
import threading
import queue

def producer():
    for i in range(10):
        q.put("骨头 %s" % i)
    print("开始等待所有的骨头被取走...")
    q.join()
    print("所有的骨头被取完了...")

def consumer(n):
    while q.qsize() > 0:
        print("%s 取到" % n, q.get())
        q.task_done()  # 告知这个任务执行完了

q = queue.Queue()
p = threading.Thread(target=producer)
p.start()
c1 = consumer("李闯")

import time,random
import queue,threading


def Producer(name):
  count = 0
  while count <20:
    time.sleep(random.randrange(3))
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1

def Consumer(name):
  count = 0
  while count <20:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    else:
        print("-----no baozi anymore----")
    count +=1

q = queue.Queue()
p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
p1.start()
c1.start()