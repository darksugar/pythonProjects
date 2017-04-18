#Authon Ivor
def addition(a):
    return str(round(float(a[0].strip())+float(a[1].strip()),5))
def subtraction(a):
    return str(round(float(a[0].strip())-float(a[1].strip()),5))
def multiplication(a):
    return str(round(float(a[0].strip())*float(a[1].strip()),5))
def division(a):
    return str(round(float(a[0].strip())/float(a[1].strip()),5))

import re
import datetime

num = '''
请输入运算式:
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
>>>
'''
a = input(num)
begin_time = datetime.datetime.now()
a = a.replace(" ","")
while True:
    b = re.search(r'\([^()]+\)',a)
    if b:
        c = re.search('\d+\.?\d*/(\+|\-)?\d+\.?\d*',b.group())
        if c:
            d = division(c.group().split("/"))
            a = a.replace(c.group(),d)
            continue
        c = re.search('\d+\.?\d*\*(\+|\-)?\d+\.?\d*',b.group())
        if c:
            d = multiplication(c.group().split("*"))
            a = a.replace(c.group(),d)
            continue
        c = re.search('\d+\.?\d*\-\d+\.?\d*',b.group())
        if c:
            d = subtraction(c.group().split("-"))
            a = a.replace(c.group(),d)
            continue
        c = re.search('\d+\.?\d*\+\d+\.?\d*',b.group())
        if c:
            d = addition(c.group().split("+"))
            a = a.replace(c.group(),d)
            continue
        c = re.search('\d+\.?\d*(\+|\-){2}\d+\.?\d*',b.group())
        if c:
            if "+-" in c.group():
                a = a.replace(c.group(),c.group().replace("+-","-"))
            if "--" in c.group():
                a = a.replace(c.group(),c.group().replace("--","+"))
            if "-+" in c.group():
                a = a.replace(c.group(),c.group().replace("-+","-"))
            if "++" in c.group():
                a = a.replace(c.group(),c.group().replace("++","+"))
            continue
        if b and not c:
            a = a.replace(b.group(),b.group().strip("()"))
            continue
    else:
        if "+-" in a:
            a = a.replace("+-","-")
        if "--" in a:
            a = a.replace("--","+")
        if "-+" in a:
            a = a.replace("-+","-")
        if "++" in a:
            a = a.replace("++","+")
        b = re.search('\d+\.?\d*/(\+|\-)?\d+\.?\d*', a)
        if b:
            c = division(b.group().split("/"))
            a = a.replace(b.group(),c)
            continue
        b = re.search('\d+\.?\d*\*(\+|\-)?\d+\.?\d*',a)
        if b:
            c = multiplication(b.group().split("*"))
            a = a.replace(b.group(),c)
            continue
        b = re.search('\d+\.?\d*\-\d+\.?\d*', a)
        if b:
            c = subtraction(b.group().split("-"))
            a = a.replace(b.group(),c)
            continue
        b = re.search('\d+\.?\d*\+\d+\.?\d*', a)
        if b:
            c = addition(b.group().split("+"))
            a = a.replace(b.group(),c)
            continue
        print(a)
        end_time = datetime.datetime.now()

        print("use %s" % (end_time-begin_time))
        print(begin_time,end_time)
        exit()
