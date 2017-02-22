#Authon Ivor

#查询
def select():
    select_str = input("please input your \033[31;1mselect\033[0m backend:")
    with open("haproxy","r") as f:
        for i in f:
            i = i.strip().split(" ")
            if i[0] == "backend" and i[1] == select_str:
                print(f.readline())

#新增
def add():
    stop_str = ''
    add_str = ''
    print("please input your \033[31;1madd\033[0m backend:↓↓↓")
    for line in  iter(input,stop_str):
        add_str += line.strip()
    add_str = eval(add_str)
    with open ("haproxy","a") as f:
        first_line = "\nbackend " + add_str["backend"]
        second_line = "\n\t\tserver " + add_str["record"]["server"] + " weight " + str(add_str["record"]["weight"]) + " maxconn " + str(add_str["record"]["maxconn"])
        f.write(first_line)
        f.write(second_line)
        print("\033[31;1mthe new backend is added\033[0m")

#删除
def delete():
    del_str = ''
    stop_str = ''
    print("please input your \033[31;1mdel\033[0m backend:↓↓↓")
    for line in  iter(input,stop_str):
        del_str += line.strip()
    del_str = eval(del_str)

    read = []
    with open("haproxy","r") as f,open("haproxy_bak","w") as bak:
        for  line in f:
            read.append(line)
            bak.write(line)

    for index,line in enumerate(read):
            if line.strip() == "backend " + del_str["backend"]:
                if read[index+1].strip() == "server " + del_str["record"]["server"] + " weight " + str(del_str["record"]["weight"]) + " maxconn " + str(del_str["record"]["maxconn"]):
                    del read[index]
                    del read[index]
                    print("\033[31;1mthe backend is already delete\033[0m")
    with open("haproxy","w") as f:
        for line in read:
            f.write(line)

#修改
def change():
    chg_str = input("please input your \033[31;1mchange\033[0m string:")
    new_str = input("please input your \033[31;1mnew\033[0m string:")

    read = []
    with open("haproxy","r") as f,open("haproxy_bak","w") as bak:
        for  line in f:
            read.append(line)
            bak.write(line)

    for index,line in enumerate(read):
            if chg_str in line:
                line = line.replace(chg_str,new_str)
                read[index] = line
                print("\033[31;1m%s has changed to %s!\033[0m" % (chg_str,new_str))
    with open("haproxy","w") as f:
        for line in read:
            f.write(line)

while True:
    choose = input(
        '''choose what you want?
        1.select
        2.add new
        3.delete
        4.change
        q.exit
        ''')
    if choose == '1':
        select()
    if choose == '2':
        add()
    if choose == '3':
        delete()
    if choose == '4':
        change()
    if choose == 'q':
        exit()