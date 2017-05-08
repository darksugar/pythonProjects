#Author:Ivor
import pika
import time,json
import paramiko

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def ssh_cmd(msg):
    res_msg = {}
    hosts = msg.get("hosts")
    task_id = msg.get("task_id")
    cmd = msg.get("cmd")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for host in hosts:
        # ssh.connect(hostname=host, port=22, username="root:", password="XXX")
        # stdin, stdout, stderr = ssh.exec_command(cmd)
        # result = stdout.read() if stdout.read() else stderr.read()
        result = "666"
        res_msg[host] = result
    ssh.close()
    response = {
        "task_id": task_id,
        "res_msg":res_msg
    }
    response = json.dumps(response).encode()
    return response
def on_request(ch, method, props, body):
    msg = json.loads(body.decode())
    print(msg)
    response = ssh_cmd(msg)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=response
                     )
    ch.basic_ack(delivery_tag=method.delivery_tag)
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
channel.start_consuming()