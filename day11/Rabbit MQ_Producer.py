#Authon Ivor
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)

channel.basic_publish(exchange='',
                    routing_key='hello',
                    body='Hello World!',
                    property=pika.BasicProperties(delivery_mode=2,)
                    )
print("[x] Send Hello World!")
connection.close()