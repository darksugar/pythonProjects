#Authon Ivor
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from db import db

def delete():
    staff_table = db.load_db()
    for i in staff_table:
        i = " ".join(i)
        print(i)
    delete_id = input("please input the staff_id that you want to delete:")
    if int(delete_id) <= int(staff_table[len(staff_table)-1][0]) and int(delete_id) >= 0:
        for index,i in enumerate(staff_table):
            if delete_id == i[0]:
                del staff_table[index]
        db.delete_staff(staff_table)
        print("\033[31;1mThe new staff is delete!!!\033[0m")
    else:
        print("\033[31;1mWrong Staff_id!\033[0m")