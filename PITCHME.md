## Kafka Connect - szwajcarski scyzoryk w rękach inżyniera

---

![Video](https://player.vimeo.com/video/368358191)

---?image=assets/img/engineer1.png&size=cover

---?image=assets/img/engineer2.jpg&size=cover

---?image=assets/img/engineer3.png&size=cover

---?image=https://kafka.apache.org/images/logo.png&size=cover

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

@snap[north-east span-100 text-pink text-06]
Let your code do the talking!
@snapend

```sql zoom-18
CREATE TABLE "topic" (
    "id" serial NOT NULL PRIMARY KEY,
    "forum_id" integer NOT NULL,
    "subject" varchar(255) NOT NULL
);
ALTER TABLE "topic"
ADD CONSTRAINT forum_id
FOREIGN KEY ("forum_id")
REFERENCES "forum" ("id");
```

@snap[south span-100 text-gray text-08]
@[1-5](You can step-and-ZOOM into fenced-code blocks, source files, and Github GIST.)
@[6,7, zoom-13](Using GitPitch live code presenting with optional annotations.)
@[8-9, zoom-12](This means no more switching between your slide deck and IDE on stage.)
@snapend


---?image=assets/img/presenter.jpg

@snap[north span-100 h2-white]
## Now It's Your Turn
@snapend

@snap[south span-100 text-06]
[Click here to jump straight into the interactive feature guides in the GitPitch Docs @fa[external-link]](https://gitpitch.com/docs/getting-started/tutorial/)
@snapend

