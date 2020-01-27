from scipy import stats
import numpy as np
from sense_hat import SenseHat
import time
from kafka import KafkaProducer
import json

device=  "Pi1"
server = "10.121.122.64:9092"
time.sleep(60)     
print('ready')
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
      #  producer.send(device+'alerts' ,key=bytes("alert", encoding='utf-8'),value=bytes(message, encoding='utf-8'))
        print(message)
if __name__ == '__main__':  
    

    x = 0
    if x > 1000: 
        gyro.insert(0,sense.gyro_raw)
        accel.insert(0,sense.accel_raw)
        #time.sleep(1)
        x = x+ 1
    
    while True:
    
        gyro.insert(0,sense.gyro_raw)
        accel.insert(0,sense.accel_raw)
        if x > 1000: 
            gyro.pop() 
            accel.pop() 
        
        time.sleep(1)
        x = x+ 1
        if (zscore(gyro)>4 or zscore(accel)) and x < 120:
            sendAlert(gyro[0],accel[0])
            
       
    
    
 
