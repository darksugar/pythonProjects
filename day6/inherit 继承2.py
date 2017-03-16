#Authon Ivor
class SchoolMember(object):
    '''基类'''
    member = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex
        self.enroll()

    def enroll(self):
        print("[%s] has just enrolled ." % self.name)
        SchoolMember.member += 1

    def tell(self):
        print("info %s".center(20,"-") % self.name )
        for k,v in self.__dict__.items():
            print("%s:%s" % (k,v))
        print("info %s".center(20,"-") % self.name )
    #析构函数
    def __del__(self):
        print("\033[31;1mmember [%s] is dead!\033[0m" %self.name)
        SchoolMember.member -= 1

class Teacher(SchoolMember):
    '''讲师类'''
    def __init__(self,name,age,sex,salary,tuition):
        # 新式类写法
        # super(Teacher,self).__init__(name,age,sex)
        # 经典类写法
        SchoolMember.__init__(self,name,age,sex)
        self.salary = salary
        self.tuition = tuition

class Student(SchoolMember):
    '''学生类'''
    def __init__(self,name,age,sex,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.amount = 0
        self.tuition = tuition

s1 = Student("Hebe",18,"F","Python")
t1 = Teacher("Yoyo",22,"F",10000,"Python")
t1.tell()
print(SchoolMember.member)
del s1
print(SchoolMember.member)
