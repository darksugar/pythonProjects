#Authon Ivor
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import select,add,delete,update

def run():
    menu = u'''
         ------- 模拟SQL ---------
        \033[32;1m 1.  查询
        2.  创建
        3.  删除
        4.  修改
        5.  退出
        \033[0m'''
    menu_dic = {
        "1":select.select,
        "2":add.add,
        "3":delete.delete,
        "4":update.update,
        "5":exit
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print(user_option)
            menu_dic[user_option]()
        else:
            print("\033[31;1mOption does not exist!\033[0m")