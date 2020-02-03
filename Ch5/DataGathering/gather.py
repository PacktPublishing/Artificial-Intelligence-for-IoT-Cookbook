import numpy as np
from sense_hat import SenseHat
import json
import time

sense = SenseHat()
sense.set_imu_config(True, True, True) 
readings = 1000
gyro,accel = sense.gyro_raw, sense.accel_raw
actions = ['normal', 'anomolous']
dat = np.array([gyro['x'],gyro['y'],gyro['z'],accel['x'],accel['y'],accel['z']])
x = 1

for user_input in actions:
  activity = input('Hit enter to record '+user_input + ' activity')

  while x < readings:
      x = x + 1
      time.sleep(0.1)
      gyro,accel = sense.gyro_raw, sense.accel_raw
      dat = np.vstack([dat,[[gyro['x'],gyro['y'],gyro['z'],accel['x'],accel['y'],accel['z']]]])
      print(readings - x)

X_test = np.concatenate((np.full(800,0), np.full(800,1)), axis=0) 
y_test = np.concatenate((np.full(200,0), np.full(200,1)), axis=0) 
X_train = np.concatenate(dat[0:800],dat[1000:1800])
y_train = np.concatenate(dat[800:1000],dat[1800:2000])

np.savetxt('y_train.txt', y_train,delimiter=' ', fmt="%10.8f")
np.savetxt('y_test.txt',y_test, delimiter=' ',fmt="%10.8f") )
np.savetext('X_train.txt', X_train,delimiter=' ', fmt="%10.8f")
np.savetxt('X_test.txt',x_test, delimiter=' ',fmt="%10.8f") )

  