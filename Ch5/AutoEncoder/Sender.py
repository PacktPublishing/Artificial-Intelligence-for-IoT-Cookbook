#https://github.com/yzhao062/pyod

from kafka import KafkaProducer
import json
import time



server = "localhost:9092"
producer = KafkaProducer(bootstrap_servers=server)

np_array = np.loadtxt('test1.txt', dtype=float)
np_array_to_list = np_array.tolist()
    
for item in np_array_to_list:
    time.sleep(1)     
    alert = {'Gyro':lastestGyro, 'Accel':latestAccel}
    message = json.dumps(alert)
    producer.send(device+'alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
