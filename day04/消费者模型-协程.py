#Authon Ivor
import time

def consumer(name):
    print("我准备吃包子啦！")
    while True:
        baozi = yield
        print("包子(%s)来了,(%s)吃掉了！" % (baozi,name))


def producer():
    c1 = consumer("A")
    c2 = consumer("B")
    c1.__next__()
    c2.__next__()
    print("我开始做包子了！")
    for i in range(10):
        print("做好了一个！")
        time.sleep(1)
        c1.send(i)
        c2.send(i)

producer()