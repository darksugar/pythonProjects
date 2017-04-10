#Author:Ivor

lib = __import__("lib.aa")  #动态导入

lib.aa.c()

try:                #正常代码
    pass
except (KeyError,IOError) as e:
    pass
except Exception as e: #抓取任何异常
    pass
else:               #没有发生异常
    pass
finally:            #无论怎样都执行
    pass

#断言,保证后边代码正常运行
assert type("aaa") is str

