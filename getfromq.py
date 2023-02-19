import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fibonacci')


def my_callback(ch, method, properties, body):
    print("Received message:", body)


channel.basic_consume(queue='fibonacci', on_message_callback=my_callback, auto_ack=True)
channel.start_consuming()
