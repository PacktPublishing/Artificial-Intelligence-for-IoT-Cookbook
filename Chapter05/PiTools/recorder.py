from scipy import stats
import numpy as np
from sense_hat import SenseHat
import time
from kafka import KafkaProducer
import json


    
sense = SenseHat()
sense.set_imu_config(True, True, True) 

gyro.insert(0,sense.gyro_raw)
accel.insert(0,sense.accel_raw)