def diskon(harga):
    total = harga
    if(total > 50000):
        total = total - (total * 0.27)
    elif(30000 <= total <= 50000):
        total = total - (total * 0.22)
    return total

def main():
    harga = int(input())
    total = diskon(harga)
    print("Total harga yang harus dibayarkan:", total)

main()