#Authon Ivor
import os

#初始化用户字典
user_list = {}
#将用户从文件中导入字典
with open("user.txt","r") as f:
    for k,v in (i.strip().split(" ") for i in f):
        user_list[k] = v
# 判断用户是否存在
while True:
    username = input("Please input your \033[31;1musername\033[0m:")
    if user_list.get(username):
        # 输入密码
        password = input("Please input your \033[32;1mpassword\033[0m:")
        # 判断密码是否正确
        if user_list[username] == password:
            print("login success..")
            break
        else:
            print("Wrong password")
    else:
        print("Wrong username...")

#读取用户信息,没有则提示用户输入
if os.path.isfile("{user}_info.txt".format(user=username)):
    with open ("{user}_info.txt".format(user=username),"r") as f:
        for i in f:
            i = i.strip().split(" ")
            salary = int(i[1])
else:
    salary = input("New user,please input your \033[32;1mSalary\033[0m:")
    if salary.isdigit():
        salary = int(salary)

#提取商品信息
product_list = []
with open("products_info.txt") as f:
    for item in f:
        item = item.strip().split(" ")
        product_list.append(item)

# 提取用户历史信息
user_goods = []
if os.path.isfile("{user}_goods.txt".format(user=username)):
    with open("{user}_goods.txt".format(user=username),"r") as f:
        for item in f:
            item = item.strip().split(" ")
            user_goods.append(item)

#打印商品信息,开始循环
user_list = []
while True:
    for index,item in enumerate(product_list):
        print(index,item[0],item[1])
    choice = input("Please input your choice,exit input [q],query history input [h]:")
    if choice == 'q':
        print("\033[32;1myour balance is %s\033[0m" % salary)
        print("\033[32;1myour good list is %s\033[0m" % user_list)
        break
    if choice == 'h':
        print(user_goods)
        continue
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
            print("\033[31;1mInvalid numbers...\033[0m")
    else:
        print("\033[31;1mWrong choice...\033[0m")

#存储剩余余额
with open ("{user}_info.txt".format(user=username),"w") as f:
    f.write("{user} {salary}" .format(user=username,salary=salary))
with open("{user}_goods.txt".format(user=username),"w") as f:
    for i in user_goods:
        f.write("{goods} {price}\n" .format(goods=i[0],price=i[1]))