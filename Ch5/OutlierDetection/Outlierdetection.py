from scipy import stats
import numpy as np
from sense_hat import SenseHat
import json
from kafka import KafkaProducer
import time


device=  "Pi1"
server = '10.121.122.64:9092'
producer = KafkaProducer(bootstrap_servers=server)
sense = SenseHat()
sense.set_imu_config(True, True, True) 
gyro = []
accel = [] 


def combined_value(data):
    return float(data['x'])+float(data['y'])+float(data['z'])

def zscore(data):
    return np.abs(stats.zscore(np.array(data)))[0]

def sendAlert(lastestGyro,latestAccel):
        alert = {'Gyro':lastestGyro, 'Accel':latestAccel}
        message = json.dumps(alert)
        producer.send(device+'alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
if __name__ == '__main__':  
    x = 0
    while True:
        gyro.insert(0,combined_value(sense.gyro_raw))
        accel.insert(0,combined_value(sense.accel_raw))
        time.sleep(1)
        if x > 1000: 
            gyro.pop() 
            accel.pop() 
        x = x+ 1
        if x > 120:
            if zscore(gyro) > 4 or zscore(accel) > 4:
                sendAlert(gyro[0],accel[0])            
       