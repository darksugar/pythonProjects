#Authon Ivor
import pika
connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
            )
channel = connection.channel()
channel.queue_declare(queue="hello",durable=True)

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
                callback,
                queue='hello',
                no_ack=True
                )
print("Waiting for the messages .")
channel.start_consuming()