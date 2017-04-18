#Authon Ivor
class dog(object):
    #公有变量，如果有私有变量，优先调用私有，如果没有调用公有
    age = 8

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def bark(self):
        print("%s is barking,wang.wang..wang..." % self.name)
        self.type = "wang.wang..wang.."

    def get_type(self):
        print("{0} 's type is {1}".format(self.name,self.type))

d = dog("lovely","Teddy")
d2 = dog("diudiu","田园犬")

d.bark()
d2.get_type()
d.age = 10
print(d.age)
print(d2.age)
dog.age = 9
print(d.age)
print(d2.age)

def bark2():
    print("bark")
d.bark = bark2
d.bark()