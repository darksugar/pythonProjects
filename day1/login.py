#Authon Ivor
#初始化用户字典
user_list = {}
#初始化已锁定用户列表
lock_list = []
#初始化密码尝试次数
count = 3
#将用户从文件中导入字典
with open("user.txt","r") as f:
    for k,v in (i.strip().split(" ") for i in f):
        user_list[k] = v
#将锁定用户从文件中导入列表
ff = open("lock.txt","a+")
for i in ff:
        lock_list.append(i)
#输入用户名
username = input("Please input your \033[31;1musername\033[0m:")
#判断用户是否锁定，没锁定则继续，锁定直接退出
if  username not in lock_list:
    #判断用户是否存在
    if user_list.get(username):
        #开始验证密码，输入错误3次则锁定用户，写入文件
        while count > 0:
            #输入密码
            password = input("Please input your \033[32;1mpassword\033[0m:")
            #判断密码是否正确，正确则登录成功，错误则继续尝试，并且尝试次数-1
            if user_list[username] == password:
                print("login success..")
                break
            else:
                count -= 1
                print("Wrong password,you only have %d chances now.." % count)
        else:
            print("you have tried 3 times,lock the user %s" % username)
            text = "%s\n" % username
            ff.write(text)
    else:
        print("Wrong username...")
else:
    print("The user is locked")
ff.close()