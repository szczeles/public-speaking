## Apache Spark, czyli jak wycisnąć z JVMa więcej niż fabryka dała

@JDD2017

Note:
będzie generalnie o optymalizacji JVM, a Spark jako przykład

---

## O mnie

- Mariusz Strzelecki
- ![DXC](http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png)
- stackoverflow, tagi `spark` i `pyspark`

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
 * Kiedy Spark powstawał (2009) Scala miała już 5 lat

---

### cośtam cośtam

- linia 1 
- linia 2

---

### Dzięki! Pytania?
