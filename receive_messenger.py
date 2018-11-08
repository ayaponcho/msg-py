#!/usr/bin/env python
import pika
import sys
import mysql.connector

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='messenger',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    # Specifying the ODBC driver, server name, database, etc. directly
    #cnxn = mysql.connector.connect("DRIVER={MySQL ODBC 5.3 ANSI Driver}; SERVER=localhost;DATABASE=symfony; UID=root; PASSWORD=;")
    cnxn = mysql.connector.connect(user='root', database='symfony')
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO message (origine, version, status, template_name) VALUES ('test_python', 'v1', '1','welcome')")
    cnxn.commit()
    print(cursor.rowcount, "record inserted.")

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

