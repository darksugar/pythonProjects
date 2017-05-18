#Authon Ivor
from core import db_handler

class Class_Manage(object):
    def __init__(self,user_data):
        menu = '''
        1.  添加班级
        2.  添加学员到班级
        '''
        menu_dic = {
            '1':self.add_class,
            '2':self.add_student2class,
        }
        print(menu)
        choice = input("[1/2]>>>:")
        if choice.isdigit():
            menu_dic.get(choice)(user_data)

    def db_conn(self):
        db_api = db_handler.db_handler()
        return db_api

    def add_class(self,user_data):
        class_name = input("Input the class name:")
        db_api = self.db_conn()
        res = db_api.add_class(class_name,user_data["account_data"].tea_id)
        if res:
            print("Class %s added..." % class_name)

    def add_student2class(self,user_data):
        class_name = input("Input the class name:")
        qq_num = input("Input the qq of student:")
        db_api = self.db_conn()
        res = db_api.add_student2class(class_name,qq_num)
        if res:
            print("Student added...")

class Class_record_Manage(object):
    def __init__(self, user_data):
        menu = '''
        1.  添加上课记录
        '''
        menu_dic = {
            '1': self.add_class_record,
        }
        print(menu)
        choice = input("[1]>>>:")
        if choice.isdigit():
            menu_dic.get(choice)(user_data)

    def db_conn(self):
        db_api = db_handler.db_handler()
        return db_api

    def add_class_record(self,user_data):
        class_name = input("Input the class name:")
        lesson_name = input("Input the lesson name:")
        db_api = self.db_conn()
        res = db_api.add_class_record(class_name,lesson_name,user_data["account_data"].tea_id)
        if res:
            print("Record added...")

class Score_Manage(object):
    def __init__(self,user_data):
        pass