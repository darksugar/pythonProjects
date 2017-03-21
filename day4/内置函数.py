#Authon Ivor

#filter 筛选
res = filter(lambda n:n>5,range(10))
print(res)
for i in res:
    print(i)

#sorted排序
a = {1:3
     ,5:-7
    ,3:10}
b = [1,4,5,8,6,4,2,4,6,]
print(a.items())
print(sorted(a.items(),key=lambda x:x[0]))
print(sorted(a.items(),key=lambda x:x[1]))

#all里边如果都为真，返回真，非0都为真
all([1,0,-3])

#any里边如果有一个为真，则返回真
any([0,2,-3])

#ascii 把内存的数据变成一个可打印的字符串
a = ascii([1,2,666])
print(type(a),a,[a])

#bin 把一个整数十进制到二进制转换

#boll 判断真假

#id 返回内存地址

#frozenset

#globals

#locals

#float

#int

#isinstance()

#max min

#chr ord
#pow
#ascii