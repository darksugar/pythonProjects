#Authon Ivor
from core import db_handler

class Hand_work:
    def __init__(self, user_data):
        db_api = self.db_conn()
        class_id_list= db_api.get_class_by_stu_id(user_data["account_data"].stu_id)
        class_id = input("Input class id:")
        if int(class_id) in class_id_list:
            db_api.get_lesson_by_class_id(class_id,user_data["account_data"].stu_id)
            lesson_name = input("Input lesson name:")
            res = db_api.hand_in_homework(user_data["account_data"].stu_id,class_id,lesson_name)
            if res:
                print("Hand in success...")
        else:
            print("Wrong class id...")

    def db_conn(self):
        db_api = db_handler.db_handler()
        return db_api

class Get_score(object):
    pass

class Get_ranking(object):
    pass