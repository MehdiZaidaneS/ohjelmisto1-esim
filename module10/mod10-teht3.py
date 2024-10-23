class Hissi:

    def __init__(self, alikerros, ylikerros):
        self.alikerros = alikerros
        self.ylikerros = ylikerros
        self.kerros = self.alikerros

    def siirry_kerrokseen(self, kerrosnumero):

        while kerrosnumero != self.kerros:
          if kerrosnumero > self.kerros:
             self.kerros_ylös()
          elif kerrosnumero < self.kerros:
             self.kerros_alas()

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on {self.kerros}")


class Talo:
    def __init__(self, alikerros, ylikerros, hissilukumaara):
        self.alikerros = alikerros
        self.ylikerros = ylikerros
        self.hissilukumaara = hissilukumaara
        self.hissit = []
        for i in range(hissilukumaara):
            self.hissit.append(Hissi(alikerros, ylikerros))

    def aja_hissiä(self, hissinumero, kohdekerros):
        self.hissit[hissinumero-1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for i in range(len(self.hissit)):
            self.hissit[i].siirry_kerrokseen(self.alikerros)
            print(f"Hissi {i+1} on pohjakerroksessa")


talo = Talo(0,10,5)
talo.aja_hissiä(5, 5)
talo.aja_hissiä(4,4)
talo.aja_hissiä(3,3)
talo.aja_hissiä(2,2)
talo.aja_hissiä(1,1)
talo.palohälytys()