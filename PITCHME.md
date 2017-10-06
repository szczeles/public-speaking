## Safer roads with kafka&python

pyData Warsaw 2017

---

## About me

<ul>
<li class="fragment">Mariusz Strzelecki</li>
<li class="fragment"><img src="http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png", width="40%" /></li>
<li class="fragment">stackoverflow task **pyspark** and **spark**</li>
</ul>

Note:
 - data ecosystem engineer, not data scientists

---

# Streaming 

Note:
 - Nowadays data are coming in streaming-way
 - IoT (sensors, cars) will not wait off-line data
 - Events - search events from users should have instant impact on what we deliver to users

---

# Apache Kafka

Note:
 - distributed log/journal
 - 2011
 - topics/subjects
 - multiple producers
 - partitions paradighm - multiple consumers
 - from 0.11 (newest release) transactions and exactly-once delivery - so can be used as enterprise message bus

---

# Python frameworks

- raw client
- spark streaming
- winton kafka sterams

---

# Simplest approach TODO-IMG (Section)

One event arrives:
- all data are in place
- we have numeric values (not video/images)
- model is final

## All frameworks work fine :-)

---

# Not all data in place TODO-IMG (Section)

For some properties need to:
- join with other stream
- join using REST API calls/databases/off-line data

Note:
 - temperature + wind
 - is driver safe

---

# Video data TODO-IMG (Section)

- grab only latest frame
- grab all frames and process in parallel way

---

# Model upgrade TODO-IMG (Section)

 - deploy new model without loosing data
 - push pointer to the past

---

# Thank you!
## Questions?