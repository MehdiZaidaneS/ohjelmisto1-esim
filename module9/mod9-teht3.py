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



uusiauto = Auto("ABC-123", 142)

uusiauto.kiihdyta(30)
uusiauto.kiihdyta(70)
uusiauto.kiihdyta(50)
print(f"{uusiauto.tunnus} auton tämän hetkinen nopeus on {uusiauto.thnopeus}km/h")

uusiauto.kulje(1)
print(f"Auto kuljettu matka on {uusiauto.kuljettumatka} km.")