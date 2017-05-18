#Authon Ivor
from core import auth
from core.teacher_func import Class_Manage,Class_record_Manage,Score_Manage
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
    \033[32;1m 1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': order_history,
        '6': logout,
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