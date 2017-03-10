#Authon Ivor
def addition(a):
    return str(float(a[0].strip())+float(a[1].strip()))
def subtraction(a):
    return str(float(a[0].strip())-float(a[1].strip()))
def multiplication(a):
    return str(float(a[0].strip())*float(a[1].strip()))
def division(a):
    return str(float(a[0].strip())/float(a[1].strip()))
# import re
# a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# b = re.search(r'\([^()]+\)',a).group()
# print(b)
# c = re.search('\d+\*\d+',b)
# print(c)
# c = re.search('\d+/\d+',b)
# print(b)
# print(c.group())
# d = c.group().split("/")
# e = division(d[0],d[1])
# print(e)
# f = re.sub(c.group(),e,a)
# print(f)

import re
a = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#1
b = re.search(r'\([^()]+\)',a)
print(b.group())

c = re.search('\s*\d+\.?\d*\s*\*\s*\d+\.?\d*\s*\s*',b.group())
print(c.group())

d = multiplication(c.group().split("*"))
print(d)

a = a.replace(c.group(),d)
print(a)
