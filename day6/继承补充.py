#Authon Ivor
class F1(object):
    def a1(self):
        print("F1a1")

class F2(F1):
    def a1(self):
        self.a2()
        print("F2a1")
    def a2(self):
        print("F2a2")

class F3(F2):

    def a2(self):
        print("F3a2")

#优先调取obj自身的方法
obj = F3()
obj.a1()