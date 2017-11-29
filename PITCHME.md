# Czym nie jest Apache&nbsp;Kafka?

<img src="http://day.torun.jug.pl/wp-content/uploads/2017/03/jug5d_2.png" width="20%" />

Mariusz Strzelecki

---?image=http://ocdn.eu/pulscms-transforms/1/AO9ktkpTURBXy8yNzc1OWY4MGEwNzU1ODUwMGUzMjBkNmZhYWYzZGFkOS5qcGeSlQLNA8AAwsOVAgDNA8DCww&size=cover

--- 

# Publish-subscribe

---?image=assets/images/story01.png&size=contain

---?image=assets/images/story02.png&size=contain

---?image=assets/images/story03.png&size=contain

---?image=assets/images/story04.png&size=contain

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

---?image=assets/images/impl01.png&size=contain

---?image=assets/images/impl02.png&size=contain

---?image=assets/images/impl03.png&size=contain

---?image=assets/images/impl04.png&size=contain

---?image=assets/images/impl05.png&size=contain

---?image=assets/images/impl06.png&size=contain

---

## Wysoka dostępność (HA)

- producenci ✓
- broker ☹
- konsumenci ☹

---?image=assets/images/impl07.png&size=contain

---?image=assets/images/impl08.png&size=contain

---?image=assets/images/impl09.png&size=contain

---

## Wysoka dostępność (HA)

- producenci ✓
- brokerzy ✓
- konsumenci ☹

---?image=assets/images/impl10.png&size=contain

Note:
rozkładanie obciążenia

---?image=assets/images/impl11.png&size=contain

---?image=assets/images/impl12.png&size=contain

---?image=assets/images/impl13.png&size=contain

---

## Wysoka dostępność (HA)

- producenci ✓
- brokerzy ✓
- konsumenci ✓

---

## Dyski nie są nieskończone...

---?image=assets/images/impl14.png&size=contain

---

## "Poproszę wiadomość nr 9283723"

---?image=assets/images/impl15.png&size=contain

---?image=https://kafka.apache.org/images/logo.png&size=contain

---

# Kafka

- nie cachuje danych |
- nie przechowuje konfiguracji |
- obsługuje żądania "w swoim czasie" |
- nie tylko usuwa, ale też kompaktuje dane |

---

## Gwarancje dostarczenia wiadomości

![hard problems](assets/images/hardproblems.png)

---

## Kolejność wiadomości

- tylko w obrębie partycji |
- lider vs. replika |

---

## At-least-once

---?image=assets/images/atleastonce01.png&size=contain

---?image=assets/images/atleastonce02.png&size=contain

---

## At-most-once

---?image=assets/images/atmostonce01.png&size=contain

---?image=assets/images/atmostonce02.png&size=contain

---

## Exactly-once

---?image=assets/images/exactlyonce01.png&size=contain

---?image=assets/images/exactlyonce02.png&size=contain

---

## Bezpieczeństwo

- dane są przechowywane w sposób jawny |
- TLS szyfruje ruch i uwierzytelnia brokerów |
- TLS lub Kerberos (SASL) uwierzytelniają klientów |
- autoryzacja dostępu (do topików i grup konsumentów) |

---

## Wady

- brak wsparcia dla ponowień po stronie konsumentów |
- nie ma możliwości filtrowania wiadomości |
- brak komunikacji push do konsumentów |
- zalecane użycie dedykowanych maszyn |

---

# Podsumowanie

## O Kafce słów kilka

- proste założenia → genialny efekt |
- wysoka skalowalność |
- pasuje do niemal każdego zastosowania |

Note:
skalowalność, bezpieczeństwo danych, niezawodność, wysoka wydajność

---

## Jak zacząć?

Docker: `spotify/kafka`

Klasycznie: [confluent.io/download](confluent.io/download)

---

# Dzięki!

## Pytania?
