#Authon Ivor
import shelve

d = shelve.open('shelve_test')  # 打开一个文件

class Test(object):
    def __init__(self, n):
        self.n = n

t1 = Test("123")
t2 = Test("ivor")
name = ["alex","ivor"]

d["name"] = name
d["t1"] = t1
d["t2"] = t2

d.close()