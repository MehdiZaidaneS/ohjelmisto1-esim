
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


h = Hissi(0, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alikerros)