#!/usr/bin/python3

import confluent_kafka
import time
import json
import random
p = confluent_kafka.Producer({'bootstrap.servers': 'localhost:9092'})
while True:
  event = {
    'temp': 23,
    'snow': 8,
    'rain': 4,
    'pressure': 1023,
    'timestamp': int(time.time()),
    'station': random.choice(['A', 'B'])
  }
  p.produce('weather', json.dumps(event), key=event['station']) 
  time.sleep(1)

