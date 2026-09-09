# Pengerjaan Graph Search LKP3b

Dokumen ini menjelaskan cara kerja BFS, DFS, dan UCS pada dua kasus:

1. Jalur distribusi pupuk di Jawa Tengah
2. Rute kapal di Sulawesi Selatan

Pada kedua kasus, pencarian dimulai dari kota awal dan berhenti ketika kota tujuan ditemukan.

---

# Kasus 1: Jalur Distribusi Pupuk di Jawa Tengah

## 1. Data Masalah

- Titik awal: **Semarang**
- Tujuan: **DesaA**
- Satuan biaya: **KM**
- Jalan bersifat dua arah karena graph menggunakan `directed=False`.

---

## 2. Breadth-First Search (BFS)

### Cara kerja

BFS menggunakan **queue** dengan aturan FIFO (*First In, First Out*). Kota yang masuk lebih dahulu akan diproses lebih dahulu. BFS mencari berdasarkan tingkat kedalaman, bukan berdasarkan jarak.

Kota yang sudah ditemukan tidak dimasukkan kembali ke queue agar pencarian tidak berputar pada jalan yang sama.

### Simulasi queue

Kota paling kiri adalah kota yang akan diproses berikutnya.

| Langkah | Kota yang diproses | Isi queue setelah tetangga ditambahkan |
|---:|---|---|
| 0 | - | Semarang |
| 1 | Semarang | Kendal, Ungaran |
| 2 | Kendal | Ungaran, Batang |
| 3 | Ungaran | Batang, Ambarawa, Salatiga |
| 4 | Batang | Ambarawa, Salatiga, Pekalongan |
| 5 | Ambarawa | Salatiga, Pekalongan, Magelang |
| 6 | Magelang | Salatiga, Pekalongan, DesaA ditemukan |

Ketika Magelang diperiksa, DesaA ditemukan melalui jalur:

```text
Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA
```

### Perhitungan cost

```text
Semarang -> Ungaran       = 15 KM
Ungaran -> Ambarawa       = 10 KM
Ambarawa -> Magelang      = 25 KM
Magelang -> DesaA         = 40 KM

Total = 15 + 10 + 25 + 40 = 90 KM
```

### Pohon pencarian BFS

```text
Semarang
├── Kendal
│   └── Batang
│       └── Pekalongan
└── Ungaran
    ├── Ambarawa
    │   └── Magelang
    │       └── DesaA (tujuan)
    └── Salatiga
```

### Hasil BFS

```text
Jalur: Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA
Cost: 90 KM
```

---

## 3. Depth-First Search (DFS)

### Cara kerja

DFS menggunakan **stack** dengan aturan LIFO (*Last In, First Out*). Kota yang terakhir dimasukkan akan diproses lebih dahulu. DFS menyusuri satu cabang sedalam mungkin sebelum mencoba cabang lain.

Kota paling kiri pada tabel adalah bagian atas stack yang akan diproses berikutnya.

### Simulasi stack

| Langkah | Kota yang diproses | Isi stack setelah tetangga ditambahkan |
|---:|---|---|
| 0 | - | Semarang |
| 1 | Semarang | Ungaran, Kendal |
| 2 | Ungaran | Salatiga, Ambarawa, Kendal |
| 3 | Salatiga | Boyolali, Ambarawa, Kendal |
| 4 | Boyolali | Solo, Ambarawa, Kendal |
| 5 | Solo | DesaA, Sragen, Ambarawa, Kendal |
| 6 | DesaA | Tujuan ditemukan |

Jalur yang ditemukan DFS adalah:

```text
Semarang -> Ungaran -> Salatiga -> Boyolali -> Solo -> DesaA
```

### Perhitungan cost

```text
Semarang -> Ungaran       = 15 KM
Ungaran -> Salatiga       = 20 KM
Salatiga -> Boyolali      = 18 KM
Boyolali -> Solo          = 22 KM
Solo -> DesaA             = 30 KM

Total = 15 + 20 + 18 + 22 + 30 = 105 KM
```

### Pohon pencarian DFS

```text
Semarang
└── Ungaran
    └── Salatiga
        └── Boyolali
            └── Solo
                └── DesaA (tujuan)
```

### Hasil DFS

```text
Jalur: Semarang -> Ungaran -> Salatiga -> Boyolali -> Solo -> DesaA
Cost: 105 KM
```

DFS tidak menjamin jalur dengan cost paling kecil karena DFS memilih cabang berdasarkan kedalaman dan urutan tetangga.

---

## 4. Uniform-Cost Search (UCS)

### Cara kerja

UCS menggunakan **priority queue**. Setiap elemen memiliki total cost dari Semarang sampai kota tersebut. Kota dengan total cost terkecil diproses lebih dahulu.

### Simulasi priority queue

Format isi tabel adalah `kota: total cost`.

| Langkah | Kota yang dipilih | Cost | Kandidat setelah diperiksa |
|---:|---|---:|---|
| 0 | Semarang | 0 | Ungaran: 15, Kendal: 20 |
| 1 | Ungaran | 15 | Ambarawa: 25, Salatiga: 35, Kendal: 20 |
| 2 | Kendal | 20 | Salatiga: 35, Ambarawa: 25, Batang: 45 |
| 3 | Ambarawa | 25 | Salatiga: 35, Batang: 45, Magelang: 50 |
| 4 | Salatiga | 35 | Batang: 45, Magelang: 50, Boyolali: 53 |
| 5 | Batang | 45 | Magelang: 50, Boyolali: 53, Pekalongan: 75 |
| 6 | Magelang | 50 | Boyolali: 53, Pekalongan: 75, DesaA: 90 |
| 7 | DesaA | 90 | Tujuan ditemukan |

Jalur dengan total cost paling kecil adalah:

```text
Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA
```

### Perhitungan cost

```text
15 + 10 + 25 + 40 = 90 KM
```

### Hasil UCS

```text
Jalur: Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA
Cost: 90 KM
```

UCS menemukan cost minimum karena selalu memproses kandidat dengan total cost terkecil.

---

## 5. Perbandingan Kasus 1

| Metode | Jalur | Jumlah langkah | Cost |
|---|---|---:|---:|
| BFS | Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA | 4 | 90 KM |
| DFS | Semarang -> Ungaran -> Salatiga -> Boyolali -> Solo -> DesaA | 5 | 105 KM |
| UCS | Semarang -> Ungaran -> Ambarawa -> Magelang -> DesaA | 4 | 90 KM |

---

# Kasus 2: Rute Kapal di Sulawesi Selatan

## 1. Data Masalah

- Titik awal: **Makassar**
- Tujuan: **PasarB**
- Satuan biaya: **Jam**
- Jalan bersifat dua arah karena graph menggunakan `directed=False`.

---

## 2. Breadth-First Search (BFS)

### Simulasi queue

| Langkah | Kota yang diproses | Isi queue setelah tetangga ditambahkan |
|---:|---|---|
| 0 | - | Makassar |
| 1 | Makassar | ParePare, Jeneponto |
| 2 | ParePare | Jeneponto, Palopo |
| 3 | Jeneponto | Palopo, Bira |
| 4 | Palopo | Bira, Kolaka |
| 5 | Bira | Kolaka, Kendari |
| 6 | Kolaka | Kendari |
| 7 | Kendari | BauBau |
| 8 | BauBau | PasarB ditemukan |

### Pohon pencarian BFS

```text
Makassar
├── ParePare
│   └── Palopo
│       └── Kolaka
└── Jeneponto
    └── Bira
        └── Kendari
            └── BauBau
                └── PasarB (tujuan)
```

### Perhitungan cost

```text
Makassar -> Jeneponto = 4 jam
Jeneponto -> Bira     = 3 jam
Bira -> Kendari       = 8 jam
Kendari -> BauBau     = 6 jam
BauBau -> PasarB      = 4 jam

Total = 4 + 3 + 8 + 6 + 4 = 25 jam
```

### Hasil BFS

```text
Jalur: Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB
Cost: 25 jam
```

---

## 3. Depth-First Search (DFS)

### Simulasi stack

| Langkah | Kota yang diproses | Isi stack setelah tetangga ditambahkan |
|---:|---|---|
| 0 | - | Makassar |
| 1 | Makassar | Jeneponto, ParePare |
| 2 | Jeneponto | Bira, ParePare |
| 3 | Bira | Kendari, ParePare |
| 4 | Kendari | BauBau, Kolaka, ParePare |
| 5 | BauBau | PasarB, Kolaka, ParePare |
| 6 | PasarB | Tujuan ditemukan |

### Pohon pencarian DFS

```text
Makassar
└── Jeneponto
    └── Bira
        └── Kendari
            └── BauBau
                └── PasarB (tujuan)
```

### Perhitungan cost

```text
Makassar -> Jeneponto = 4 jam
Jeneponto -> Bira     = 3 jam
Bira -> Kendari       = 8 jam
Kendari -> BauBau     = 6 jam
BauBau -> PasarB      = 4 jam

Total = 25 jam
```

### Hasil DFS

```text
Jalur: Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB
Cost: 25 jam
```

---

## 4. Uniform-Cost Search (UCS)

### Simulasi priority queue

| Langkah | Kota yang dipilih | Cost | Kandidat setelah diperiksa |
|---:|---|---:|---|
| 0 | Makassar | 0 | Jeneponto: 4, ParePare: 5 |
| 1 | Jeneponto | 4 | ParePare: 5, Bira: 7 |
| 2 | ParePare | 5 | Bira: 7, Palopo: 12 |
| 3 | Bira | 7 | Palopo: 12, Kendari: 15 |
| 4 | Palopo | 12 | Kendari: 15, Kolaka: 18 |
| 5 | Kendari | 15 | Kolaka: 18, BauBau: 21 |
| 6 | Kolaka | 18 | BauBau: 21 |
| 7 | BauBau | 21 | PasarB: 25 |
| 8 | PasarB | 25 | Tujuan ditemukan |

### Pohon jalur UCS

```text
Makassar (0)
└── Jeneponto (4)
    └── Bira (7)
        └── Kendari (15)
            └── BauBau (21)
                └── PasarB (25)
```

Angka dalam kurung adalah total cost dari Makassar sampai kota tersebut.

### Perhitungan cost

```text
4 + 3 + 8 + 6 + 4 = 25 jam
```

### Hasil UCS

```text
Jalur: Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB
Cost: 25 jam
```

---

## 5. Perbandingan Kasus 2

| Metode | Jalur | Jumlah langkah | Cost |
|---|---|---:|---:|
| BFS | Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB | 5 | 25 jam |
| DFS | Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB | 5 | 25 jam |
| UCS | Makassar -> Jeneponto -> Bira -> Kendari -> BauBau -> PasarB | 5 | 25 jam |

---

# Kesimpulan

- **BFS** memakai queue FIFO dan mencari berdasarkan tingkat kedalaman.
- **DFS** memakai stack LIFO dan menyusuri satu cabang sedalam mungkin.
- **UCS** memakai priority queue dan selalu memilih total cost terkecil.
- Pada Kasus 1, BFS dan UCS menghasilkan cost 90 KM, sedangkan DFS menghasilkan 105 KM.
- Pada Kasus 2, ketiga metode menghasilkan jalur yang sama dengan cost 25 jam.
- UCS paling tepat digunakan ketika tujuan utama adalah mencari jalur dengan biaya minimum.
