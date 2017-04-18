#Authon Ivor
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from db import db

def add():
    staff_table = db.load_db()
    new_staff_phone = str(input("please input the phone of new staff:"))
    for employee in staff_table:
        if new_staff_phone in employee:
            print("The phone is exist!")
    new_staff_name = str(input("please input the name of new staff:"))
    new_staff_age = str(input("please input the age of new staff:"))
    new_staff_dept = str(input("please input the dept of new staff:"))
    new_staff_enroll_date = str(input("please input the enroll_date of new staff:"))
    new_staff_id = str(int(staff_table[len(staff_table)-1][0])+1)
    new_employee = [new_staff_id,new_staff_name,new_staff_age,new_staff_phone,new_staff_dept,new_staff_enroll_date]
    db.add_new_staff(new_employee)
    print("\033[32;1mThe new staff is added!\033[0m")