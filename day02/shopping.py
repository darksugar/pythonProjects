#Author:Ivor
product_list = [
    ["iphone", 5999],
    ["bike", 899],
    ["book", 120],
    ["coffee", 31]
]
goods =[]
salary = input("please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input(">>>")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >= 0 and user_choice < len(product_list):
                if salary > product_list[user_choice][1]:
                    salary -= product_list[user_choice][1]
                    goods.append(product_list[user_choice])
                    print("your balance is:",salary)
                else:
                    print("your money is not enough..")
            else:
                print("in valid number!")
        elif user_choice == 'q':
            print("your balance is ",salary)
            print("your shop list is ",goods)
            break
        else:
            print("invalid choice")
else:
    print("invalid value!")




