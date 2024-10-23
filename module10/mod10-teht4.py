import random

class Auto:

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




class Kilpailu:

    tunti = 1

    def __init__(self, nimi, pituus):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = []
        for i in range(1, 11):
            tunnus = f"ABC-{i}"
            huippunopeus = random.randint(100, 200)

            self.autot.append(Auto(tunnus, huippunopeus))

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-15, 10))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<10}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<15}{'Matka (km)':<10}")
        for auto in self.autot:
            print(f"{auto.tunnus:<10} {auto.huippunopeus:<20} {auto.thnopeus:<15} {auto.kuljettumatka:<10.2f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettumatka > self.pituus:
                return True

        return False


kilpailu1 = Kilpailu("Suuri romuralli", 8000)

while kilpailu1.kilpailu_ohi() == False:
    kilpailu1.tunti_kuluu()
    if Kilpailu.tunti % 10 == 0:
        kilpailu1.tulosta_tilanne()
    if kilpailu1.kilpailu_ohi() == True:
        kilpailu1.tulosta_tilanne()
        break
    Kilpailu.tunti += 1


