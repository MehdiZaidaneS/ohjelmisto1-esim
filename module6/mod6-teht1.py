import random


def noppa():
    heitto = random.randint(1,6)
    return heitto


def ohjelma():
    luku = noppa()
    while luku != 6:
        print(luku)
        luku = noppa()
    print("Sait numero 6!")



ohjelma()