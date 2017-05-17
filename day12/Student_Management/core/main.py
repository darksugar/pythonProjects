#Authon Ivor
from core import auth
from core.auth import login_required
from conf import settings

# from core import logger
# #transaction logger
# trans_logger = logger.logger('transaction')
# #access logger
# access_logger = logger.logger('access')

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def interactive(acc_data):
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
    acc_data = auth.acc_login(user_data)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
def stu_auth():
    acc_data = auth.acc_login(user_data)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)