lentoasemat = {"EFHK": "Helsinki-Vantaan lentoasema",
               "EFTP": "Tampere-Pirkkalan lentoasema",
               "EFTU": "Turun lentoasema",
               "EFOU": "Oulun lentoasema",
               "EFRO": "Rovaniemen lentoasema"}


while True:
    print(f"\nMitä haluaisit tehda:\n"
          f"Paina 1 jos: Haluatko syöttää uuden lentoaseman?\n"
          f"Paina 2 jos: Haluatko hakea jo syötetyn lentoaseman tiedot?\n"
          f"Paina 3 jos: Haluatko lopettaa?")

    toiminto = int(input("Syötä toiminto: "))

    if toiminto == 1:
         ICAO = input("Syötä uuden lentoaseman ICAO-koodi: ")
         nimi = input("Syötä uuden lentoaseman nimi: ")
         lentoasemat[ICAO] = nimi
         print(f"Olet lisännyt {nimi} {ICAO}-koodilla")
    elif toiminto == 2:
        ICAO = input("Syötä lentoaseman ICAO-koodi: ")
        print(f"Lentoaseman nimi koodilla {ICAO} on {lentoasemat[ICAO]}")
    else:
        print("Ohjelman suoritus päättyy!")
        break




