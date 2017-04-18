#Authon Ivor

list1 = [1,3,5,6,8,9]
list2 = [2,3,5,6,7,8,0]

set1 =set(list1)
set2 =set(list2)

a = set1 | set2  # t 和 s的并集

b = set1 & set2  # t 和 s的交集

c = set1 - set2# 求差集（项在t中，但不在s中）

d = set1 ^ set2  # 对称差集（项在t或s中，但不会同时出现在二者中）

set1.add('x')  # 添加一项

set1.update([10, 37, 42])  # 在s中添加多项

set1.remove('H') #使用remove() 可以删除一项：

len(set1) #长度

set1.issubset(set2) #子集

set1.issuperset((set2)) #父集

set1.union(set2)  #并集

set2.intersection(t) #交集

set1.remove(5) #删除 没有则报错

set1.discard(6)  #删除 但是不返回

set1.difference(set2) #差集

set1.symmetric_difference(set2)  #对称差集，返回两个集合没有的元素

