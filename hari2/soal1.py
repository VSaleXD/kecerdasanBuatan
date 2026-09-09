class mahasiswa:

    def __init__(self, nilaiUTS, nilaiUAS, nilaiPraktikum, nilaiKeaktifan):
        self.nilaiUTS = nilaiUTS
        self.nilaiUAS = nilaiUAS
        self.nilaiPraktikum = nilaiPraktikum

        if isinstance(nilaiKeaktifan, list):
            self.nilaiKeaktifan = sum(nilaiKeaktifan) / len(nilaiKeaktifan)
        else:
            self.nilaiKeaktifan = nilaiKeaktifan

    def hitung(self):
        return (
            (0.30 * self.nilaiUTS)
            + (0.35 * self.nilaiUAS)
            + (0.30 * self.nilaiPraktikum)
            + (0.05 * self.nilaiKeaktifan)
        )


class alihJenis(mahasiswa):

    def __init__(
        self,
        nilaiUTS,
        nilaiUAS,
        nilaiPraktikum,
        nilaiKeaktifan,
        nilaiUjianMatrikulasi,
    ):

        super().__init__(nilaiUTS, nilaiUAS, nilaiPraktikum, nilaiKeaktifan)
        self.nilaiUjianMatrikulasi = nilaiUjianMatrikulasi

    def hitung(self):
        return (
            (0.25 * self.nilaiUTS)
            + (0.25 * self.nilaiUAS)
            + (0.20 * self.nilaiPraktikum)
            + (0.05 * self.nilaiKeaktifan)
            + (0.25 * self.nilaiUjianMatrikulasi)
        )


def main():
    teks = input()

    if "matrikulasi" in teks:
        bagian = teks.split("matrikulasi")

        nilai = [
            float(x) for x in bagian[0].replace(",", " ").split() if x.isdigit()
        ]

        matrikulasi = float(
            bagian[1].replace("=", "").replace(",", "").strip()
        )

        uts = nilai[0]
        uas = nilai[1]
        praktikum = nilai[2]
        keaktifan = nilai[3:] 

        mhs = alihJenis(uts, uas, praktikum, keaktifan, matrikulasi)
    else:
        nilai = [
            float(x) for x in teks.replace(",", " ").split() if x.isdigit()
        ]

        uts = nilai[0]
        uas = nilai[1]
        praktikum = nilai[2]
        keaktifan = nilai[3:]  

        mhs = mahasiswa(uts, uas, praktikum, keaktifan)

    print(mhs.hitung())

main()