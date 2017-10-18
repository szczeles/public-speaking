# Safer roads with kafka&python

pyData Warsaw 2017

---

# About me

<ul>
<li class="fragment">Mariusz Strzelecki</li>
<li class="fragment"><img src="http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png", width="40%" /></li>
<li class="fragment">stackoverflow tags **pyspark** and **spark**</li>
</ul>

Note:
 - data ecosystem engineer, not data scientist

---?image=https://img00.deviantart.net/b90d/i/2009/314/9/f/welcome_to_accident_by_howardtj43147.jpg&size=cover

+++

## Read safety "features"

- weather conditions (fog, wind, rain, snow, sun) |
- traffic: |
  - road occupancy |
  - vehicles speed (compared to allowed speed) |
  - gaps between vehicles and their length |
- road shape, surface quality, neighbourhood |
- calendar: day of week, national holiday |

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

+++?image=https://i.imgur.com/KkUB0dL.jpg&size=contain

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

- real-time grouping induction loops events (windowing) |
- handling global state of current weather |
- joining two streams of events |

---

# Kafka meets python

+++

# Frameworks

- [Confluent Kafka Client](https://github.com/confluentinc/confluent-kafka-python)
- [Spark Streaming](https://spark.apache.org/docs/2.2.0/streaming-kafka-0-10-integration.html)
- [Winton Kafka Streams](https://github.com/wintoncode/winton-kafka-streams)

+++

## Confluent Kafka Client

```python
consumer = Consumer({'metadata.broker.list': ...})
consumer.subscribe([car_events_topic])

while True:
    msg = consumer.poll()
    if msg.topic() == car_events_topic:
        process_data(msg.value())
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
inductive_loop_events = KafkaUtils.createDirectStream(
   ssc, [car_events_topic], ...)

cars_stats = get_window(inductive_loop_events, 10) \
  .join(get_window(inductive_loop_events, 1)) \
  .map(...)

cars_stats.pprint()
```
@[1-2]
@[3-4]
@[6-8]
@[10]

+++

## Winton Kafka Streams

```python
topology_builder \
    .source('loop-event-json', [car_events_topic]) \
    .processor('loop-event', ReadJson, 'loop-event-json') \
    .processor('loops-windows', ProcessEvent, 'loop-event') \
    .processor('stats', CalculateStats, 'loops-windows') \
    .processor('results', ApplyMLModel, 'stats')

kafka_streams.KafkaStreams(topology_builder, kafka_config)\
    .start()
```
@[1-6]
@[8-9]

---?image=https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Two_Windows_Aarhus.jpg/1280px-Two_Windows_Aarhus.jpg&size=cover

<br/><br/><br/><br/><br/><br/><br/><br/>
<h1 style="color: white">(double) windowing</h1>

+++?image=assets/images/double_windowing.png

+++

## Raw client

```python
class LoopEventsWindows:
    def loop_event(self, event):
        self.deque.append(event)

    def get_windows(self):
        current_time = time.time()
        data = pd.DataFrame(list(self.deque))
        ts_field = data[self.timestamp_field]
        return { 
            str(window): data[
                (ts_field >= current_time - window) & 
                (ts_field <= current_time)
            ] for window in self.windows }
```

+++

## Spark Streaming

```python
def get_window(length):
    return inductive_loop_events.window(length * 60, 60) \
        .map(map_record).reduceByKey(get_stats) \
        .map(lambda r: map_stats(r, str(length)))

get_window(long_window).join(get_window(short_window))
```

Note:
 - https://issues.apache.org/jira/browse/SPARK-18791 - strustured steraming do not have joins
+++

## Kafka Streams

```python
class ProcessLoopEvent(BaseProcessor):
    def initialise(self, name, context):
        self.context.schedule(short_window * 60)
        
    def punctuate(self, timestamp):
        short_window_data = self.datastore[-1]
        long_window_data = join_last_10_windows()
        self.context.forward(None, 
            json.dumps((short_window_data, long_window_data)))
        self.datastore.append([])
    
    def process(self, key, value):
        self.datastore[-1].append(value)
```

---?image=assets/images/puzzle.jpg&size=cover

<h1 style="padding-left: 60%">Global state</h1>

+++

## Raw client

```python
class WeatherState:
    def __init__(self):
        self.state = {}
        
    def update(self, key, value):
        self.state[key] = value
        
    def get_current_data(self):
        return pd.DataFrame(list(self.state.values())) \
            .set_index('station')
        
weather_state = WeatherState()

while True:
    msg = consumer.poll()
    if msg.topic() == weather_topic:
        weather_state.update(msg.key(), msg.value())
```

+++

## Spark Streaming

```python
def update_function(new_values, last_state):
    if len(new_values) == 0:
        return last_state
    return new_values[0]

weather_information.updateStateByKey(update_function)
```

+++

## Kafka Streams

```python
class UpdateState(BaseProcessor):
    def initialise(self, name, context):
        self.store = context.get_store('weather_store')
    
    def process(self, key, value):
        self.store.update_weather(key.decode('ascii'), value)

topology_builder \
    ... \
    .processor('weather', UpdateState, 'weather-event') \
    .processor('stats', CalculateStatsAndJoin, 'loops-windows')
    .state_store('weather_store', WeatherStore, 'weather', 'stats')
```

---?image=http://i.imgur.com/FP5GKOK.jpg&size=cover

<h1 style="color: red">Joining two streams</h1>
<br/><br/> <br/><br/> <br/><br/> <br/><br/>

+++

## Raw client

Nie da się :-(

+++

## Spark Streaming

[TODO - pseudokod z join]

+++

## Kafka Streams

[TODO - pseudokod z join]

---

## Other challenges

- Kafka security (authorization, encryption)
- Model upgrade
- HA
- Performance

---

# Summary

* TODO
* TODO2

+++

## Thank you! Questions?

![dxc](assets/images/hiring.png)


Note:
- 
- https://ops.fhwa.dot.gov/freewaymgmt/publications/frwy_mgmt_handbook/chapter15_01.htm#notee
- http://www.cobrasoftwares.in/wp-content/uploads/2016/06/vslam-640x383.png
- https://camo.githubusercontent.com/825e165b317d2e3ace789296b2d350817f9e765e/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3837332f312a5569567048753741653878675f50766962676e4655512e6a706567
- http://www.remotemagazine.com/main/wp-content/uploads/2016/06/1-Classification.jpg
- https://i.ytimg.com/vi/0tTk9_XHQxY/maxresdefault.jpg
- http://www.mdpi.com/1424-8220/15/10/27201/pdf "Vehicle Classification Using the Discrete Fourier Transform with Traffic Inductive Sensors"


Spark:

 - https://issues.apache.org/jira/browse/SPARK-16534 - no kafka 0.10 support in DStreams

|framework                  | stream joins | security  |
|---------------------------|--------------|-----------|
|Spark Streaming            | YES          | NO        |
|Spark Structured Streaming | NO           | SSL       |
|Raw client                 | NO           | SSL, SASL |




+++

## Battle results

|Challenge|Raw|Spark|Winton|
|---------|---|-----|------|
|Windowing|![BAD](http://www.iconninja.com/files/617/943/793/valid-up-positive-good-thumb-yes-ok-success-pro-accept-icon.png)|OK|OK|
