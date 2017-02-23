#Authon Ivor
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting
from db import db

def update():
    tip = """
    Please input your sql
    For example:
    update staff_table SET dept = Market where dept = IT
    """
    staff_table = db.load_db()
    sql = input(tip)
    sql = sql.strip().split("where")
    update = sql[0].strip().split(" ")
    where = sql[1].strip().split(" ")
    # print(staff_table)
    # print(update,where)
    new_staff_table = []
    for employee in staff_table:
        if setting.row.get(where[0]):
            # data = employee[setting.row[where[0]]] + where[1] + where[2]
            # if eval(data)
                if employee[setting.row[where[0]]] == where[2]:
                    employee[setting.row[update[-3]]] = update[-1]
        new_staff_table.append(employee)
    db.update_staff(new_staff_table)
    print("\033[32;1mStaff_table update sucdessed!\033[0m")
