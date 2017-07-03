#Authon Ivor
import paramiko
#创建一个连接
conn = paramiko.Transport(('10.0.2.57',22))
conn.connect(username='root',password='test83@123')
#通过连接实例，创建一个FTPClient实例
sftp = paramiko.SFTPClient.from_transport(conn)
# print(sftp.listdir("/tmp/test"))
# files = sftp.listdir_attr("/tmp/test/1")
# print(files)
# for file in files:
#     print(file.st_mode)
#     if stat.S_ISDIR(file.st_mode):
#         print(file)
b = sftp.listdir_attr("/tmp/test/aaa/")
for i in b:
    print(i.filename)
#上传动作
# sftp.put('D:/bbb.txt','/tmp/test/')
# f = sftp.file("/tmp/test")
# print(f.__dir__())
# print(f.__dict__)
# sftp.put('D:\Programs\Python\Python35-32\LICENSE.txt','/tmp/test/bb')
# sftp.mkdir('/tmp/test/ttt')
#下载动作
# print(sftp.listdir('/tmp/test/bbb/'))
# a = sftp.listdir_attr('/tmp/test/2')
# print(a)
# for i in a:
#     print(i.__dict__)
#     print(i.filename)
# sftp.get('/tmp/test/bbb','D:\\1')
conn.close()
