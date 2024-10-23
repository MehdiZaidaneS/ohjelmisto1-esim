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
        print(f"{self.tunnus} kuljettumataka on {self.kuljettumatka}")



class Sahkoauto(Auto):

     def __init__(self, tunnus, huippunopeus, akkukapasiteetti):
         Auto.__init__(self, tunnus, huippunopeus)
         self.akkukapasiteetti = akkukapasiteetti




class Polttomoottoriauto(Auto):

    def __init__(self, tunnus, huippunopeus, bensatankki):
        Auto.__init__(self, tunnus, huippunopeus)
        self.bensatankki = bensatankki



sahkoauto = Sahkoauto("ABC-15", 180,52.5)
polttomoottoriauton = Polttomoottoriauto("ABC-123", 165,32.3)


sahkoauto.kiihdyta(100)
polttomoottoriauton.kiihdyta(90)
sahkoauto.kulje(1)
polttomoottoriauton.kulje(1)



