# Pengerjaan Graph Search Jawa Barat

## 1. Data Masalah

- Titik awal: **Bogor**
- Tujuan: **Pangandaran**
- Setiap angka pada peta menunjukkan jarak atau biaya perjalanan antarkota.
- Karena `directed=False`, setiap jalan dianggap bisa dilalui dua arah.

Pencarian dilakukan dengan tiga metode:

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Uniform-Cost Search (UCS)

---

## 2. Breadth-First Search (BFS)

### Cara kerja

BFS memeriksa titik berdasarkan tingkat kedalaman. Semua kota yang berjarak satu langkah dari titik awal diperiksa lebih dahulu, kemudian kota yang berjarak dua langkah, dan seterusnya.

BFS menggunakan prinsip **FIFO** (*First In, First Out*). Kota yang masuk lebih dahulu ke antrean akan diperiksa lebih dahulu.

### Langkah pencarian

Mulai dari **Bogor**:

1. Bogor memiliki tetangga Bekasi, Sukabumi, dan Cianjur.
2. Pencarian dilanjutkan berdasarkan urutan tingkat kedalaman.
3. Jalur yang pertama mencapai Pangandaran adalah:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

### Perhitungan biaya

```text
Bogor -> Cianjur       = 8
Cianjur -> Bandung     = 8
Bandung -> Garut       = 8
Garut -> Tasikmalaya   = 8
Tasikmalaya -> Pangandaran = 8

Total biaya = 8 + 8 + 8 + 8 + 8 = 40
```

### Hasil BFS

```text
Jalur: Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
Cost: 40
```

BFS menemukan jalur dengan jumlah langkah paling sedikit. Namun, BFS tidak selalu menghasilkan biaya paling kecil jika bobot jalan berbeda-beda.

---

## 3. Depth-First Search (DFS)

### Cara kerja

DFS menelusuri satu jalur sedalam mungkin. Jika jalur tersebut belum mencapai tujuan, pencarian dapat kembali (*backtracking*) dan mencoba jalur lain.

DFS menggunakan prinsip **LIFO** (*Last In, First Out*). Titik yang terakhir dimasukkan akan diperiksa lebih dahulu.

### Langkah pencarian

Dengan urutan tetangga seperti pada data peta, DFS menemukan jalur:

```text
Bogor -> Cianjur -> Purwakarta -> Subang -> Sumedang
      -> Majalengka -> Kuningan -> Ciamis -> Pangandaran
```

### Perhitungan biaya

```text
Bogor -> Cianjur          = 8
Cianjur -> Purwakarta     = 8
Purwakarta -> Subang      = 8
Subang -> Sumedang        = 10
Sumedang -> Majalengka    = 5
Majalengka -> Kuningan    = 10
Kuningan -> Ciamis        = 8
Ciamis -> Pangandaran     = 5

Total biaya = 8 + 8 + 8 + 10 + 5 + 10 + 8 + 5 = 62
```

### Hasil DFS

```text
Jalur: Bogor -> Cianjur -> Purwakarta -> Subang -> Sumedang
       -> Majalengka -> Kuningan -> Ciamis -> Pangandaran
Cost: 62
```

DFS tidak menjamin jalur terpendek atau biaya termurah. Hasilnya sangat bergantung pada urutan tetangga yang diperiksa.

---

## 4. Uniform-Cost Search (UCS)

### Cara kerja

UCS selalu memilih jalur dengan **total biaya sementara paling kecil**. Setiap kali ada beberapa pilihan jalur, jalur dengan cost terkecil diperiksa lebih dahulu.

Berbeda dengan BFS dan DFS, UCS memperhitungkan bobot setiap jalan.

### Langkah pencarian

Jalur termurah yang ditemukan adalah:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

Total biaya sementara:

```text
Bogor -> Cianjur                         = 8
Bogor -> Cianjur -> Bandung              = 16
Bogor -> Cianjur -> Bandung -> Garut     = 24
... -> Tasikmalaya                       = 32
... -> Pangandaran                       = 40
```

### Perhitungan biaya

```text
8 + 8 + 8 + 8 + 8 = 40
```

### Hasil UCS

```text
Jalur: Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
Cost: 40
```

UCS menghasilkan jalur dengan biaya paling kecil selama semua bobot jalan bernilai tidak negatif.

---

## 5. Isi Queue, Stack, dan Priority Queue

Pada tabel berikut, isi struktur data ditulis dari **depan atau bagian yang akan diproses**.

### A. Simulasi Queue BFS

Queue menggunakan aturan FIFO. Setiap kota yang baru ditemukan dimasukkan ke bagian belakang queue.

| Langkah | Kota yang diproses | Isi queue setelah penambahan tetangga |
|---:|---|---|
| 0 | - | Bogor |
| 1 | Bogor | Bekasi, Sukabumi, Cianjur |
| 2 | Bekasi | Sukabumi, Cianjur, Karawang |
| 3 | Sukabumi | Cianjur, Karawang |
| 4 | Cianjur | Karawang, Bandung, WestBandung, Purwakarta |
| 5 | Karawang | Bandung, WestBandung, Purwakarta, Subang |
| 6 | Bandung | WestBandung, Purwakarta, Subang, Sumedang, Garut |
| 7 | WestBandung | Purwakarta, Subang, Sumedang, Garut |
| 8 | Purwakarta | Subang, Sumedang, Garut |
| 9 | Subang | Sumedang, Garut, Indramayu |
| 10 | Sumedang | Garut, Indramayu, Majalengka |
| 11 | Garut | Indramayu, Majalengka, Tasikmalaya |
| 12 | Indramayu | Majalengka, Tasikmalaya, Cirebon |
| 13 | Majalengka | Tasikmalaya, Cirebon, Kuningan |
| 14 | Tasikmalaya | Pangandaran ditemukan |

Pada saat Tasikmalaya diproses, tetangganya adalah Pangandaran. Karena tujuan sudah ditemukan, pencarian berhenti.

Pohon jalur BFS yang menuju tujuan dapat digambarkan sebagai berikut:

```text
Bogor
├── Bekasi
│   └── Karawang
├── Sukabumi
└── Cianjur
      ├── Bandung
      │   └── Garut
      │       └── Tasikmalaya
      │           └── Pangandaran (tujuan)
      ├── WestBandung
      └── Purwakarta
```

Jalur hasil diambil dengan menelusuri induk dari tujuan kembali ke awal:

```text
Pangandaran <- Tasikmalaya <- Garut <- Bandung <- Cianjur <- Bogor
```

Kemudian urutannya dibalik menjadi:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

### B. Simulasi Stack DFS

Stack menggunakan aturan LIFO. Kota yang terakhir dimasukkan akan diproses lebih dahulu. Pada tabel ini, kota paling kiri adalah bagian atas stack.

| Langkah | Kota yang diproses | Isi stack setelah penambahan tetangga |
|---:|---|---|
| 0 | - | Bogor |
| 1 | Bogor | Cianjur, Sukabumi, Bekasi |
| 2 | Cianjur | Purwakarta, WestBandung, Bandung, Sukabumi, Bekasi |
| 3 | Purwakarta | Subang, WestBandung, Bandung, Sukabumi, Bekasi |
| 4 | Subang | Sumedang, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi |
| 5 | Sumedang | Majalengka, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi |
| 6 | Majalengka | Kuningan, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi |
| 7 | Kuningan | Ciamis, Cirebon, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi |
| 8 | Ciamis | Pangandaran, Tasikmalaya, Cirebon, Bandung, Indramayu, WestBandung, Bandung, Sukabumi, Bekasi |
| 9 | Pangandaran | Tujuan ditemukan |

Pohon jalur DFS yang pertama kali mencapai tujuan adalah:

```text
Bogor
└── Cianjur
      └── Purwakarta
            └── Subang
                  └── Sumedang
                        └── Majalengka
                              └── Kuningan
                                    └── Ciamis
                                          └── Pangandaran (tujuan)
```

DFS berhenti ketika Pangandaran ditemukan. Karena DFS fokus menyusuri satu cabang sampai dalam, jalurnya tidak harus menjadi jalur terpendek.

### C. Simulasi Priority Queue UCS

UCS menyimpan pasangan **(total cost, kota)**. Elemen dengan total cost terkecil selalu dikeluarkan lebih dahulu.

| Langkah | Kota yang dipilih | Cost jalur yang dipilih | Kandidat penting setelah diperiksa |
|---:|---|---:|---|
| 0 | Bogor | 0 | Cianjur: 8, Sukabumi: 15, Bekasi: 10 |
| 1 | Cianjur | 8 | Bandung: 16, WestBandung: 16, Purwakarta: 16 |
| 2 | Bekasi | 10 | Karawang: 20 |
| 3 | Sukabumi | 15 | Tidak ada cost yang lebih kecil dari 16 |
| 4 | Bandung | 16 | Garut: 24, Sumedang: 26 |
| 5 | WestBandung | 16 | Tidak ada jalur baru yang lebih murah |
| 6 | Purwakarta | 16 | Subang: 24 |
| 7 | Garut | 24 | Tasikmalaya: 32 |
| 8 | Subang | 24 | Indramayu: 34 |
| 9 | Tasikmalaya | 32 | Ciamis: 37, Pangandaran: 40 |
| 10 | Ciamis | 37 | Pangandaran tetap 40 karena jalur baru biayanya lebih besar |
| 11 | Pangandaran | 40 | Tujuan ditemukan |

Karena Pangandaran dipilih dengan cost `40`, sedangkan semua kandidat lain memiliki cost lebih besar, UCS berhenti.

```text
Bogor (0)
└── Cianjur (8)
      └── Bandung (16)
            └── Garut (24)
                  └── Tasikmalaya (32)
                        └── Pangandaran (40)
```

Angka dalam kurung adalah total cost dari Bogor sampai kota tersebut.

---

## 6. Perbandingan Hasil

| Metode | Jalur | Jumlah langkah | Cost |
|---|---|---:|---:|
| BFS | Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran | 5 | 40 |
| DFS | Bogor -> Cianjur -> Purwakarta -> Subang -> Sumedang -> Majalengka -> Kuningan -> Ciamis -> Pangandaran | 8 | 62 |
| UCS | Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran | 5 | 40 |

## 7. Kesimpulan

- **BFS** mencari berdasarkan jumlah tingkat atau langkah.
- **DFS** mencari sedalam mungkin berdasarkan urutan tetangga.
- **UCS** mencari berdasarkan total biaya perjalanan.
- Pada peta ini, BFS dan UCS mendapatkan jalur yang sama dengan cost **40**.
- DFS mendapatkan jalur yang lebih panjang dengan cost **62**.
- Untuk mencari rute termurah, UCS adalah metode yang paling sesuai.
