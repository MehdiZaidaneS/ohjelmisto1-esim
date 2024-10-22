class Auto:
    def __init__(self, tunnus, huippunopeus, thnopeus = 0, kuljettumatka= 0):
        self.tunnus = tunnus
        self.huippunopeus = huippunopeus
        self.thnopeus = thnopeus
        self.kuljettumatka = kuljettumatka


uusiauto = Auto("ABC-123", 142)

print(f"{uusiauto.tunnus} auto huippunopeus on {uusiauto.huippunopeus}km/h, tämän hetkinen nopues on {uusiauto.thnopeus}km/h ja kuljettu matka on {uusiauto.kuljettumatka}.")