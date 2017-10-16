# Safer roads with kafka&python

## Prerequisites

### Kafka

The easiest way go get kafka is to use Confluent packages. Go to [official site](https://www.confluent.io/download/), use Download as `tar.gz` of OpenSource edition and unpack on local computer. Then use

    ./bin/confluent kafka start

To start zookeeper and kafka (with data storage in `/tmp/` directory)

### confluent_kafka from pip

Install from pip:

    sudo pip3 install confluent_kafka

The library required `librdkafka` installed on the system. For more information visit [confluent_kafka documentation](https://github.com/confluentinc/confluent-kafka-python#prerequisites)

### Spark

Download the newest version from the [official site](https://spark.apache.org/downloads.html) (using version Pre-built for Hadoop 2.7+).

### Winton Kafka Streams

Use pip with github link:

    sudo pip3 install git+https://github.com/wintoncode/winton-kafka-streams

Python 3.6 is required to run the library!

## Generators

Provided generators simulate inductive loop events (approx 1000/sec) and weather sensors events (one event per second).
