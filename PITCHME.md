## Kafka Connect - szwajcarski scyzoryk w rękach inżyniera

---

![Video](https://player.vimeo.com/video/368358191)

---?image=assets/img/engineer1.png&size=cover

---?image=assets/img/engineer2.jpg&size=cover

---?image=assets/img/engineer3.png&size=cover

---?image=https://kafka.apache.org/images/logo.png&size=contain

---

## Kafka

![IMAGE](https://szczeles.github.io/images/Kafka.svg)

---

## + Schema Registry

![IMAGE](https://szczeles.github.io/images/Kafka_SR.svg)

---

## + Kafka Streams API

![IMAGE](https://szczeles.github.io/images/Kafka_SR_Streams.svg)

---

## + REST Proxy

![IMAGE](https://szczeles.github.io/images/Kafka_SR_Streams_Rest.svg)

---

# Kafka Connect

---

![IMAGE](https://szczeles.github.io/images/Kafka_Connect.svg)

---

## Kafka Connect

@ul
- rozszerzanie przez wtyczki (dostarczane jako JARy)
- bestanowość
- gwarancje dostarczenia zależne od implementacji
@ulend

---

## Architekt wraca z konferencji...

## "Migrujemy na Postgresa 12"

---

```java
class UserRepository {
    private MySQL mysql;

    ...

    public void save(User user) {
        this.mysql.persist(user);
    }
}
```

---

```java
class UserRepository {
    private MySQL mysql;
    private PostgreSQL postgres;

    ...

    public void save(User user) {
        this.mysql.persist(user);
        this.postgres.persist(user);
    }
}
```
@snap[south span-100 text-gray text-08]
@[3]
@[9]
@[1-11]
@snapend

---

## Wyglada OK, ale...

@ul
- jak przenieść aktualny stan bazy?
- co jeśli Postgres jest niedostępny?
- co z RODO?
@ulend

---

![IMAGE](https://szczeles.github.io/images/App_Sync.svg)

---

![IMAGE](https://szczeles.github.io/images/App_Sync_Kafka.svg)

---

# Dzięki!

## Pytania?

@fa[github] **szczeles/kafkaconnect-demo**
