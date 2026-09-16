# LKP 4 - Greedy Best-First Search dan A*

## 1. Permasalahan

- Node awal: **Bogor**
- Node tujuan: **Pangandaran**
- Heuristic: jarak Euclidean dari kota saat ini ke Pangandaran

Rumus jarak Euclidean:

```text
euclid(x, y) = sqrt((x1 - y1)^2 + (x2 - y2)^2)
```

Koordinat tujuan Pangandaran adalah `(50, 5)`.

## 2. Perhitungan Euclidean

| Kota | Koordinat | Perhitungan | h(n) |
|---|---|---|---:|
| Bandung | (30, 10) | sqrt((30 - 50)^2 + (10 - 5)^2) | 20.62 |
| Bekasi | (10, 50) | sqrt((10 - 50)^2 + (50 - 5)^2) | 60.21 |
| Bogor | (20, 30) | sqrt((20 - 50)^2 + (30 - 5)^2) | 39.05 |
| Ciamis | (50, 20) | sqrt((50 - 50)^2 + (20 - 5)^2) | 15.00 |
| Cianjur | (23, 20) | sqrt((23 - 50)^2 + (20 - 5)^2) | 30.89 |
| Cirebon | (45, 30) | sqrt((45 - 50)^2 + (30 - 5)^2) | 25.50 |
| Garut | (40, 5) | sqrt((40 - 50)^2 + (5 - 5)^2) | 10.00 |
| Indramayu | (40, 30) | sqrt((40 - 50)^2 + (30 - 5)^2) | 26.93 |
| Karawang | (20, 50) | sqrt((20 - 50)^2 + (50 - 5)^2) | 54.08 |
| Kuningan | (45, 20) | sqrt((45 - 50)^2 + (20 - 5)^2) | 15.81 |
| Majalengka | (40, 20) | sqrt((40 - 50)^2 + (20 - 5)^2) | 18.03 |
| Pangandaran | (50, 5) | sqrt((50 - 50)^2 + (5 - 5)^2) | 0.00 |
| Purwakarta | (30, 30) | sqrt((30 - 50)^2 + (30 - 5)^2) | 32.02 |
| Subang | (20, 40) | sqrt((20 - 50)^2 + (40 - 5)^2) | 46.10 |
| Sukabumi | (20, 20) | sqrt((20 - 50)^2 + (20 - 5)^2) | 33.54 |
| Sumedang | (35, 25) | sqrt((35 - 50)^2 + (25 - 5)^2) | 25.00 |
| Tasikmalaya | (45, 5) | sqrt((45 - 50)^2 + (5 - 5)^2) | 5.00 |
| WestBandung | (25, 10) | sqrt((25 - 50)^2 + (10 - 5)^2) | 25.50 |

## 3. Greedy Best-First Search

Greedy memilih node dengan nilai heuristic terkecil, yaitu `h(n)`.

| Iterasi | Node diekspansi | Queue setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Bogor (39.05) | Cianjur (30.89), Sukabumi (33.54), Bekasi (60.21) | Bogor | Tidak |
| 1 | Cianjur (30.89) | Bandung (20.62), WestBandung (25.50), Purwakarta (32.02), Sukabumi (33.54), Bekasi (60.21) | Bogor, Cianjur | Tidak |
| 2 | Bandung (20.62) | Garut (10.00), Sumedang (25.00), WestBandung (25.50), Purwakarta (32.02), Sukabumi (33.54), Bekasi (60.21) | Bogor, Cianjur, Bandung | Tidak |
| 3 | Garut (10.00) | Tasikmalaya (5.00), Sumedang (25.00), WestBandung (25.50), Purwakarta (32.02), Sukabumi (33.54), Bekasi (60.21) | Bogor, Cianjur, Bandung, Garut | Tidak |
| 4 | Tasikmalaya (5.00) | Pangandaran (0.00), Ciamis (15.00), Sumedang (25.00), WestBandung (25.50), Purwakarta (32.02), Sukabumi (33.54), Bekasi (60.21) | Bogor, Cianjur, Bandung, Garut, Tasikmalaya | Tidak |
| 5 | Pangandaran (0.00) | Ciamis (15.00), Sumedang (25.00), WestBandung (25.50), Purwakarta (32.02), Sukabumi (33.54), Bekasi (60.21) | Bogor, Cianjur, Bandung, Garut, Tasikmalaya, Pangandaran | YA |

Jalur Greedy:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

Cost:

```text
8 + 8 + 8 + 8 + 8 = 40
```

## 4. A* Search

A* memilih node dengan nilai terkecil:

```text
f(n) = g(n) + h(n)
```

Keterangan:

- `g(n)`: cost dari Bogor ke node saat ini
- `h(n)`: estimasi Euclidean dari node saat ini ke Pangandaran
- `f(n)`: total nilai prioritas node

| Iterasi | Node diekspansi | Queue setelah ekspansi | Explored | Solusi? |
|---:|---|---|---|---|
| 0 | Bogor (g=0, h=39.05, f=39.05) | Cianjur (f=38.89), Sukabumi (f=48.54), Bekasi (f=70.21) | Bogor | Tidak |
| 1 | Cianjur (g=8, h=30.89, f=38.89) | Bandung (f=36.62), WestBandung (f=41.50), Purwakarta (f=48.02), Sukabumi (f=48.54), Bekasi (f=70.21) | Bogor, Cianjur | Tidak |
| 2 | Bandung (g=16, h=20.62, f=36.62) | Garut (f=34.00), WestBandung (f=41.50), Purwakarta (f=48.02), Sukabumi (f=48.54), Sumedang (f=51.00), Bekasi (f=70.21) | Bogor, Cianjur, Bandung | Tidak |
| 3 | Garut (g=24, h=10.00, f=34.00) | Tasikmalaya (f=37.00), WestBandung (f=41.50), Purwakarta (f=48.02), Sukabumi (f=48.54), Sumedang (f=51.00), Bekasi (f=70.21) | Bogor, Cianjur, Bandung, Garut | Tidak |
| 4 | Tasikmalaya (g=32, h=5.00, f=37.00) | Pangandaran (f=40.00), WestBandung (f=41.50), Purwakarta (f=48.02), Sukabumi (f=48.54), Sumedang (f=51.00), Ciamis (f=52.00), Bekasi (f=70.21) | Bogor, Cianjur, Bandung, Garut, Tasikmalaya | Tidak |
| 5 | Pangandaran (g=40, h=0.00, f=40.00) | WestBandung (f=41.50), Purwakarta (f=48.02), Sukabumi (f=48.54), Sumedang (f=51.00), Ciamis (f=52.00), Bekasi (f=70.21) | Bogor, Cianjur, Bandung, Garut, Tasikmalaya, Pangandaran | YA |

Jalur A*:

```text
Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran
```

Cost:

```text
8 + 8 + 8 + 8 + 8 = 40
```

## 5. Kesimpulan

| Metode | Jalur | Cost |
|---|---|---:|
| Greedy Best-First Search | Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran | 40 |
| A* Search | Bogor -> Cianjur -> Bandung -> Garut -> Tasikmalaya -> Pangandaran | 40 |

Pada kasus ini, Greedy dan A* menghasilkan jalur serta cost yang sama. Perbedaannya terletak pada prioritas queue: Greedy hanya menggunakan `h(n)`, sedangkan A* menggunakan `f(n) = g(n) + h(n)`.
