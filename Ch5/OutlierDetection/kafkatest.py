from kafka import KafkaProducer
import json

device=  'YOURDEVICEID'
server = '127.0.0.1:9092'

producer = KafkaProducer(bootstrap_servers=server)
alert = {'button':'event.action', 'direction':'event.direction', 'device':'device'}
message = json.dumps(alert)

producer.send(device+'alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))