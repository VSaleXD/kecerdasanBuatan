
def golongan(gaji):
    if gaji <= 4000000:
        return "UKT 2"
    elif 4000000 < gaji <= 7000000:
        return "UKT 3"
    elif 7000000 < gaji <= 10000000:
        return "UKT 4"
    else:
        return "UKT 5"

def main():
    golo = str(input())
    if(golo == "BIDIKMISI"):
        print("Anda mendapatkan golongan UKT 1")
        return
    else:
        gaji = int(input())
        gol = golongan(gaji)
        print("Anda mendapatkan golongan", gol)
        return

main()