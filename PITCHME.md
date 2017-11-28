# Czym nie jest Apache&nbsp;Kafka?

<img src="http://day.torun.jug.pl/wp-content/uploads/2017/03/jug5d_2.png" width="20%" />

Mariusz Strzelecki

---?image=http://ocdn.eu/pulscms-transforms/1/AO9ktkpTURBXy8yNzc1OWY4MGEwNzU1ODUwMGUzMjBkNmZhYWYzZGFkOS5qcGeSlQLNA8AAwsOVAgDNA8DCww&size=cover

--- 

# Publish-subscribe

---?image=assets/images/story01.png&size=auto

---?image=assets/images/story02.png&size=auto

---?image=assets/images/story03.png&size=auto

---?image=assets/images/story04.png&size=auto

---

# Przypadki użycia

- asynchroniczna komunikacja między mikrousługami |
- informowanie o zmianach |
- przesuwanie ciężkich zadań "w tło" |
- Internet Of Things |

Note:
gry multiplayer
reagowanie na zmiany cen akcji

---?image=http://ddarchitekci.pl/www/wp-content/uploads/blueprint-964629.jpg&size=cover

---

# Założenia

- szybko
- bezpiecznie
- proste API

---?image=assets/images/impl01.png&size=auto

---?image=assets/images/impl02.png&size=auto

---?image=assets/images/impl03.png&size=auto

---?image=assets/images/impl04.png&size=auto

---?image=assets/images/impl05.png&size=auto

---?image=assets/images/impl06.png&size=auto

---

# Wysoka dostępność (HA)

- producenci ✓
- broker ☹
- konsumenci ☹

---?image=assets/images/impl07.png&size=auto

---?image=assets/images/impl08.png&size=auto

---?image=assets/images/impl09.png&size=auto

---

# Wysoka dostępność (HA)

- producenci ✓
- brokerzy ✓
- konsumenci ☹

---?image=assets/images/impl10.png&size=auto

---?image=assets/images/impl11.png&size=auto

---?image=assets/images/impl12.png&size=auto

---?image=assets/images/impl13.png&size=auto

---

# Wysoka dostępność (HA)

- producenci ✓
- brokerzy ✓
- konsumenci ✓

---

Upraszczamy API

---



--- 

# Kafka

- nie cachuje danych |
- nie przechowuje konfigutacji |
- obsługuje żądania "w swoim czasie" |
- jest przewidywalna |
