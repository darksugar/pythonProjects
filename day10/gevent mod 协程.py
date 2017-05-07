#Authon Ivor
import gevent

#自动切换
def run():
    print(1)
    gevent.sleep(2)
    print(6)
def run2():
    print(2)
    gevent.sleep(1)
    print(5)
def run3():
    print(3)
    gevent.sleep(0)
    print(4)
gevent.joinall([gevent.spawn(run),gevent.spawn(run2),gevent.spawn(run3)])

#手动切换
from greenlet import greenlet

def run1():
    print(1)
    gr2.switch()
    print(3)
    gr2.switch()
    print(5)
    gr2.switch()
def run2():
    print(2)
    gr1.switch()
    print(4)
    gr1.switch()
    print(6)
gr1 = greenlet(run1)
gr2 = greenlet(run2)
gr1.switch()
