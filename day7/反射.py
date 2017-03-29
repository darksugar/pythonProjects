#Authon Ivor
def bark(self):
    print("%s is yelling!" )


class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating!" % self.name)

d = Dog("WangWang")
choice = input(">>>:").strip()

print(hasattr(d,choice))
if hasattr(d,choice):
    func = getattr(d,choice)
    setattr(d,choice,'hanghang')
    print(func)
    d.eat()

else:
    pass
    # setattr(d,choice,bark)
    # #choice = aaa
    # d.aaa(d)


# if choice == 'eat':
#     d.eat()