#Authon Ivor
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core.basic import School,Course,Classes,Teacher,Student
import pickle

def load():
    if os.path.isfile("backup.txt"):
        with open("backup.txt","rb") as f:
            data = pickle.load(f)
    else:#初始化数据
        #创建学校
        school_list = []
        school_bj = School("OldBoy", "北京")
        school_sh = School("NewBoy", "上海")
        school_list.append(school_bj)
        school_list.append(school_sh)
        # 创建课程
        course_list = []
        course_linux = Course(school_bj, "Linux", "8month", "9999")
        course_python = Course(school_bj, "Python", "5month", "19999")
        course_go = Course(school_sh, "Go", "3month", "6666")
        course_list.append(course_linux)
        course_list.append(course_python)
        course_list.append(course_go)
        # 创建班级
        classes_list = []
        classes_18 = Classes(school_bj, "18班")
        classes_21 = Classes(school_sh, "21班")
        classes_list.append(classes_18)
        classes_list.append(classes_21)
        classes_18.add_course(course_python)
        classes_21.add_course(course_go)
        # 创建老师
        teacher_list = []
        teacher1 = Teacher("张老师", "32", school_bj, classes_18)  # 北京
        teacher2 = Teacher("李老师", "31", school_bj, classes_18)  # 北京
        teacher3 = Teacher("王老师", "30", school_sh, classes_21)  # 上海
        teacher_list.append(teacher1)
        teacher_list.append(teacher2)
        teacher_list.append(teacher3)
        # 创建学生
        student_list = []
        student1 = Student("小明", "18", school_bj, classes_18)  # 北京
        student2 = Student("小强", "18", school_bj, classes_18)  # 北京
        student3 = Student("小花", "18", school_sh, classes_21)  # 上海
        student_list.append(student1)
        student_list.append(student2)
        student_list.append(student3)
        student1.classes.stu_list.append(student1)
        student2.classes.stu_list.append(student2)
        student3.classes.stu_list.append(student3)
        data = {
            "school_list":school_list,
            "course_list":course_list,
            "classes_list":classes_list,
            "teacher_list":teacher_list,
            "student_list":student_list
        }
    return data