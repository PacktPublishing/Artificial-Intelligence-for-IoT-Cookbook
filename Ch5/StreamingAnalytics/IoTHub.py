import time
from azure.iot.device import IoTHubDeviceClient, Message
from sense_hat import SenseHat
import json


msg = '{{"gyro": {gyro},"accel": {accel}}}'
client = IoTHubDeviceClient.create_from_connection_string("HostName=microtemp.azure-devices.net;DeviceId=mikesiot;SharedAccessKey=F39KN2BvgeotC9oxy+ynwOkfYzMSRKQ+/GKfN4XZM60=")
sense = SenseHat()
sense.set_imu_config(True, True, True) 

def combined_value(data):
    return float(data['x'])+float(data['y'])+float(data['z'])

while True:
    gyro = combined_value(sense.gyro_raw)
    accel = combined_value(sense.accel_raw)
     
    msg_txt_formatted = msg.format(gyro=gyro, accel=accel)
    message = Message(msg_txt_formatted)
    client.send_message(message)
    print(gyro)
    time.sleep(1)
