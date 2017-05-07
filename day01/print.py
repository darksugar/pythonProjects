#Author:Ivor
name = input("Name:")
age = input("age:")
salary = input("salary:")

print("\033[31;1m  select  \033[0m")

info = '''
------ Info of %s------
Name = %s
age = %s
salary = %s
''' % (name,name,age,salary)

info2 = '''
------ Info of {_name}------
Name = {_name}
age = {_age}
salary = {_salary}
'''.format(_name=name,_age=age,_salary=salary)

info3 = '''
------ Info of {0}------
Name = {0}
age = {1}
salary = {2}
'''.format(name,age,salary)

print(info3)
