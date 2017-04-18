#Authon Ivor
import os
#类方法，只能访问类变量，不能访问实例变量
class School(object):
    db_path = '/home/db/school/'

    @classmethod
    def get_obj(cls):
        import pickle
        data = pickle.load(open(cls.db_path,'rb'))

        return data