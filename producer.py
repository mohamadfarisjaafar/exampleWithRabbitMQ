import pika
import sys

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (a queue is like a buffer that stores messages)
channel.queue_declare(queue='hello')

# Send a message to the queue
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(f" [x] Sent '{message}'")

# Close the connection
connection.close()
