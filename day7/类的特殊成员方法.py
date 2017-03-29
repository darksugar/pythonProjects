#Authon Ivor

class Foo(object):
    #定义类的原类
    __metaclass__ = type

    #类中所有的方法和属性
    #__dict__

    #构造函数，创建对象时调用
    def __init__(self,name,age):
        super(Foo,self).__init__()
        self.age = age
        self.name = name
    #定义对象的调用方式
    def __call__(self, *args, **kwargs):
        print("I'm the __call__ .")
    #打印对象时，使用这个函数的返回值
    def __str__(self):
        return "%s" % self.name

    def __new__(cls, *args, **kwargs):
        print("I'm the __new__!")
        return object.__new__(cls)
    def __del__(self):
        pass

f = Foo("ivor",27)
f()

#类的第二种定义方法，一切皆对象，类也是对象，源于type
def func(self):
    print("hello %s"%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age
Foo = type('Foo',(object,),{'func':func,'__init__':__init__})
f = Foo("jack",22)
f.func()
