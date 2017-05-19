#Authon Ivor
from core import auth
from core.teacher_func import Class_Manage,Class_record_Manage,Score_Manage
from core.student_func import Hand_work,Get_score,Get_ranking
from conf import settings

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def tea_interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Teacher VIew ---------
    \033[32;1m 1.  管理班级
    2.  管理上课记录
    3.  管理成绩
    4.  退出
    \033[0m'''
    menu_dic = {
        '1': Class_Manage,
        '2': Class_record_Manage,
        '3': Score_Manage,
        '4': exit
    }
    while True:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print('accdata',acc_data)
            #acc_data['is_authenticated'] =False
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def stu_interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Virtual  Bank ---------
    \033[32;1m 1.  提交作业
    2.  查看成绩
    3.  查看班级排名
    \033[0m'''
    menu_dic = {
        '1': Hand_work,
        '2': Get_score,
        '3': Get_ranking,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print('accdata',acc_data)
            #acc_data['is_authenticated'] =False
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def tea_auth():
    acc_data = auth.acc_login(user_data,user_type='T')
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        print(user_data)
        tea_interactive(user_data)
def stu_auth():
    acc_data = auth.acc_login(user_data,user_type='S')
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        print(user_data)
        stu_interactive(user_data)