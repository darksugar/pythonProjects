#Author:Ivor
import pika
import subprocess,json

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='ssh_client',
                         type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='ssh_client',
                       queue=queue_name,
                       routing_key='1.1.1.1')

def execute_cmd(msg):
    cmd = msg.get("cmd").strip('"')
    task_id = msg.get("task_id")
    print(cmd)
    result = subprocess.getoutput(cmd)
    response = {
        "host": '1.1.1.1',
        "res_msg":result,
        "task_id":task_id
    }
    response = json.dumps(response).encode()
    return response
def on_request(ch, method, props, body):
    msg = json.loads(body.decode())
    print(msg)
    response = execute_cmd(msg)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=response
                     )
    ch.basic_ack(delivery_tag=method.delivery_tag)
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue=queue_name)
channel.start_consuming()