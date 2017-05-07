# !/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()
# 声明queue
channel.queue_declare(queue='hello', durable=True) #durable 队列持久化

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2,)#消息持久化  # make message persistent
                      )
print(" [x] Sent 'Hello World!'")
connection.close()