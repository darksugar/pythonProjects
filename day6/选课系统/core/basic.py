#Authon Ivor
import pickle

class School(object):
    def __init__(self,name,city):
        self.name = name
        self.city = city

class Course(object):
    def __init__(self,school,name,outline,price):
        self.school = school
        self.name = name
        self.cycle = outline
        self.price = price

class Classes(object):
    def __init__(self,school,name):
        self.school = school
        self.name = name
    def add_course(self,course,teacher):
        self.course = {}
        self.course[course] = teacher

class People(object):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school =school

class Teacher(People):
    def __init__(self, name,age,school):
        super(Teacher, self).__init__(name,age,school)

class Student(People):
    def __init__(self, name,age,school,classes):
        super(Student, self).__init__(name,age,school)
        self.classes = classes

#创建学校
school_bj = School("OldBoy","北京")
school_sh = School("NewBoy","上海")


#创建课程,关联学校
course_linux = Course(school_bj,"Linux","8month","9999")
course_python = Course(school_bj,"Python","5month","19999")
course_go = Course(school_sh,"Go","3month","6666")

#创建班级
classes_18 = Classes(school_bj,"18班")
classes_21 = Classes(school_sh,"21班")

#创建老师
teacher1 = Teacher("张老师","32",school_bj)    #北京
teacher2 = Teacher("李老师","31",school_bj)    #北京
teacher3 = Teacher("王老师","30",school_sh)    #上海

#创建学员
student1 = Student("小明","18",school_bj,classes_18)     #北京
student2 = Student("小强","18",school_bj,classes_18)     #北京
student3 = Student("小花","18",school_sh,classes_21)     #上海

#分配老师班级、课程
classes_18.add_course(course_linux,teacher1)
classes_18.add_course(course_python,teacher2)
classes_21.add_course(course_go,teacher3)

with open("backup.txt","w") as f:
    pickle.dump(f,info)