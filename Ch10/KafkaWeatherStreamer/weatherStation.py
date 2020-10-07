from BuildData import BuildData
from kafka import KafkaProducer
import json
import time
MessagesToSend = 0

if __name__ == '__main__':  
    #producer = KafkaProducer(bootstrap_servers='wn0-microk.l1nji5hfpjbe5g4bvryy2aon2a.gx.internal.cloudapp.net:9092')
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    buildData = BuildData()
    template = buildData.loadTemplate("weatherStation.json")
    

    x = 0
    while(x < MessagesToSend or MessagesToSend == 0):
        time.sleep(0.05)
        x = x+ 1
        MessagesToSend -= MessagesToSend
        message = buildData.getDistribution(template)
        if(x%1 == 0):
            print(str(x) + ' ' + message)
        producer.send('weather',key=bytes(str(x%10), encoding='utf-8'),value=bytes(message, encoding='utf-8'))
     