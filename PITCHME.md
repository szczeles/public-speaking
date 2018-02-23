# Czy chodziło Ci o... ?

<img src="http://day.torun.jug.pl/wp-content/uploads/2017/03/jug5d_2.png" width="20%" />

Mariusz Strzelecki

---

# Rekomendacje dla wyszukiwarki

---

![literowka](images/literowka.png)

---

![podobne](images/podobne.png)

---

![Spark logo](http://blog.scottlogic.com/bjedrzejewski/assets/apache-spark-logo.png)

---

# Środowisko

- Spark (scala/python)
- Notatniki 
- Databricks (6.5GB RAM, 8 CPU?)

---

# Dane

- [Logi wyszukiwarki AOL](http://www.cim.mcgill.ca/~dudek/206/Logs/AOL-user-ct-collection/U500k_README.txt)
- Leżą na S3 (https://pastebin.com/LbwRGBUv)

```
$ s3cmd ls s3://torun-jug-spark/aol-search-logs/ | cut -d' ' -f3-
        0   s3://torun-jug-spark/aol-search-logs/
 44961123   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-01.txt.gz
 45909232   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-02.txt.gz
 46632841   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-03.txt.gz
 46236686   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-04.txt.gz
 48205554   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-05.txt.gz
 44916910   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-06.txt.gz
 46175060   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-07.txt.gz
 45663522   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-08.txt.gz
 45826468   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-09.txt.gz
 45734730   s3://torun-jug-spark/aol-search-logs/user-ct-test-collection-10.txt.gz

```

---
