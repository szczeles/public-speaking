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

- weather conditions (fog, wind, rain, snow, blinding sun) |
- traffic: |
  - road occupancy |
  - vehicles speed (compared to allowed speed) |
  - gaps between vehicles and their length |
- road shape, surface quality, neighbourhood |

+++?image=https://ops.fhwa.dot.gov/freewaymgmt/publications/frwy_mgmt_handbook/images/fig15-1.jpg&size=contain

+++

# DXC

https://dgxcentre.com/using-data-analytics-to-make-roads-safer/

TODO - screenshot

+++?image=assets/images/model_building_1.png&size=cover

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
 - topics/subjects
 - multiple producers
 - partitions paradighm - multiple consumers
 - from 0.11 (newest release) transactions and exactly-once delivery - so can be used as enterprise message bus

+++?image=assets/images/model_building_4.png&size=cover

+++

# Real-time approach challenges

- induction loops events are atomic |
- streams do not look joinable |
- processing scalability |

+++

# Python kafka frameworks

- ["raw" kafka client](https://github.com/confluentinc/confluent-kafka-python)
- [Spark Streaming](https://spark.apache.org/docs/2.2.0/streaming-kafka-0-10-integration.html)
- [Winton Kafka Streams](https://github.com/wintoncode/winton-kafka-streams)

---

# 1. Merging induction loops events

[TODO - jakiś obrazek związany z mergem]

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

---

# 2. Streams join

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

# 3. Scalability

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

---

# Thank you!
## Questions?

Note:
- 
- https://ops.fhwa.dot.gov/freewaymgmt/publications/frwy_mgmt_handbook/chapter15_01.htm#notee
- http://www.cobrasoftwares.in/wp-content/uploads/2016/06/vslam-640x383.png
- https://camo.githubusercontent.com/825e165b317d2e3ace789296b2d350817f9e765e/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3837332f312a5569567048753741653878675f50766962676e4655512e6a706567
- http://www.remotemagazine.com/main/wp-content/uploads/2016/06/1-Classification.jpg
- https://i.ytimg.com/vi/0tTk9_XHQxY/maxresdefault.jpg
