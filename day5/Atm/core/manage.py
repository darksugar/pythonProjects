#Author:Ivor
from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required


def change_credit():
    account_id = input("Please input the account id:")
    account_data = accounts.load_current_balance(account_id)
    if account_data:
        current_balance = ''' --------- BALANCE INFO --------
               Credit :    %s
               Balance:    %s''' % (account_data['credit'], account_data['balance'])
        print(current_balance)
        account = input("\033[33;1mInput the account your want to change:\033[0m")
        if account.isdigit():
            if int(account) > -account_data["balance"]:

                print("\033[32;1m%s's account is changed to %s\033[0m" % (account_id,account))
            else:
                print('\033[31;1m[%s] is less than your balance,please repay your bill first!\033[0m' % account)
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % account)
    else:
        print("the account is not exists!")


def add_account():
    pass

def freeze_account():
    pass

def unfreeze_account():
    pass

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