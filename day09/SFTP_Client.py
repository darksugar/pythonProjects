#Authon Ivor
import stat
import paramiko
#创建一个连接
conn = paramiko.Transport(('10.0.2.57',22))
conn.connect(username='root',password='test83@123')
#通过连接实例，创建一个FTPClient实例
sftp = paramiko.SFTPClient.from_transport(conn)

# print(sftp.listdir("/tmp/test"))
files = sftp.listdir_attr("/tmp/test")
print(files)
for file in files:
    print(file.st_mode)
    if stat.S_ISDIR(file.st_mode):
        print(file)
# print(sftp.listdir_iter("/tmp/test"))
#上传动作
# sftp.put('D:/aaa.txt','/tmp/test/')
# f = sftp.file("/tmp/test")
# print(f.__dir__())
# print(f.__dict__)
# sftp.put('D:\Programs\Python\Python35-32\LICENSE.txt','/tmp/test/bb')
# sftp.mkdir('/tmp/test/ttt')
#下载动作
# sftp.get('/tmp/test.xls','D:\\test.xls')
conn.close()
