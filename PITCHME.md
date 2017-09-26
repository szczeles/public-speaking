## Apache Spark, czyli jak wycisnąć z JVMa więcej niż fabryka dała

@JDD2017

Note:
będzie generalnie o optymalizacji JVM, a Spark jako przykład

---

## O mnie

<ul>
<li class="fragment">Mariusz Strzelecki</li>
<li class="fragment"><img src="http://day.torun.jug.pl/wp-content/uploads/2017/03/jug5d_2.png" width="20%" /></li>
<li class="fragment"><img src="http://assets1.dxc.technology/newsroom/images/dxc_logo_hz_blk_rgb_300.png", width="40%" /></li>
<li class="fragment">stackoverflow: **spark** i **pyspark**</li>
</ul>

---

![Spark logo](http://blog.scottlogic.com/bjedrzejewski/assets/apache-spark-logo.png)

+++

## Dlaczego Spark jest napisany w Scali?

- 2009: Scala świętuje 5. urodziny |
- zwięzłe, przyjazne api |
- interpreter |
- statyczne typowanie |
- serializacja funkcji |

Note:
- Hadoop jest już w Javie - zgodność z całością ekosystemu
- Matei Zaharia
- Zwięzłe, przyjazne api, podobne do LINQ
- Scala shell intepreter do eksploracji danych
- Nie Jython ani Groovy, bo Scala jest statycznie typowana, więc można zastosować więcej sztuczek wydajnośiowych
- W scali można wygodnie serializować funkcje i przesyłać je siecią

+++

## OLTP vs. OLAP

- narzuty pamięci |
- duża ilość referencji |
- GC |

Note:

- Boxing zmiennych - przykład z jdd2017
- Sortowanie -> słabe układy pamięci / Serializacja - wymaga skakania po pamięci 
- Garbage collector na niemutowalnych danych

+++

## Ile pamięci zajmują napisy?

 -  `"jdd2017"`
 - 8 bajtów?  |
 - 16 bajtów? |
 - 56 bajtów! |

Note:
- compressed OOPS

+++

```
 	new String("jdd2017")

    12 | header 
     4 | char[] reference -------> 12 | header
     4 | String.hash               14 | char[] (UTF-16)
     4 | String.hash32              6 | padding
```

 - [JEP-254](http://openjdk.java.net/jeps/254) na ratunek!


Note:
- object's class, ID and status flags such as whether the object is currently reachable, currently synchronization-locked etc.
- w javie 9 - 48 bajtów

+++

## java.util.HashMap

Note:
- nie grzeszy wydajnością
- sortowanie

+++?image=assets/images/java_hashmap.png&size=auto

---

## 2015: Projekt Tungsten

+++?image=http://periodictable.com/Samples/074.68/s12s.JPG&size=auto

+++

![PWN](assets/images/pwn_tungsten.png)

+++

## Ostatnie 7 lat sparka:


|         | 2010          | 2015           |
| ------- |:-------------:|:--------------:|
| Dysk    | 50 MB/s (HDD) | 500 MB/s (SSD) |
| Sieć    | 1 GBps        | 10 GBps        |
| CPU     | ~3 GHz        | ~3 GHz         |

Note:
- IO w sparku i tak zostało zoptymalizowane 
- Pojawiły się kolumnowe formaty danych
- CPU wciąż jest wąskim gardłem, taki jest też spodziewany trend
- rola CPU w przetwarzaniu: serializacja, hashowanie, kompresja

---

## Pamieć

+++

## UTF8String 

byte[] + ilość elementów

Note:
- 50% oszczędności RAM
- wady - w UDFach trzeba transformować na String i w drugą stronę	

+++

## sun.misc.Unsafe

Note:
- niskopoziomowe zarządzanie, m.in. pamiecią
- jawna alokacja/zwalnianie pamięci
- implementacja mocno zależy od platformy!

+++

## UnsafeRow

```
+-------------------------------------------------------+
| null bits | primitive values | variable-length values |
+-------------------------------------------------------+

{
	"konferencja: "jdd",                +-------|
	"miasto": "Kraków"    +----+--------|-------v--------------------+
	"rok": 2017    -----> | 00 | 2017 | 4 | 6 | 3 | jdd | 6 | Kraków |	
}                         +----+------------|-------------^----------+
                                            +-------------|
``` 

- wydajne (pamięciowo) przechowywanie danych |
- serializacja | 
- trywialne porównywanie |
- spilling |

Note:
 * wydajne pamięciowo przechowwyanie danych
 * serializacja: unikanie niepotrzebnych skoków po referencjach
 * equals() to porównwanie bajtów
 * proste obliczanie rozmiaru danych (ułatwia spilling na dysk), wcześniej heurystyki i aproksymacje

+++?image=assets/images/spark_unsafe.png&size=auto

+++ 

## TaskMemoryManager

- obsługi wirtualnej adresacji stron
  - Off-heap: `java.nio.DirectByteBuffer` z "podstawionym buforem"
  - On-heap: jako `long[]`

Note:
- unikanie złych praktyk ze skakaniem po pamięci
- pozbywanie się nadmiernego GC
- w on-heap java może dowolnie przenosić strony, potrzebna tablica stron

+++



+++


- BytesToBytesMap -> wydajne przeszukiwanie


+++


## JIT nie zawsze inline'uje metody

Note:

* inline nie działa dla długich metod i poliformizmu
* boxing wszystkich obiektów

## Sortowanie

```
 4b          4b
--------------------               ------
|key-prefix|pointer| ------------> |data|
--------------------               ------
```


---

## Projekt Tungsten, faza 2



- generowanie kodu
- optymalizacja użycia cache CPU

- Volcano -> generowanie kodu
- wektoryzacja

+++

## Volcano vs student

Volcano: 13.95 mln rekordów/sec
Kod: 125 mln rekordów/sec

| Volcano                 | kod studenta                     |
|-------------------------|----------------------------------|
|wiele wirtualnych funkcji| 0 funkcji                        |
|dane w pamieci/cache     | dane w cache CPU                 |
| ---                     | loop unrolling, SIMD, pipelining |

+++

## Whole-stage codegen [SPARK-12795](https://issues.apache.org/jira/browse/SPARK-12795)

Wyszukaj operacje następujące po sobie i włóż do jednej funkcji

- Nie da zastosować dla zewnętrznych bibliotek (UDFy, python, R)
- Skomplikowane IO i tak wymaga wywołań funkcji

+++

## Wektoryzacja

Przechowywanie danych w kolumnach, nie wierszowo.

+++

## Przykład

```
df.where(df.conference == "jdd2017").count()
```

![arrow](https://raw.githubusercontent.com/gitpitch/code-presenting/master/assets/down-arrow.png)

+++

```java
private void agg_doAggregateWithoutKey() throws java.io.IOException {
  // initialize aggregation buffer
  agg_bufIsNull = false;
  agg_bufValue = 0L;

  while (inputadapter_input.hasNext()) {
    InternalRow inputadapter_row = (InternalRow) inputadapter_input.next();
    boolean inputadapter_isNull = inputadapter_row.isNullAt(0);
    UTF8String inputadapter_value = inputadapter_isNull ? null : (inputadapter_row.getUTF8String(0));

    if (!(!(inputadapter_isNull))) continue;

    boolean filter_isNull2 = false;

    Object filter_obj = ((Expression) references[1]).eval(null);
    UTF8String filter_value4 = (UTF8String) filter_obj;
    boolean filter_value2 = false;
    filter_value2 = inputadapter_value.equals(filter_value4);
    if (!filter_value2) continue;

    filter_numOutputRows.add(1);

    // do aggregate
    // common sub-expressions

    // evaluate aggregate function
    boolean agg_isNull1 = false;

    long agg_value1 = -1L;
    agg_value1 = agg_bufValue + 1L;
    // update aggregation buffer
    agg_bufIsNull = false;
    agg_bufValue = agg_value1;
    if (shouldStop()) return;
  }
}
```

@[15-19](filtrowanie)
@[30-33	](zliczanie)

+++

![arrow](https://raw.githubusercontent.com/gitpitch/code-presenting/master/assets/down-arrow.png)

[Janino](http://janino-compiler.github.io/janino/)

Note:
janino wspiera kod zgodny z Javą 1.7 (z wyjątkami)

+++

## Czy naprawdę warto?

|                      | OFF    | ON      |
|----------------------|--------|---------|
|filter                | 15 ns  | 1.1 ns  |
|sum w/o group         | 14 ns  | 0.9 ns  |
|sum w/ group          | 79 ns  | 10.7 ns |
|hash join             | 115 ns | 4.0 ns  |
|sort (8 bit entropy)  | 620 ns	| 5.3 ns  |
| sort (64 bit entropy)| 620 ns | 40 ns   |
|sort-merge join	   | 750 ns | 700 ns  |

---

### Dzięki! Pytania?

Note:
- [Flame graphs](https://db-blog.web.cern.ch/blog/luca-canali/2016-09-spark-20-performance-improvements-investigated-flame-graphs)
- https://www.slideshare.net/databricks/spark-performance-whats-next
- [Statystyki operacji po wholestagecodegen](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/6122906529858466/293651311471490/5382278320999420/latest.html)
- [Wektoryzacja, loop unrolling](https://spoddutur.github.io/spark-notes/second_generation_tungsten_engine.html)
- [Advanced meetup slajdy](https://www.slideshare.net/cfregly/advanced-apache-spark-meetup-project-tungsten-nov-12-2015)
- [Prezka databricksa](https://www.youtube.com/watch?v=5ajs8EIPWGI&t=335s)
- https://databricks.com/blog/2016/05/23/apache-spark-as-a-compiler-joining-a-billion-rows-per-second-on-a-laptop.html
- https://databricks.com/blog/2015/04/28/project-tungsten-bringing-spark-closer-to-bare-metal.html
