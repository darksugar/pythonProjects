#Authon Ivor

import time
#打印时间戳
print(time.time())
#打印当前时间的时间对象格式
print(time.localtime())

#字符串转换时间对象
print(time.strptime("2016-02-02 15:52:20","%Y-%m-%d %H:%M:%S"))
#时间对象转换字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#时间对象转换时间戳
print(time.mktime(time.localtime()))
#时间戳转换时间对象
print(time.gmtime(time.time()))

import datetime

#打印当前日期时间
print(datetime.datetime.now())
#从时间戳转换成年月日格式
print(datetime.date.fromtimestamp(time.time()))
#从时间戳转换成年月日时间格式
print(datetime.datetime.fromtimestamp(time.time()))
#对当前时间进行加减运算
print(datetime.datetime.now() + datetime.timedelta(days=3))
print(datetime.datetime.now() + datetime.timedelta(hours=-3))
#直接进行时间替换
t = datetime.datetime.now()
print(t.replace(year=2012,month=12,day=24,hour=0,minute=0,second=0))