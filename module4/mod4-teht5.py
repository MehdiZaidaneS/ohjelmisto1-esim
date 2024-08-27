tunnus = input("Käyttäjätunnus: ")
salasana = input("Salasana: ")

numTry = 5

while tunnus != "python" or salasana != "rules":
    if numTry <= 0:
        print("Pääsy evätty!")
        break

    numTry = numTry - 1
    print("\nKäyttäjätunnus tai salasana on väärä. Jäljellä olevat yritykset: " + str(numTry))
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")


if tunnus == "python" or salasana == "rules":
    print("Tervetuloa!")