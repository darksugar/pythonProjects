#Authon Ivor

#列表实现队列
#第一种方法
l = []
l.insert(0,'p1')
l.insert(0,'p2')
l.insert(0,'p3')
l.pop()
l.pop()
l.pop()
#第二种方法
l = []
l.append('p1')
l.append('p2')
l.append('p3')
l.pop(0)
l.pop(0)
l.pop(0)

#列表实现堆栈
#实现方法1
l = []
l.insert(0,'p1')
l.insert(0,'p2')
l.insert(0,'p3')
l.pop(0)
l.pop(0)
l.pop(0)
#实现方法2
l = []
l.append('p1')
l.append('p2')
l.append('p3')
l.pop()
l.pop()
l.pop()