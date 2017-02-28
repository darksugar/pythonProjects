#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
main program handle module , handle all the user interaction stuff

'''

from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
from conf import settings
import time

#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
@login_required
def account_info(acc_data):
    # print(user_data['account_data'])
    account_data = accounts.load_current_balance(acc_data["account_id"])
    print("————Account info of %s ————" % account_data["id"])
    for key,value in account_data.items():
        print(key,":",value)
    print("————Account info of %s ————" % account_data["id"])
@login_required
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    #for k,v in account_data.items():
    #    print(k,v )
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount(return input(b):\033[0m").strip()
        if repay_amount == 'b':
            back_flag = True
            continue
        if len(repay_amount) >0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[35;1mNew Balance:%s\033[0m''' %(new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)

@login_required
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount(return input(b)):\033[0m").strip()
        if withdraw_amount == 'b':
            back_flag = True
            continue
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[35;1mNew Balance:%s\033[0m''' %(new_balance['balance']))
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

@login_required
def transfer(acc_data):
    '''
        print current balance and let user do the transfer action
        :param acc_data:
        :return:
        '''
    roll_out_account_data = accounts.load_current_balance(acc_data['account_id'])
    # print(roll_out_account_data)
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (roll_out_account_data['credit'], roll_out_account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        transfer_id = input("\033[34;1mInput transfer id(return input(b)):\033[0m").strip()
        if transfer_id == 'b':
            back_flag = True
            continue
        is_exist = accounts.load_account_is_exist(transfer_id)
        if is_exist:
            roll_in_account_data = accounts.load_current_balance(transfer_id)
            transfer_amount = input("\033[33;1mInput transfer amount(return input(b)):\033[0m").strip()
            if transfer_id == 'b':
                back_flag = True
                continue
            if len(transfer_amount) > 0 and transfer_amount.isdigit():
                roll_out_id = roll_out_account_data['id']
                new_balance = transaction.make_transaction(trans_logger, roll_out_account_data, 'transfer_roll_out', transfer_amount)
                if new_balance:
                    print('''\033[35;1m%s New Balance:%s\033[0m''' % (roll_out_id,new_balance['balance']))
                    new_balance = transaction.make_transaction(trans_logger, roll_in_account_data, 'transfer_roll_in', transfer_amount)
                    print('''\033[35;1m%s New Balance:%s\033[0m''' % (transfer_id,new_balance['balance']))
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)
def pay_check(user_list,bill):
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        status = transaction.make_transaction(trans_logger, acc_data, 'pay_check', bill)
        if status:
            return True

def order_history(acc_data):
    month = input("Please input the bill month:")
    bill = 0
    if month.isdigit():
        bill_file = "%s/log/transactions.log" % settings.BASE_DIR
        with open(bill_file,'r') as f:
            for i in f:
                i = i.strip().split(" ")
                user = i[7].strip().split(":")
                if user[1] == acc_data["account_id"]:
                    if i[-8] == "action:pay_check":
                        date = i[0].strip().split("-")
                        if int(month) == int(date[1]):
                            # action = i[-8].strip().split(":")
                            amount = i[-4].strip().split(":")
                            bill += float(amount[1])
        if bill >0 :
            print("您%s月的消费是%f元！" % (month,bill))
        else:
            print("您%s月没有消费!" % month)


def logout(acc_data):
    exit()
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
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)

