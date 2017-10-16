#!/usr/bin/python3

import confluent_kafka
import time
import json
import random
p = confluent_kafka.Producer({'bootstrap.servers': 'localhost:9092'})
topic = 'car'
points = 3
while True:
  randomtime = random.uniform(0, 0.2)
  event = {
    'lane': random.randint(1, 3),
    'timestamp_in_1': time.time(),
    'timestamp_out_1': time.time() + randomtime * 1,
    'timestamp_in_2': time.time() + randomtime * 2,
    'timestamp_out_2': time.time() + randomtime * 3,
    'speed': random.randint(40, 140),
    'gap_meters': random.randint(10, 200),
    'gap_seconds': 1,
    'length': 4,
    'point_id': random.randint(1, points)
  }
  p.produce(topic, json.dumps(event), key=str(event['point_id'])) 
  time.sleep(random.uniform(0.0005, 0.0010))
  #time.sleep(random.uniform(0.0002, 0.0004))
  if random.randint(0, 100) == 0:
    p.flush()

