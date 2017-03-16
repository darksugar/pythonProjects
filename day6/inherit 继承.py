#Authon Ivor

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sex = "F"
    def talk(self):
        print("I'm a person!")

class BlackPerson(Person):
    #先继承，再重构
    def __init__(self,name,age,strength):
        Person.__init__(self,name,age)
        self.strength = strength
    #重构函数
    def talk(self):
        print("I am BlackMan!")
class WhitePerson(Person):
    pass

B = BlackPerson("YoYo",22,"Strong")
B.talk()
