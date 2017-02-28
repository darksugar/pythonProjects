#Authon Ivor
import sys
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core import main

#提取商品信息
product_list = []
user_list = []
products_file = "%s/db/products_info.txt" % base_dir


with open(products_file) as f:
    for item in f:
        item = item.strip().split(" ")
        product_list.append(item)

def the_mall():
    while True:
        for index,item in enumerate(product_list):
            print(index,item[0],item[1])
        user_choice = input("请输入想要购买的商品编号,查看购物车输入[g]，返回输入[r]:")
        if user_choice == "g":
            print("------your list------")
            for item in user_list:
                print(item)
            print("---------------------")
            continue
        if user_choice == "r":
            break
        if user_choice.isdigit():
            choice = int(user_choice)
            if choice >= 0 and choice < len(product_list):
                user_list.append(product_list[choice])
            else:
                print("\033[31;1mInvalid numbers...\033[0m")
        else:
            print("\033[31;1mWrong choice...\033[0m")

def order():
    while True:
        print("--------------------")
        for item in enumerate(user_list):
            print(item)
        print("--------------------")
        user_choice = input("请输入想要从购物车删除的商品编号，返回输入[r]:")
        if user_choice == "r":
            break
        if user_choice.isdigit():
            choice = int(user_choice)
            if choice >= 0 and choice < len(user_list):
                user_list.remove(user_list[choice])
            else:
                print("\033[31;1mInvalid numbers...\033[0m")
        else:
            print("\033[31;1mWrong choice...\033[0m")


def check_up():
    ensure = input("您确认要结账么，确认请输入[y]:")
    if ensure == 'y':
        order_bill = 0
        for item in user_list:
            order_bill += int(item[1])
        status = main.pay_check(user_list,order_bill)
        if status:
            user_list.clear()
            print("您的账单已经结清！")
        else:
            print("付款失败！")


#打印商品信息,开始循环
def run():
    while True:
        menu = '''
        1. 进入商城购物
        2. 操作购物车
        3. 结账
        q. 退出
        '''
        menu_dic= {
            "1":the_mall,
            "2":order,
            "3":check_up,
            "q":exit
        }
        print(menu)
        choice = input("请输入对应编号:")
        if menu_dic.get(choice):
            menu_dic[choice]()


