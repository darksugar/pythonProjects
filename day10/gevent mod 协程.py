#Authon Ivor
import gevent

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