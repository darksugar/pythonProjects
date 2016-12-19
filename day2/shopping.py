#Author:Ivor

salary = int(input("Please input your Salary...:"))
goods = [['1','iphone',5999],['2','coffee',50],['3','bike',800],['4','python book',101],['5','girlfriend',19999]]
l= []

while True:
    for i in goods:
        n=0
        info = '''
    ----------------------
    {id}  {goods}  {price}'''.format(id=i[0],goods=i[1],price=i[2])
        n += n
        print(info)
    choose = int(input("which one?:"))
    if salary > goods[choose-1][2]:
        salary = salary - goods[choose-1][2]
        l.append(goods[choose - 1])
    else:
        print("your money is not enough..")
        break
print("your money is..",salary)
print("your good is..",l)
