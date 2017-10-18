## Safer roads with kafka&python

pyData Warsaw 2017

---

## About me

<ul>
<li class="fragment">Mariusz Strzelecki</li>
<li class="fragment"><img src="http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png", width="40%" /></li>
<li class="fragment">stackoverflow tags **pyspark** and **spark**</li>
</ul>

Note:
 - data ecosystem engineer, not data scientists

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

+++?image=assets/images/kafka.png

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

- [confluent kafka client](https://github.com/confluentinc/confluent-kafka-python)
- [Spark Streaming](https://spark.apache.org/docs/2.2.0/streaming-kafka-0-10-integration.html)
- [Winton Kafka Streams](https://github.com/wintoncode/winton-kafka-streams)

+++

# Confluent Kafka Client

+++

# Spark Streaming

+++

# Winton Kafka Streams

---?image=https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Two_Windows_Aarhus.jpg/1280px-Two_Windows_Aarhus.jpg&size=cover

<br/><br/><br/><br/><br/><br/><br/>
<h1 style="color: white">(double) windowing</h1>

+++?image=assets/images/double_windowing.png

+++

## Raw client

[TODO - pseudokod z poll()]

+++

## Spark Streaming

[TODO - pseudokod z windowingiem]

+++

## Kafka Streams

[TODO - pseudokod z windowingiem]

+++

## Battle results

|Challenge|Raw|Spark|Winton|
|---------|---|-----|------|
|Windowing|![BAD](http://www.iconninja.com/files/617/943/793/valid-up-positive-good-thumb-yes-ok-success-pro-accept-icon.png)|OK|OK|

---?image=assets/images/puzzle.jpg&size=cover

<h1 style="padding-left: 60%">Global state</h1>

+++

## Raw client

Nie da się :-(

+++

## Spark Streaming

[TODO - pseudokod z join]

Note:
 - https://issues.apache.org/jira/browse/SPARK-18791 - strustured steraming do not have joins

+++

## Kafka Streams

[TODO - pseudokod z join]

---?image=http://i.imgur.com/FP5GKOK.jpg&size=cover

<h1 style="color: yellow">Joining two streams</h1>
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



