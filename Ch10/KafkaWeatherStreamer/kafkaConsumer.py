from kafka import KafkaConsumer

import json
MessagesToSend = 0

if __name__ == '__main__':  

# To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('microTopic',
                         group_id='my-group',
                         bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
    x = 0
    for message in consumer:
        x = x+ 1
        if(x%1000 == 0):
        
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
            print ("%d:%s:%d:%d: key=%s value=%s" % (x,message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
