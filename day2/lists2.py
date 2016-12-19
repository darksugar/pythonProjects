#Author:Ivor
#list使用

names = ["zZhangsan","lisi",['www','bbbb'],"wangwu","xiaoliu"]

#names.copy() 浅copy,只复制第一层
names2 = names.copy()

#import copy;copy.deepcopy(),深copy，完全复制

#import copy;copy.copy(),也是浅copy

#列表指向同一块内存
#names2 = names

#
names[1] = 'aaaaa'
names[2][0] = 'ccccc'


print(names)
print(names2)
