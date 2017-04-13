#Authon Ivor
import paramiko
#创建一个连接
conn = paramiko.Transport(('10.0.2.57',22))
conn.connect(username='root',password='test83@123')
#通过连接实例，创建一个FTPClient实例
sftp = paramiko.SFTPClient.from_transport(conn)
#上传动作
# sftp.put('D:\\test.xls','/tmp/test.xls')
#下载动作
sftp.get('/tmp/test.xls','D:\\test.xls')
conn.close()