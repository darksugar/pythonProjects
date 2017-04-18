#Authon Ivor
import os
DB_DIR = os.path.dirname(os.path.abspath(__file__))
# print(DB_DIR)
db_file = "%s\employee.txt" % DB_DIR

#将文件中的数据读入内存，创建一个列表
def load_db():
    staff_table = []
    with open(db_file,"r") as f:
        for i in f:
            i = i.strip().split(",")
            staff_table.append(i)
    # print(staff_table)
    return staff_table

def add_new_staff(employee):
    e = ",".join(employee)
    with open(db_file,"a") as f:
        f.write(e)
        f.write("\n")

def delete_staff(new_staff_table):
    with open(db_file, "w") as f:
        for employee in new_staff_table:
            e = ",".join(employee)
            f.write(e)
            f.write("\n")

def update_staff(new_staff_table):
    with open(db_file, "w") as f:
        for employee in new_staff_table:
            e = ",".join(employee)
            f.write(e)
            f.write("\n")