# LKP3b - Graph Search Dua Kasus

Dokumentasi berikut menampilkan adjacency list, urutan ekspansi node, isi frontier pada setiap iterasi, explored, dan solusi yang ditemukan.

# Kasus 1 - Jalur Distribusi Pupuk di Jawa Tengah

## 1. Adjacency List

```text
Semarang: Kendal(20), Ungaran(15)
Kendal: Semarang(20), Batang(25)
Batang: Kendal(25), Pekalongan(30)
Ungaran: Semarang(15), Ambarawa(10), Salatiga(20)
Ambarawa: Ungaran(10), Magelang(25)
Salatiga: Ungaran(20), Boyolali(18)
Boyolali: Salatiga(18), Solo(22)
Solo: Boyolali(22), Sragen(25), DesaA(30)
Magelang: Ambarawa(25), DesaA(40)
Sragen: Solo(25), DesaA(15)
DesaA: Magelang(40), Sragen(15), Solo(30)
```

Node awal adalah **Semarang** dan tujuan adalah **DesaA**.

## 2. BFS

BFS menggunakan queue FIFO. Node paling kiri adalah node yang diproses berikutnya.

| Iterasi | Node diekspansi | Frontier setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Semarang | Kendal, Ungaran | Semarang | Tidak |
| 1 | Kendal | Ungaran, Batang | Semarang, Kendal | Tidak |
| 2 | Ungaran | Batang, Ambarawa, Salatiga | Semarang, Kendal, Ungaran | Tidak |
| 3 | Batang | Ambarawa, Salatiga, Pekalongan | ..., Batang | Tidak |
| 4 | Ambarawa | Salatiga, Pekalongan, Magelang | ..., Ambarawa | Tidak |
| 5 | Salatiga | Pekalongan, Magelang, Boyolali | ..., Salatiga | Tidak |
| 6 | Pekalongan | Magelang, Boyolali | ..., Pekalongan | Tidak |
| 7 | Magelang | Boyolali, DesaA | ..., Magelang | YA |

Solusi jalur:

```text
Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA
```

Cost: `15 + 10 + 25 + 40 = 90 KM`.

Pohon pencarian yang relevan:

```text
Semarang
├── Kendal -> Batang -> Pekalongan
└── Ungaran
	├── Ambarawa -> Magelang -> DesaA (tujuan)
	└── Salatiga -> Boyolali -> Solo
```

## 3. DFS

DFS menggunakan stack LIFO. Node paling kiri adalah bagian atas stack.

| Iterasi | Node diekspansi | Isi stack setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Semarang | Ungaran, Kendal | Semarang | Tidak |
| 1 | Ungaran | Salatiga, Ambarawa, Kendal | Semarang, Ungaran | Tidak |
| 2 | Salatiga | Boyolali, Ambarawa, Kendal | ..., Salatiga | Tidak |
| 3 | Boyolali | Solo, Ambarawa, Kendal | ..., Boyolali | Tidak |
| 4 | Solo | DesaA, Sragen, Ambarawa, Kendal | ..., Solo | Tidak |
| 5 | DesaA | - | ..., DesaA | YA |

Solusi jalur:

```text
Semarang -> Ungaran -> Salatiga -> Boyolali -> Solo -> DesaA
```

Cost: `15 + 20 + 18 + 22 + 30 = 105 KM`.

Pohon jalur DFS:

```text
Semarang
└── Ungaran
	└── Salatiga
		└── Boyolali
			└── Solo
				└── DesaA (tujuan)
```

## 4. UCS

UCS menggunakan priority queue. Format frontier adalah `node: total cost`.

| Iterasi | Node diekspansi | Priority queue setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Semarang (0) | Ungaran:15, Kendal:20 | Semarang | Tidak |
| 1 | Ungaran (15) | Kendal:20, Ambarawa:25, Salatiga:35 | ..., Ungaran | Tidak |
| 2 | Kendal (20) | Ambarawa:25, Salatiga:35, Batang:45 | ..., Kendal | Tidak |
| 3 | Ambarawa (25) | Salatiga:35, Batang:45, Magelang:50 | ..., Ambarawa | Tidak |
| 4 | Salatiga (35) | Batang:45, Magelang:50, Boyolali:53 | ..., Salatiga | Tidak |
| 5 | Batang (45) | Magelang:50, Boyolali:53, Pekalongan:75 | ..., Batang | Tidak |
| 6 | Magelang (50) | Boyolali:53, Pekalongan:75, DesaA:90 | ..., Magelang | Tidak |
| 7 | DesaA (90) | - | ..., DesaA | YA |

Solusi jalur UCS:

```text
Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA
```

Total cost minimum: `90 KM`.

## 5. Ringkasan Kasus 1

| Metode | Jalur | Cost |
|---|---|---:|
| BFS | Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA | 90 KM |
| DFS | Semarang -> Ungaran -> Salatiga -> Boyolali -> Solo -> DesaA | 105 KM |
| UCS | Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA | 90 KM |

---

# Kasus 2 - Rute Kapal di Sulawesi Selatan

## 1. Adjacency List

```text
Makassar: ParePare(5), Jeneponto(4)
ParePare: Makassar(5), Palopo(7)
Palopo: ParePare(7), Kolaka(6)
Jeneponto: Makassar(4), Bira(3)
Bira: Jeneponto(3), Kendari(8)
Kolaka: Palopo(6), Kendari(5)
Kendari: Kolaka(5), Bira(8), BauBau(6)
BauBau: Kendari(6), PasarB(4)
PasarB: BauBau(4)
```

Node awal adalah **Makassar** dan tujuan adalah **PasarB**.

## 2. BFS

| Iterasi | Node diekspansi | Frontier setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Makassar | ParePare, Jeneponto | Makassar | Tidak |
| 1 | ParePare | Jeneponto, Palopo | Makassar, ParePare | Tidak |
| 2 | Jeneponto | Palopo, Bira | ..., Jeneponto | Tidak |
| 3 | Palopo | Bira, Kolaka | ..., Palopo | Tidak |
| 4 | Bira | Kolaka, Kendari | ..., Bira | Tidak |
| 5 | Kolaka | Kendari | ..., Kolaka | Tidak |
| 6 | Kendari | BauBau | ..., Kendari | Tidak |
| 7 | BauBau | PasarB | ..., BauBau | Tidak |
| 8 | PasarB | - | ..., PasarB | YA |

Solusi jalur:

```text
Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB
```

Cost: `4 + 3 + 8 + 6 + 4 = 25 jam`.

## 3. DFS

| Iterasi | Node diekspansi | Isi stack setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Makassar | Jeneponto, ParePare | Makassar | Tidak |
| 1 | Jeneponto | Bira, ParePare | Makassar, Jeneponto | Tidak |
| 2 | Bira | Kendari, ParePare | ..., Bira | Tidak |
| 3 | Kendari | BauBau, Kolaka, ParePare | ..., Kendari | Tidak |
| 4 | BauBau | PasarB, Kolaka, ParePare | ..., BauBau | Tidak |
| 5 | PasarB | - | ..., PasarB | YA |

Solusi jalur:

```text
Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB
```

Cost: `4 + 3 + 8 + 6 + 4 = 25 jam`.

## 4. UCS

| Iterasi | Node diekspansi | Priority queue setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Makassar (0) | Jeneponto:4, ParePare:5 | Makassar | Tidak |
| 1 | Jeneponto (4) | ParePare:5, Bira:7 | ..., Jeneponto | Tidak |
| 2 | ParePare (5) | Bira:7, Palopo:12 | ..., ParePare | Tidak |
| 3 | Bira (7) | Palopo:12, Kendari:15 | ..., Bira | Tidak |
| 4 | Palopo (12) | Kendari:15, Kolaka:18 | ..., Palopo | Tidak |
| 5 | Kendari (15) | Kolaka:18, BauBau:21 | ..., Kendari | Tidak |
| 6 | Kolaka (18) | BauBau:21 | ..., Kolaka | Tidak |
| 7 | BauBau (21) | PasarB:25 | ..., BauBau | Tidak |
| 8 | PasarB (25) | - | ..., PasarB | YA |

Solusi jalur:

```text
Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB
```

Total cost minimum: `25 jam`.

## 5. Ringkasan Kasus 2

| Metode | Jalur | Cost |
|---|---|---:|
| BFS | Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB | 25 jam |
| DFS | Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB | 25 jam |
| UCS | Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB | 25 jam |

---

# Kesimpulan

- BFS memakai queue FIFO dan memeriksa node berdasarkan tingkat kedalaman.
- DFS memakai stack LIFO dan menyusuri satu cabang sedalam mungkin.
- UCS memakai priority queue dan memilih total cost terkecil.
- Pada Kasus 1, BFS dan UCS menghasilkan 90 KM, sedangkan DFS menghasilkan 105 KM.
- Pada Kasus 2, ketiga metode menghasilkan jalur yang sama dengan cost 25 jam.
