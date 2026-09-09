class Robot:

    def __init__(self, matriks):
        self.matriks = matriks
        self.rows = len(matriks)
        self.cols = len(matriks[0])
        self.t = 1  

    def status(self, r, c):
        print(f"t = {self.t}")

        for i in range(self.rows):
            baris = []
            for j in range(self.cols):
                if i == r and j == c:
                    baris.append("x")
                else:
                    baris.append(str(self.matriks[i][j]))
            print(" ".join(baris))

        print("***")
        self.t += 1

    def jalankan(self):
        r, c = 0, 0
        arah = 1  

        while r < self.rows:
            self.status(r, c)

            if self.matriks[r][c] == 1:
                self.matriks[r][c] = 0

            c_next = c + arah

            if c_next < 0 or c_next >= self.cols:
                r += 1  # Turun 
                arah *= -1  # Balik arah
            else:
                c = c_next


def main():
    matriks= [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]

    r = Robot(matriks)
    r.jalankan()    


main()