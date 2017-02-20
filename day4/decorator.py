#Authon Ivor
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("The program cost %s" % (stop_time-start_time))
    return deco

@timer
def test1():
    time.sleep(1.5)
    print("I'm in the test1 !")
@timer
def test2(name,age):
    time.sleep(0.5)
    print("%s's age is %s" % (name,age))

test1()
test2("Ivor",25)