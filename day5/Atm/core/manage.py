#Author:Ivor
from core import auth
from core import accounts
from core import logger
from core import accounts
import time
from core import db_handler
import datetime
from core import transaction
from core.auth import login_required


manage_log = logger.logger('manage')


def change_credit():
    account_id = input("Please input the account id:")
    account_data = accounts.load_current_balance(account_id)
    old_credit = account_data['credit']
    if account_data:
        current_balance = ''' --------- BALANCE INFO --------
               Credit :    %s
               Balance:    %s''' % (account_data['credit'], account_data['balance'])
        print(current_balance)
        account = input("\033[33;1mInput the account your want to change:\033[0m")
        if account.isdigit():
            if int(account) > -account_data["balance"]:
                account_data['credit'] = account
                accounts.dump_account(account_data)
                manage_log.info("account:%s   action:change_credit    old_credit:%s   new_credit:%s" %
                          (account_data['id'], old_credit,account_data['credit']) )
                print("\033[32;1m%s's account is changed to %s\033[0m" % (account_id,account))
            else:
                print('\033[31;1m[%s] is less than your balance,please repay your bill first!\033[0m' % account)
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % account)
    else:
        print("the account is not exists!")


def add_account():
    acc_id = input("Please input the new account id:")
    exists = accounts.load_current_balance(acc_id)
    if exists:
        print("%s is exist!" % acc_id)
        return
    acc_passwd = input("Please input the password of %s:" % acc_id)
    credit = input("Please input the credit of %s:" % acc_id)
    acc_data = {}
    acc_data['id'] = acc_id
    acc_data['password'] = acc_passwd
    acc_data['credit'] = credit
    acc_data['balance'] = 0
    acc_data['enroll_date'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    acc_data['expire_date'] = '2021-01-01'
    acc_data['pay_day'] = '22'
    acc_data['status'] = 0
    db_handler.add_account(acc_data)
    if db_handler:
        print("Account %s is created!" % acc_id)

def freeze_account():
    account_id = input("Please input the account id:")
    account_data = accounts.load_current_balance(account_id)
    if account_data:
        current_status = ''' --------- Account INFO --------
               Current Status : %s
               Normal : 0
               Freeze : 1''' % (account_data['status'])
        print(current_status)
        if account_data['status'] == 1:
            print("The account is already frozen!")
        else:
            user_option = input("Please confirm to freeze the account[y]: ")
            if user_option == 'y':
                account_data['status'] = 1
                accounts.dump_account(account_data)
                manage_log.info("account:%s   action:freeze_account" %
                          (account_data['id']))
                print("Account %s is freeze now!" % account_id)
            else:
                print("Nothing changed!")
    else:
        print("The account is not exists!")


def unfreeze_account():
    account_id = input("Please input the account id:")
    account_data = accounts.load_current_balance(account_id)
    if account_data:
        current_status = ''' --------- Account INFO --------
               Current Status : %s
               Normal : 0
               Freeze : 1''' % (account_data['status'])
        print(current_status)
        if account_data['status'] == 0:
            print("The account is Normal,no need to unfreeze!")
        else:
            user_option = input("Please confirm to unfreeze the account[y]: ")
            if user_option == 'y':
                account_data['status'] = 0
                accounts.dump_account(account_data)
                manage_log.info("account:%s   action:unfreeze_account" %
                          (account_data['id']))
                print("Account %s is Normal now!" % account_id)
            else:
                print("Nothing changed!")
    else:
        print("The account is not exists!")


def manage():
    '''
    the entrance of manage
    :return:
    '''
    menu = '''
    ------- User Management  ---------    \033[32;1m
        1.  修改用户额度
        2.  添加账户
        3.  冻结账户
        4.  启用账户
    \033[0m
    '''
    menu_dic = {
        "1":change_credit,
        "2":add_account,
        "3":freeze_account,
        "4":unfreeze_account
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print("\033[31;1mOption does not exist!\033[0m")