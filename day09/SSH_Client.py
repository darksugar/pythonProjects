#Authon Ivor
import paramiko
#创建SSH实例
ssh = paramiko.SSHClient()
#设置不在known_host的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#建立连接
ssh.connect(hostname="10.0.2.57",port=22,username="root:",password="test83@123")
#执行命令，返回标准输入输出错误
stdin, stdout, stderr = ssh.exec_command("df")
#读取结果
result = stdout.read()
print(result.decode())
#关闭连接
ssh.close()

#SSHClient 封装 Transport
import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', password='123')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()

