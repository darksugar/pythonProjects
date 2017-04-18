#Authon Ivor

name = [0,1,2]
dic = {}

try:
    name[3]
except IndexError as e :
    print(e)
try:
    dic['666']
except KeyError as e:
    print("KeyError",e)

except Exception as e:
    print("可以抓到任何错误！")
else:
    print("没有错误时我会运行！")
finally:
    print("不管怎么样，我都会运行！")

# 常用异常
# AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
# 导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的

