#Author:Ivor

lib = __import__("lib.aa")  #��̬����

lib.aa.c()

try:                #��������
    pass
except (KeyError,IOError) as e:
    pass
except Exception as e: #ץȡ�κ��쳣
    pass
else:               #û�з����쳣
    pass
finally:            #����������ִ��
    pass

#����,��֤��ߴ�����������
assert type("aaa") is str

