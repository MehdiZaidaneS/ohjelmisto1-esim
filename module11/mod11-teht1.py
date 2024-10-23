class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi



class Kirja(Julkaisu):
   def __init__(self, nimi,kirjoittaja, sivumaara):
       Julkaisu.__init__(self, nimi)
       self.kirjoittaja = kirjoittaja
       self.sivumaara = sivumaara

   def tulosta_tiedot(self):
       print(f"Kirjan nimi on {self.nimi}, kirjoittaja on {self.kirjoittaja} ja {self.sivumaara} sivua")



class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi} ja päätoimittaja on {self.paatoimittaja}.")



akuankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", "200")


akuankka.tulosta_tiedot()
hytti6.tulosta_tiedot()




