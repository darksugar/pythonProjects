#Authon Ivor
import os

#读取用户信息,没有则提示用户输入
if os.path.isfile("user_info.txt"):
    with open ("user_info.txt","r") as f:
        for i in f:
            i = i.strip().split(" ")
            username = i[0]
            salary = int(i[1])
else:
    username = input("Please input your \033[31;1mUsername\033[0m:")
    salary = input("Please input your \033[32;1mSalary\033[0m:")
    if salary.isdigit():
        salary = int(salary)

#提取商品信息
product_list = []
with open("products_info.txt") as f:
    for item in f:
        item = item.strip().split(" ")
        product_list.append(item)

#打印商品信息,开始循环
user_list = []
while True:
    for index,item in enumerate(product_list):
        print(index,item[0],item[1])
    choice = input("Please input your choice,exit input [q]:")
    if choice == 'q':
        print("\033[32;1myour balance is %s\033[0m" % salary)
        print("\033[32;1myour good list is %s\033[0m" % user_list)
        break
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(product_list):
            price = int(product_list[choice][1])
            if  salary > price:
                salary -= price
                user_list.append(product_list[choice])
                print("\033[32;1myour balance is %s\033[0m" % salary)
            else:
                print("\033[31;1myour money is not enough...\033[0m")
        else:
            print("\033[31;Invalid numbers...\033[0m")
    else:
        print("\033[31;Wrong choice,please input a number...\033[0m")

#存储剩余余额                                                         +
with open ("user_info.txt","w") as f:
    f.write("{user} {salary}" .format(user=username,salary=salary))




