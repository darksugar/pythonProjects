#Authon Ivor

dic_list = {
    "1.北京":{
        "2.东城": {},
        "3.崇文": ['虹桥市场','北京游乐园','百荣商场'],
        "4.西城": {},
        "5.宣武": {}
    },
    "上海":{},
    "广州":{}
}
#优化写法
level = []
while True:
    for i in dic_list:
        print(i)
    choice = input("Please input your choice exit(q):")
    if choice == 'b':
        if len(level) == 0:
            break
        dic_list = level[-1]
        level.pop()
        continue
    level.append(dic_list)
    dic_list = dic_list[choice]

#
# while True:
#     for i in dic_list:
#         print(i)
#     choice = input("Please input your choice exit(q):")
#     if choice == "q":
#         print("exit the program..")
#         exit()
#     while True:
#         if choice in dic_list.keys():
#             for i in dic_list[choice]:
#                  print(i)
#             choice2 = input("Please input your choice2 exit(q) return(r):")
#             if choice2 == "q":
#                 print("exit the program..")
#                 exit()
#             elif choice2 == 'r':
#                 break
#         if choice2 in dic_list[choice]:
#             while True:
#                 for i in dic_list[choice][choice2]:
#                     print(i)
#                 choice3 = input("Please input your choice3 exit(q) return(r):")
#                 if choice3 == "q":
#                     print("exit the program..")
#                     exit()
#                 elif choice3 == 'r':
#                     break