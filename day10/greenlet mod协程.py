#Authon
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
