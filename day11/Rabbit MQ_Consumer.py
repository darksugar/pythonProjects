# _*_coding:utf-8_*_
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello', durable=True) #durable 队列持久化

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(20)
    print(" [x] Done")
    print("method.delivery_tag",method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag) #将处理完成的结果反馈给queue

channel.basic_qos(prefetch_count=1) #消息公平分发
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True) #让队列等待结果 #Tell the broker to expect a response
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()