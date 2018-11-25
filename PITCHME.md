---?image=http://coredump.events/img/heroBG.jpg&size=cover

# @color[white](What Apache Kafka is not?)

<img src="http://coredump.events/img/coreDump-White-Full.png" width="40%" />

---?image=http://ocdn.eu/pulscms-transforms/1/AO9ktkpTURBXy8yNzc1OWY4MGEwNzU1ODUwMGUzMjBkNmZhYWYzZGFkOS5qcGeSlQLNA8AAwsOVAgDNA8DCww&size=cover

--- 

@snap[west]
## About me

Mariusz Strzelecki<br/>

Data engineer @ <img src="https://vignette.wikia.nocookie.net/central/images/b/bc/Fandom_logo.png/revision/latest?cb=20170519213035" width="30%" /><br />

4 years with Hadoop/Spark/Kafka
@snapend

@snap[east]
![](assets/images/fotka.jpg)
@snapend

Note:
33rd most visited site in the US
--- 

# Publish-subscribe

---?image=assets/images/story01.png&size=contain

@snap[south-west template-note]
Source: "Kafka: The Definitive Guide"
@snapend

Note:
example metrics:
 * number of invalid login attempts
 * mean time of request processing
 * number of server errors

---?image=assets/images/story02.png&size=contain

@snap[south-west template-note]
Source: "Kafka: The Definitive Guide"
@snapend

Note:
Use cases for metrics:
troubleshooting
dashboards
alerting
anomaly detection

We have microservices - tightly coupled

---?image=assets/images/story03.png&size=contain

@snap[south-west template-note]
Source: "Kafka: The Definitive Guide"
@snapend

---?image=assets/images/story04.png&size=contain

@snap[south-west template-note]
Source: "Kafka: The Definitive Guide"
@snapend

Note:
asynchronous/event-driven envivonment

---

# Use cases

- asynchronous, event-driven microservices communication |
- change notification/cache invalidation |
- task queue |
- Internet Of Things |

Note:
* multiplayer games
* listening to stock prices changes

IoT:
 * till 2020, 26 bilion devices communicating via Internet of other networks

---?image=assets/images/architect-254579_1920.jpg&size=cover

---

# Key features

- distributed
- fast
- reliable, durable
- easy API

---?image=assets/images/impl01.png&size=contain

---?image=assets/images/impl02.png&size=contain

---

```java
@RestController
public class EasyMessageBroker {
  private final Database db;

  @PostMapping
  public void addEvent(@RequestBody Event event) {
    db.save(event);
  }

  @GetMapping
  public Event getEvent() {
    Event event = db.findOne();
    db.delete(event);
    return event;
  }
}
```

Note:
not effective - CRUD

---?image=assets/images/impl03.png&size=contain

---

```java
@RestController
public class FileBackedMessageBroker {
  private final File file;

  @PostMapping
  public void addEvent(@RequestBody Event event) {
    file.append(event);
  }

  @GetMapping
  public Event getEvent(int offset) {
    long filePosition = offset * MSG_SIZE;
    return Event.deserialize(file, filePosition, MSG_SIZE);
  }
}
```

---?image=assets/images/impl04.png&size=contain

---?image=assets/images/impl05.png&size=contain

---?image=assets/images/impl06.png&size=contain

Note:

not usable on production

---

## What about High Availability?

- producer ✓
- broker ☹
- consumer ☹

---?image=assets/images/impl07.png&size=contain

Note:
challenge - brokers coordination, metadata exchange

---?image=assets/images/impl08.png&size=contain

---?image=assets/images/impl09.png&size=contain

---

## What about High Availability?

- producer ✓
- broker ✓
- consumer ☹

---?image=assets/images/impl10.png&size=contain

Note:
rozkładanie obciążenia

---?image=assets/images/impl11.png&size=contain

---?image=assets/images/impl12.png&size=contain

---?image=assets/images/impl13.png&size=contain

---

## What about High Availability?

- producer ✓
- broker ✓
- consumer ✓

---

## Disk space is not infinite...

---?image=assets/images/impl14.png&size=contain

Note:
similar to rollable logs from application servers

---

## "I'd like to start reading at offset 9881292"

---?image=assets/images/impl15.png&size=contain

---?image=https://kafka.apache.org/images/logo.png&size=contain

Note:

Jay Kreps: 

I thought that since Kafka was a system optimized for writing using a writer's name would make sense. I had taken a lot of lit classes in college and liked Franz Kafka. Plus the name sounded cool for an open source project. 

---

# Kafka

- doesn't cache data |
- doesn't maintain cluster configuration |
- deletes *or compacts* old segments |
- is easy to monitor and maintain |

Note:
* zero-copy!!
* integrates well with Big Data systems like Hadoop and Spark
* large variety of metrics exposed via JMX
* supports multiple storage and protocol versions sumultianiusly
* implements local requests queue |

---

## Message delivery guarantees

![hard problems](assets/images/hardproblems.png)

---

## Ordering

- only within partition |
- managed by a leader, replicated to followers |

---

## At-least-once

---?image=assets/images/atleastonce01.png&size=contain

---?image=assets/images/atleastonce02.png&size=contain

---

## At-most-once

Note:
telemetry

---?image=assets/images/atmostonce01.png&size=contain

---?image=assets/images/atmostonce02.png&size=contain

---

## Exactly-once

Note:
since 0.11

---?image=assets/images/exactlyonce01.png&size=contain

---?image=assets/images/exactlyonce02.png&size=contain

---

## Security features

- data "at rest" are stored in plain bytes (see also KIP-317) |
- TLS for brokers authentication in clients |
- TLS or Kerberos (SASL) for producers/consumers authentication in brokers |
- ACL-based authorization (for topics and consumer groups) |

---

## The Kafka Core Is Not Enough

- Schema Registry |
- Kafka Connect |
- Kafka Streams, KSQL |
- REST Proxy |

Note:
You can't miss tomorrow's session by Robin Moffatt

---

## Kafka's weak points

- no support for retries on consuming side |
- message filtering capabilities are missing |
- "pull" mode for consumers only |
- shouldn't share VM with other applications |
- no UI in the standard package |
- not the most lightweight protocol for IoT |

---

## Summary

- easy foundations → brilliant result |
- perfect scalability, high throughput |
- works well for every possible event-driven design |

Note:
skalowalność, bezpieczeństwo danych, niezawodność, wysoka wydajność

---

## How to start?

Docker: @fa[github] wurstmeister/kafka-docker

Kubernetes: @fa[github] confluentinc/cp-helm-charts

Non-virtualized: [confluent.io/download](confluent.io/download)

---

# Thank you

## Questions time!

<br/><br />
<img src="https://vignette.wikia.nocookie.net/undertale-au/images/9/9a/FANDOM_Logo.png/revision/latest/scale-to-width-down/100" width="5%" />
@size[0.75em](We're hiring! [fandom.wikia.com/careers](fandom.wikia.com/careers)) 
