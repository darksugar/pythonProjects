#Author:Ivor
import copy

person = ["name",['saving',1000]]

#浅copy的三种方式
names2 = copy.copy(person)
names2 = person[:]
names2 = list(person)

#列表指向同一块内存
#names2 = names

#可以用作联合账号
p1 = person[:]
p2 = list(person)

p1[0]='alex'
p2[0]='fengjie'

p1[1][1]=500

print(p1)
print(p2)
