#Author:Ivor
#######
#funtion 1
#######
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='59.110.23.110', port=22, username='root', pkey=private_key)

stdin, stdout, stderr = ssh.exec_command('df')

result = stdout.read()
print(result.decode())
ssh.close()

########
#funtion 2
########
import paramiko
from io import StringIO
key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEoQIBAAKCAQEAoNufx4m+YDIW2Gpz4uifFprAyO6OnE5YAzMeZWIbvKOTL4PA
g48DUYjyo2EVvKXfcQl+7ENvnolR0VPlzDB2mi3pLf7xZvLsxJWcWmiBuy5HgoeP
m7nmI74T3wIMEmjX5D1vhRJW2HZYg7jw+OzbsBXjZsR3mxBBOiu6OKCcsFWryE8J
bwI6xnR79XNDAnlg2JdFYNg05Dd8SWuHsSvXg4u51GleuxmR+L1bFwZm8DpRudgX
ksvGsSqcC5JKuR1PAjvkRoIaeApQIh5wfkQ3MBj0Hagffj88EryR9JDOu/4YLDn1
OHnh0sq5sIF8cCIDlmixI0NFBehEsfCrAl58KQIBIwKCAQEAjnlhohrqcnWB8uHx
nRct0jFLqqdoXo6Id9zRx4LIHBvaIsUm2uxiBmNakLUTQLAsTiz7Y4wvqazTcEL+
vCrstHHOh9MtlbKXMcZXSML2j9iIeu0Yy8HpGFfltuSOWXLN2MizO1li3PsbMtcB
UYFU3co+cPcoG6CuzR9qbKuDd5rugXd0mEez0HnZrhzUFlv6O46pKhQjb9CrXWPX
SlLYuneR2EqhJMRX31mVkpPY8JVpkKE9QTJUJ3EW3FW4adoutsN3HYzGnU2dldoP
7h6P6hz0jduRMw5PJeORef35ktxIBvR45tqpVrNA/cmlq/mdZpL95SF4kgOVrtqb
kTmKCwKBgQDUAKvUmDha/tQ+iIe1WfxM7xHGWxUoVVbJksEepCFiiXhTX9jUePdd
FC+syQi+ah0KGvfTui3MpmsDYy3tW11tE40lxM17EUZQ+aPBGj22MWqdCCbODbg0
zyFS/jtX16/hDu4NEE+hEehWF2XJ/l3Ivo6YRp1sdUfQg6f/pUcxcQKBgQDCPbk9
ljba9QYmoBVT4dMq8Joa3oMFlMOOI+9dNP+ASJSpBH5Yc3YTvxgFbrGSj0MKPaYX
djvdGAYbwCSdrG61curU7LrX7vjA2iFjmT7WQK6uVE+c/RPGrXlIIkc8FTR6cEhn
6beBkIueWYqcjpGh6CvhbpjUkO78u3Li8u8aOQKBgEivxeJ9VSaDQXSGlO24c8Kb
HAl+UGWZmhk5oUxVh8oDPzKHQwcE5xiZNOrIlUiZaQrHaumBqU164tyXCG6i+3Xa
0U7HIeENPK4McqibSFu5K94RbGPncls/s6dtG6kWv/VkNFxAG00qtg7jc1syo8/M
TiWUjb7JH++4HFemYY1LAoGAQpjRy/j83VtSkOZttlwN4tYmNRkW+plnnnK4d7pm
OpyKvZskARGk05H5m3ZoxIjjyP8xoaThUx4t+uLKubd2ahjFitTSWKm0X2C6/ZOg
g/jrbvhVz2y2Ur8iRJ4Jy3T8DLjIXiQ+6pf1WtzfERrwGkD5GhdKV4ImDYIYwtby
5GsCgYA7o1MVpkf5VglQFj0Ywlk10f6F6UpSP5YrqZbAYlBYO2YUe59eisE8oAXK
Jf1Ha/Z3pMOZFXwmeqt+Ge0wUNHOqgllSg5bl6QLYaHEGccbAwcZejxHpmMaE47D
dgXdbEadXJpuBdrMUosLjaJ5Ea8FtTSWyg8cYdCvNhZkcUxjpA==
-----END RSA PRIVATE KEY-----'''
private_key = paramiko.RSAKey(file_obj=StringIO(key))
transport = paramiko.Transport(('59.110.23.110', 22))
transport.connect(username='root', pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()
transport.close()
print(result)
