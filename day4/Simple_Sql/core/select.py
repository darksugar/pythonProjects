#Authon Ivor
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import setting
from db import db

#查询
def select():
    tip = """
    Please input your sql
    For example:
    select name,age from staff_table where age > 30
    select * from staff_table where dept = IT
    select * from staff_table where enroll_date like 2013
    """
    sql = input(tip)
    sql = sql.strip().split("where")
    select = sql[0].split(" ")
    if len(sql) > 1:
        where = sql[1].strip().split()
        # print(where)
    if setting.row.get(where[0]):
        if  query_type.get(where[1]):
            staff_table = db.load_db()
            data = query_type[where[1]](where[0],where[1],where[2],staff_table)
            out_put(data,select)
        else:
            print("目前只支持 > ,< ,= ,like 运算!")
    else:
        print("请输入正确的筛选栏位(name,age,phone,dept,enroll_date)！")

#大于、小于
def interact(field,operator,values,staff_table):
    data = []
    for employee in staff_table:
        sql = employee[setting.row[field]] + operator + values
        if eval(sql):
            data.append(employee)
    return data

#等于
def equal(field,operator,values,staff_table):
    data = []
    for employee in staff_table:
        if employee[setting.row[field]].isdigit():
            if int(employee[setting.row[field]]) == int(values):
                data.append(employee)
        else:
            if employee[setting.row[field]] == values:
                data.append(employee)
    return data

#模糊匹配
def like(field,operator,values,staff_table):
    data = []
    for employee in staff_table:
        if str(values) in employee[setting.row[field]]:
            data.append(employee)
    return data

def out_put(data,sql):
    if "*" in sql:
        for i in data:
            i = " ".join(i)
            print(i)
        print("一共查询到%s条记录!" % len(data))
    else:
        field = sql[1].split(",")
        # print(field)
        for q in data:
            for i in field:
                if setting.row.get(i):
                    print(q[setting.row.get(i)], end=" ")
            print("")
        print("一共查询到%s条记录!" % len(data))


#运算符字典
query_type = {
    ">":interact,
    "<":interact,
    "=":equal,
    "like":like
}
#
# data = [['1', 'Alex Li', '33', '13561054562', 'IT', '2013-04-01'], ['2', 'Ivor', '28', '13810772022', 'HR', '2015-05-03'], ['3', 'Rain Liu', '33', '13985871833', 'Sales', '2014-05-09']]
# sql = "select age,name from staff_table"
# ss = sql.strip().split(" ")
# if "*" in ss:
#     for i in data:
#         i = " ".join(i)
#         print(i)
#     print("一共查询到%s条记录!" % len(data))
# else:
#     field = ss[1].split(",")
#     index = 0
#     for q in data:
#         for i in field:
#             if setting.row.get(i):
#                 print(q[setting.row.get(i)],end=" ")
#         print("")
#     print("一共查询到%s条记录!" % len(data))

