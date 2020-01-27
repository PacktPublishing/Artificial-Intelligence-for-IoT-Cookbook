from scipy import stats
import numpy as np
from sense_hat import SenseHat
import json
from kafka import KafkaProducer
import time


time.sleep(60)     
device=  "Pi1"
server = "[ip address of your kafka server]:9092"
producer = KafkaProducer(bootstrap_servers=server)
sense = SenseHat()
sense.set_imu_config(True, True, True) 
gyro = []
accel = [] 


def zscore(data):
    return np.abs(stats.zscore(np.array(data)))[0]

def sendAlert(lastestGyro,latestAccel):
        alert = {'Gyro':lastestGyro, 'Accel':latestAccel}
        message = json.dumps(alert)
        producer.send(device+'alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))

if __name__ == '__main__':  
    x = 0
    while True:
        gyro.insert(0,sense.gyro_raw)
        accel.insert(0,sense.accel_raw)
        if x > 1000: 
            gyro.pop() 
            accel.pop() 
        time.sleep(1)
        x = x+ 1
        if x > 120:
            if zscore(gyro) > 4 or zscore(accel) > 4:
                sendAlert(gyro[0],accel[0])            
       