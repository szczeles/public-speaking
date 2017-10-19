# Safer roads with kafka&python

pyData Warsaw 2017

---

# About me

<ul>
<li class="fragment">Mariusz Strzelecki</li>
<li class="fragment"><img src="http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png", width="40%" /></li>
<li class="fragment">**pyspark** and **spark** stackoverflow tags</li>
</ul>

Note:
 - data ecosystem engineer, not data scientist

---?image=https://img00.deviantart.net/b90d/i/2009/314/9/f/welcome_to_accident_by_howardtj43147.jpg&size=cover

Note:
- 1.3 mln dead
- 20 mln wounded

+++

## Road "unsafety" features

- weather conditions |
- traffic |
- road shape, surface quality |
- calendar |

Note:
weather: for, wind, rain, show, sun

traffic:
  - road occupancy
  - vehicles speed (compared to allowed speed)
  - gaps between vehicles and their length

calendar: day of week, national holiday

+++?image=https://ops.fhwa.dot.gov/freewaymgmt/publications/frwy_mgmt_handbook/images/fig15-1.jpg&size=contain

+++?image=assets/images/loop-controller.jpg&size=cover

+++?image=assets/images/flanders.png&size=contain

+++?image=assets/images/model_building_1.png&size=cover

+++

# Example model

- traffic statistics (average speed, average gap, min gap, number of cars) on: |
   - 1-minute window |
   - 10-minutes window |
- weather |
- road shape and condition |

+++?image=assets/images/model_building_2.png&size=cover

+++?image=assets/images/model_building_3.png&size=cover

---

# Streaming 

Note:
 - Nowadays data are coming in streaming-way
 - IoT (sensors, cars) will not wait off-line data
 - Events - search events from users should have instant impact on what we deliver to users

+++?image=https://kafka.apache.org/images/logo.png&size=contain

Note:
 - distributed log/journal
 - 2011

+++?image=assets/images/kafka.png&size=cover

Note:
 - topics/subjects
 - multiple producers
 - partitions paradighm - multiple consumers
 - from 0.11 (newest release) transactions and exactly-once delivery - so can be used as enterprise message bus
 - good community support

+++?image=assets/images/model_building_4.png&size=cover

+++

# Real-time challenges

- real-time grouping inductive loops events (windowing) |
- handling global state of current weather |
- joining two streams of events |

---

# Kafka meets python

- [Confluent Kafka Client](https://github.com/confluentinc/confluent-kafka-python)
- [Spark Streaming](https://spark.apache.org/docs/2.2.0/streaming-kafka-0-10-integration.html)
- [Winton Kafka Streams](https://github.com/wintoncode/winton-kafka-streams)

+++

## Confluent Kafka Client

```python
consumer = Consumer({'metadata.broker.list': ...})
consumer.subscribe(['topic'])

while True:
    msg = consumer.poll()
    do_something_with(msg)
```
@[1-2]
@[4-7]

Note:
 - based on library written in C

+++

## Spark Streaming

```python
spark = SparkSession.builder.getOrCreate()
ssc = StreamingContext(spark.sparkContext, 1)
stream = KafkaUtils.createDirectStream(ssc, ['topic'], ...)

stream.window(10, 2).map(...).join(...).pprint()
```
@[1-3]
@[5]

+++

## Winton Kafka Streams

```python
topology_builder \
    .source('raw_event', ['input_topic']) \
    .processor('processed_event', Processor, 'raw_event') \
    .sink('sink', 'output_topic', 'processed_event')

kafka_streams.KafkaStreams(topology_builder, kafka_config) \
    .start()
```
@[1-4]
@[6-7]

---?image=https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Two_Windows_Aarhus.jpg/1280px-Two_Windows_Aarhus.jpg&size=cover

<br/><br/><br/><br/><br/><br/><br/><br/>
<h1 style="color: white">(double) windowing</h1>

+++?image=assets/images/double_windowing.png&size=cover

+++

## Raw client

```python
def generate_windows(): # every minute
    short_window = data[
        (ts_field >= current_time - one_minute) &
        (ts_field <= current_time)]
    long_window = data[
        (ts_field >= current_time - ten_minutes) &
        (ts_field <= current_time)]

while True:
    msg = consumer.poll()
    append_message(msg.value())
```

+++

## Spark Streaming

```python
short_window = stats_of(
    input_stream.window(one_minute, one_minute))
long_window = stats_of(
    input_stream.window(ten_minutes, one_minute))

short_window.join(long_window)
```

Note:
 - https://issues.apache.org/jira/browse/SPARK-18791 - strustured steraming do not have joins
+++

## Winton Kafka Streams

```python
class ProcessLoopEvent(BaseProcessor):
    def initialise(self, name, context):
        self.context.schedule(one_minute)
        
    def punctuate(self, timestamp): # called every 1 minute
        short_window_data = self.last_minute_events()
        long_window_data = self.last_ten_minutes_events()
        combined = (short_window_data, long_window_data)
        self.context.forward(None, json.dumps(combined))
    
    def process(self, key, value):
        append_message(value)
```

---?image=assets/images/puzzle.jpg&size=cover

<h1 style="padding-left: 60%">Global state</h1>

+++

## Raw client

```python
class WeatherState:
    def update(self, key, value):
        self.state[key] = value
        
    def get_current_state(self):
        return self.state
        
weather_state = WeatherState()

while True:
    msg = consumer.poll()
    weather_state.update(msg.key(), msg.value())
```

+++

## Spark Streaming

```python
def get_newest(new_values, last_state):
    if len(new_values) == 0:
        return last_state
    return new_values[0]

weather_stream.updateStateByKey(get_newest)
```

+++

## Winton Kafka Streams

```python
topology_builder \
    .processor('weather', UpdateWeather, 'weather-event') \
    .processor('stats', CalculateStatsAndJoin, 
                                      'loops-windows')
    .state_store('weather_store', WeatherStore, 
                                      'weather', 'stats')
```

---?image=http://i.imgur.com/FP5GKOK.jpg&size=cover

<h1 style="color: white">Joining<br />streams</h1>
<br/><br/> <br/><br/><br />

+++

## Raw client

```python
# pandas local join only

joined_windows.set_index('nearest_weather_station') \
    .join(weather_state.get_current_data()) \
    .set_index('point_id')
```

+++

## Spark Streaming

```python
cars_stats_with_point_data.join(weather_state)
```

+++

## Winton Kafka Streams

```python
# the same issue like raw client
# local pandas join possible
```

---

## And the winner is...

1. Spark Streaming
2. Winton Kafka Streams
3. Raw client

<img src="https://image.flaticon.com/icons/png/128/25/25231.png" style="width: 64px"> **szczeles/public-speaking**, branch: **pydata2017**

+++

## Other challenges

- high availability |
- performance is a key |
- updating model definition |
- kafka security (authorization, encryption) |
- features support (like exactly-once delivery) |

Note:
 - https://issues.apache.org/jira/browse/SPARK-16534 - no kafka 0.10 support in DStreams

---

# Takeaways

- streaming is challenging |
- real-time vs. micro-batching | 
- no silver bullet in pure python |

Note:
 - throw yourself into history
 - to implement and maintain
 - streamparse with storm

+++

## Thank you! Questions?

![dxc](assets/images/hiring.png)


Note:
- https://ops.fhwa.dot.gov/freewaymgmt/publications/frwy_mgmt_handbook/chapter15_01.htm#notee
- http://www.mdpi.com/1424-8220/15/10/27201/pdf "Vehicle Classification Using the Discrete Fourier Transform with Traffic Inductive Sensors"
