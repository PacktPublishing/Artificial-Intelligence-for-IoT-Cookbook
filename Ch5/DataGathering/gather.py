
from scipy import stats
import numpy as np
from sense_hat import SenseHat
import json
import time


sense = SenseHat()
sense.set_imu_config(True, True, True) 
gyro,accel = sense.gyro_raw, sense.accel_raw

dat = np.array([gyro['x']
    ,gyro['y']
  ,  gyro['z']
    ,accel['x']
    ,accel['y']
    ,accel['z']]
    
    )





x = 0



while x < 1000:
    

    x = x + 1
    time.sleep(0.1)
    gyro,accel = sense.gyro_raw, sense.accel_raw
    dat = np.vstack([dat,[[gyro['x']
    ,gyro['y']
  ,  gyro['z']
    ,accel['x']
    ,accel['y']
    ,accel['z']]]]
    
    )
  #  print(dat)
    print(x)


np.savetxt('goin.txt', dat,delimiter=' ', fmt="%10.8f")
