## Apache Spark, czyli jak wycisnąć z JVMa więcej niż fabryka dała

@JDD2017

Note:
będzie generalnie o optymalizacji JVM, a Spark jako przykład

---

## O mnie

- Mariusz Strzelecki
- ![DXC](http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png)
- stackoverflow, tagi **spark** i **pyspark**

---

![Spark logo](http://blog.scottlogic.com/bjedrzejewski/assets/apache-spark-logo.png)

+++

Dlaczego Spark działa na JVM?

Note:
Hadoop jest już w Javie - zgodność z całością ekosystemy

+++

Dlaczego Spark w Scali?

Note:

* Zwięzłe, przyjazne api, podobne do LINQ
* Scala shell intepreter do eksploracji danych
* Nie Jython ani Groovy, bo Scala jest statycznie typowana, więc można zastosować więcej sztuczek wydajnośiowych
* W scali można wygodnie serializować funkcje i przesyłać je siecią
* Kiedy Spark powstawał (2009) Scala miała już 5 lat, Matei Zaharia

TODO: dodać jako listę

---

## JVM utrudnia pracę z dużymi danymi!

+++

## GC dobry dla OLTP, słaby w OLAP

+++

## Ile w JVM zajmuje napis `jdd2017`?

 - 7 bajtów?  |
 - 14 bajtów? |
 - 56 bajtów! |


```
12 | header 
 4 | char[] reference -------> 12 | header
 4 | String.hash               14 | char[] (UTF-16)
 4 | String.hash32              6 | padding
```

 - [JEP-254](http://openjdk.java.net/jeps/254) na ratunek! |


Note:
* compressed OOPS
* object's class, ID and status flags such as whether the object is currently reachable, currently synchronization-locked etc.
* w javie 9 - 48 bajtów

+++

JIT nie zawsze inline'uje metody

Note:

* inline nie działa dla długich metod i poliformizmu

---

## Projekt Tungsten

---

![PWN](assets/images/pwn_tungsten.png)

---

### cośtam cośtam

- linia 1 
- linia 2

---

### Dzięki! Pytania?
