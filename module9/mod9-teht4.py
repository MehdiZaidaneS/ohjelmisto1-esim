import random

class Auto:

    kilpailu = True

    def __init__(self, tunnus, huippunopeus, thnopeus = 0, kuljettumatka= 0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.thnopeus = thnopeus
        self.kuljettumatka = kuljettumatka


    def kiihdyta(self, nopeusmuutos):
        if nopeusmuutos + self.thnopeus > self.huippunopeus:
             print("Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi")
        elif nopeusmuutos + self.thnopeus < 0:
             print("Auton nopeus ei saa alentua nollaa pienemmäksi.")
        else:
             self.thnopeus = nopeusmuutos + self.thnopeus


    def kulje(self, tuntimaara):
        self.kuljettumatka = (self.thnopeus * tuntimaara) + self.kuljettumatka
        if self.kuljettumatka > 10000:
            print(f"{self.tunnus} on edennyt +10000km")
            Auto.kilpailu = False




autolista = []

for i in range (1,11):
    tunnus = f"ABC-{i}"
    huippunopeus = random.randint(100,200)

    autolista.append(Auto(tunnus, huippunopeus))



while Auto.kilpailu:

   for auto in autolista:
       auto.kiihdyta(random.randint(-10,15))
       auto.kulje(1)

print(f"{'Rekisteri':<10}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<15}{'Matka (km)':<10}")
for auto in autolista:
    print(f"{auto.tunnus:<10} {auto.huippunopeus:<20} {auto.thnopeus:<15} {auto.kuljettumatka:<10.2f}")