#Authon Ivor
import sys
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core import main

products_file = "%s/db/products_info.txt" % base_dir

#读取商品信息
product_list = []
with open(products_file,"r") as f:
    for i in f:
        i = i.strip().split(" ")
        product_list.append(i)
#开始循环，新增或者修改
while True:
    for index, i in enumerate(product_list):
        print(index, i[0], i[1])
    entrance = input("Please choice what do you want? Add goods\033[032;1m(a)\033[0m change goods\033[032;1m(c)\033[0m save&quit\033[032;1m(s)\033[0m...[a/c/s]")
    #修改
    if entrance == 'c':
        choice = input("Please input goods's number...")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(product_list):
                change_price = input("please input your  price...")
                if change_price.isdigit():
                    product_list[choice][1] = change_price
    #新增
    elif entrance == 'a':
        goods = input("please input the name of goods..")
        price = input("please input the price of goods..")
        if price.isdigit():
            product_list.append([goods,price])
            print("your goods is added to products list...")
        else:
            print("Invalid numbers...")
    elif entrance == 's':
        break

#将修改后的结果写入文件
with open("products_info.txt","w",encoding="utf-8") as f:
    for i in product_list:
        text = "{goods} {price}\n".format(goods=i[0],price=i[1])
        f.write(text)
