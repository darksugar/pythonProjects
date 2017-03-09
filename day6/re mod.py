#Authon Ivor
def addition(a):
    return str(float(a[0])+float(a[1]))
def subtraction(a):
    return str(float(a[0])-float(a[1]))
def multiplication(a):
    return str(float(a[0])*float(a[1]))
def division(a):
    return str(float(a[0])/float(a[1]))
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
a = '1-2*((60-30+(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
#a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
while True:
    b = re.search(r'\([^()]+\)',a)
    if b:
        c = re.search('(\d+\.\d+|\d+)/(\d+\.\d+|\d+)',b.group())
        if c:
            d = division(c.group().split("/"))
            a = re.sub(c.group(),d,a)
            print(a)
            continue
        c = re.search('(\d+\.\d+|\d+)\*(\d+\.\d+|\d+)',b.group())
        if c:
            d = multiplication(c.group().split("*"))
            a = re.sub(c.group().replace('*','\*'),d,a)
            print(a)
            continue
        c = re.search('(\d+\.\d+|\d+)\+(\d+\.\d+|\d+)',b.group())
        if c:
            d = addition(c.group().split("+"))
            a = re.sub(c.group().replace('+','\+'),d,a)
            a = re.sub(c.group(), d, a)
            print(a)
            continue
        c = re.search('(\d+\.\d+|\d+)\-(\d+\.\d+|\d+)',b.group())
        if c:
            d = subtraction(c.group().split("-"))
            a = re.sub(c.group().replace('-','\-'),d,a)
            a = re.sub(c.group(),d,a)
            print(a)
            continue
