import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (it must match the one used by the producer)
channel.queue_declare(queue='hello')

# Callback function that will be called when a message is received
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Tell RabbitMQ to send messages from the queue to our callback function
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
