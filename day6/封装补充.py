#Authon Ivor

class F1(object):
    def __init__(self,arg):
        self.a = arg

class F2(F1):
    def __init__(self,arg):
        self.b = arg

class F3(F2):
    def __init__(self,arg):
        self.c = arg

o1 = F1("Alex")
o2 = F2(o1)
o3 = F3(o2)

#######通过o3调取到Alex#######
print(o3.c.b.a)