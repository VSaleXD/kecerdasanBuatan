 # LKP3a - Graph Search Jawa Barat

## 1. Adjacency List

```text
Bekasi: Bogor(10), Karawang(10)
Bogor: Bekasi(10), Sukabumi(15), Cianjur(8)
Sukabumi: Bogor(15), Cianjur(15)
Karawang: Bekasi(10), Subang(8), Purwakarta(8)
Purwakarta: Karawang(8), Subang(8), Cianjur(8)
Subang: Karawang(8), Purwakarta(8), Indramayu(10), Sumedang(10)
Cianjur: Bogor(8), Sukabumi(15), Bandung(8), WestBandung(8)
WestBandung: Cianjur(8), Bandung(5)
Bandung: WestBandung(5), Sumedang(10), Garut(8), Cianjur(8)
Sumedang: Subang(10), Bandung(10), Majalengka(5)
Indramayu: Subang(10), Cirebon(8)
Majalengka: Sumedang(5), Kuningan(10)
Cirebon: Indramayu(8), Kuningan(8)
Kuningan: Cirebon(8), Majalengka(10), Ciamis(8)
Garut: Bandung(8), Tasikmalaya(8)
Tasikmalaya: Garut(8), Ciamis(5), Pangandaran(8)
Ciamis: Kuningan(8), Tasikmalaya(5), Pangandaran(5)
Pangandaran: Tasikmalaya(8), Ciamis(5)
```

Node awal adalah **Bogor** dan tujuan adalah **Pangandaran**.

## 2. BFS

BFS menggunakan queue FIFO. Node paling kiri adalah node yang diproses lebih dahulu.

| Iterasi | Node diekspansi | Frontier setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Bogor | Bekasi, Sukabumi, Cianjur | Bogor | Tidak |
| 1 | Bekasi | Sukabumi, Cianjur, Karawang | Bogor, Bekasi | Tidak |
| 2 | Sukabumi | Cianjur, Karawang | Bogor, Bekasi, Sukabumi | Tidak |
| 3 | Cianjur | Karawang, Bandung, WestBandung | Bogor, Bekasi, Sukabumi, Cianjur | Tidak |
| 4 | Karawang | Bandung, WestBandung, Subang, Purwakarta | Bogor, Bekasi, Sukabumi, Cianjur, Karawang | Tidak |
| 5 | Bandung | WestBandung, Subang, Purwakarta, Sumedang, Garut | ..., Karawang, Bandung | Tidak |
| 6 | WestBandung | Subang, Purwakarta, Sumedang, Garut | ..., Bandung, WestBandung | Tidak |
| 7 | Subang | Purwakarta, Sumedang, Garut, Indramayu | ..., WestBandung, Subang | Tidak |
| 8 | Purwakarta | Sumedang, Garut, Indramayu | ..., Subang, Purwakarta | Tidak |
| 9 | Sumedang | Garut, Indramayu, Majalengka | ..., Purwakarta, Sumedang | Tidak |
| 10 | Garut | Indramayu, Majalengka, Tasikmalaya | ..., Sumedang, Garut | Tidak |
| 11 | Tasikmalaya | Indramayu, Majalengka, Pangandaran | ..., Garut, Tasikmalaya | YA |

Solusi jalur:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

Cost jalur: `8 + 8 + 8 + 8 + 8 = 40`.

## 3. DFS

DFS menggunakan stack LIFO. Node paling kiri adalah bagian atas stack.

| Iterasi | Node diekspansi | Isi stack setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Bogor | Cianjur, Sukabumi, Bekasi | Bogor | Tidak |
| 1 | Cianjur | Purwakarta, WestBandung, Bandung, Sukabumi, Bekasi | Bogor, Cianjur | Tidak |
| 2 | Purwakarta | Subang, WestBandung, Bandung, Sukabumi, Bekasi | ..., Purwakarta | Tidak |
| 3 | Subang | Sumedang, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi | ..., Subang | Tidak |
| 4 | Sumedang | Majalengka, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi | ..., Sumedang | Tidak |
| 5 | Majalengka | Kuningan, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi | ..., Majalengka | Tidak |
| 6 | Kuningan | Ciamis, Cirebon, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi | ..., Kuningan | Tidak |
| 7 | Ciamis | Pangandaran, Tasikmalaya, Cirebon, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi | ..., Ciamis | Tidak |
| 8 | Pangandaran | - | ..., Pangandaran | YA |

Solusi jalur:

```text
Bogor -> Cianjur -> Purwakarta -> Subang -> Sumedang -> Majalengka
-> Kuningan -> Ciamis -> Pangandaran
```

Cost jalur: `8 + 8 + 8 + 10 + 5 + 10 + 8 + 5 = 62`.

## 4. UCS

UCS menggunakan priority queue. Format frontier adalah `node: total cost`, dan node dengan cost terkecil diproses lebih dahulu.

| Iterasi | Node diekspansi | Priority queue setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Bogor (0) | Cianjur:8, Bekasi:10, Sukabumi:15 | Bogor | Tidak |
| 1 | Cianjur (8) | Bekasi:10, Sukabumi:15, Bandung:16, WestBandung:16, Purwakarta:16 | Bogor, Cianjur | Tidak |
| 2 | Bekasi (10) | Sukabumi:15, Bandung:16, WestBandung:16, Purwakarta:16, Karawang:20 | ..., Bekasi | Tidak |
| 3 | Sukabumi (15) | Bandung:16, WestBandung:16, Purwakarta:16, Karawang:20 | ..., Sukabumi | Tidak |
| 4 | Bandung (16) | WestBandung:16, Purwakarta:16, Garut:24, Karawang:20, Sumedang:26 | ..., Bandung | Tidak |
| 5 | WestBandung (16) | Purwakarta:16, Karawang:20, Garut:24, Sumedang:26 | ..., WestBandung | Tidak |
| 6 | Purwakarta (16) | Karawang:20, Garut:24, Subang:24, Sumedang:26 | ..., Purwakarta | Tidak |
| 7 | Karawang (20) | Garut:24, Subang:24, Sumedang:26 | ..., Karawang | Tidak |
| 8 | Garut (24) | Subang:24, Sumedang:26, Tasikmalaya:32 | ..., Garut | Tidak |
| 9 | Subang (24) | Sumedang:26, Tasikmalaya:32, Indramayu:34 | ..., Subang | Tidak |
| 10 | Sumedang (26) | Majalengka:31, Tasikmalaya:32, Indramayu:34 | ..., Sumedang | Tidak |
| 11 | Tasikmalaya (32) | Majalengka:31, Indramayu:34, Ciamis:37, Pangandaran:40 | ..., Tasikmalaya | Tidak |
| 12 | Majalengka (31) | Indramayu:34, Ciamis:37, Pangandaran:40, Kuningan:41 | ..., Majalengka | Tidak |
| 13 | Indramayu (34) | Ciamis:37, Pangandaran:40, Cirebon:42 | ..., Indramayu | Tidak |
| 14 | Ciamis (37) | Pangandaran:40, Cirebon:42, Kuningan:41 | ..., Ciamis | Tidak |
| 15 | Pangandaran (40) | - | ..., Pangandaran | YA |

Solusi jalur UCS:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

Total cost minimum: `40`.

## 5. Ringkasan

| Metode | Jalur | Cost |
|---|---|---:|
| BFS | Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran | 40 |
| DFS | Bogor -> Cianjur -> Purwakarta -> Subang -> Sumedang -> Majalengka -> Kuningan -> Ciamis -> Pangandaran | 62 |
| UCS | Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran | 40 |
