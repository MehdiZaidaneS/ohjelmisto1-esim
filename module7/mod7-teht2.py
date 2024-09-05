nimet = set()
nimi = input("Syötä nimi: ")

while nimi != "":

    if nimi in nimet:
      print("Aiemmin syötetty nimi")
    else:
      print("Uusi nimi")

    nimet.add(nimi)
    nimi = input("Syötä nimi: ")


print("\nSyötetut nimet ovat: ")
for nimi in nimet:
    print("- " + nimi)