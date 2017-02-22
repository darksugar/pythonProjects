#Authon Ivor

# res = filter(lambda n:n>5,range(10))
# print(res)
# for i in res:
#     print(i)

#sorted排序
a = {1:3
     ,5:-7
    ,3:10}
print(a.items())
print(sorted(a.items(),key=lambda x:x[1]))