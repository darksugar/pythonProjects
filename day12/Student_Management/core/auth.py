#!_*_coding:utf-8_*_
#__author__:"Alex Li"
from core import db_handler
import time

def login_required(func):
    "验证用户是否登录"
    def wrapper(*args,**kwargs):
        # print('--wrapper--->',args,kwargs)
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("User is not authenticated.")
    return wrapper

def acc_auth(account,password,user_type):
    '''
    优化版认证接口
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_api = db_handler.db_handler()
    if user_type == "T":
        account_data = db_api.teacher_auth(account)
    else:
        account_data = db_api.student_auth(account)
    # print(account_data)
    if account_data:
        if account_data.password == password:
            exp_time_stamp = time.mktime(time.strptime(account_data.expire_date, "%Y%m%d"))
            if account_data.status == 0:
                if time.time() > exp_time_stamp:
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else:  # passed the authentication
                    return account_data
            else:
                print("\033[31;1mThe Account is frozen!!!\033[0m")
        else:
            print("\033[31;1mAccount ID or password is incorrect!\033[0m")

def acc_login(user_data,user_type):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    while not user_data['is_authenticated'] and retry_count < 3 :
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        account_data = acc_auth(account, password,user_type)
        if account_data: #not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            print("Welcome:",account)
            return account_data
        retry_count +=1
    else:
        # log_obj.error("account [%s] too many login attempts" % account)
        print("account [%s] too many login attempts" % account)
        exit()