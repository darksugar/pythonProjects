#Author:Ivor
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
# ��location.py �ϴ��������� /tmp/51cto.py
sftp.put('/tmp/location.py', '/tmp/51cto_client.py')
# ��remove_path ���ص����� local_path
sftp.get('remove_path', 'local_path')
transport.close()