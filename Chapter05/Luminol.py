from kafka import KafkaConsumer
from datetime import datetime
import json

server = "localhost:9092"


consumer = KafkaConsumer( group_id=device, bootstrap_servers=server)
consumer.subscribe(['devicetelem'])

for msg in consumer:
    jSon = msg.value.decode('utf-8')
    jDict = json.loads(jSon)
    accel =jDict['accel']
    gyro = jDict['gyro']

    