import random


def noppa(tahkot):
    heitto = random.randint(1,tahkot)
    return heitto


def ohjelma():
    tahkot = int(input("Syötä nopan tahkojen yhteismäärä: "))
    number = noppa(tahkot)
    while number != tahkot:
        print(number)
        number = noppa(tahkot)
    print("Sait numero " + str(tahkot))



ohjelma()