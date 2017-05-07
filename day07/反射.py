#Authon Ivor
def bark(self):
    print("%s   is yelling!" % self.name )


class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating!" % self.name)

d= Dog("Wangwang")
choice = input(">>>:")

if hasattr(d,choice):
    a = setattr(d,choice,"bbb")
    print("done")
    print(d.name)


# if hasattr(d,choice):
#     func = getattr(d,choice)
#     func()
# else:
#     setattr(d,choice,bark) #d.choice = bark
#     func = getattr(d,choice)
#     func(d)