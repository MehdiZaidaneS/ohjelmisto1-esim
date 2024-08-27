import random

pisteidenmaara = int(input("Anna pisteiden määrä: "))

N = 0
n = 0

while pisteidenmaara > 0:

    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    pisteidenmaara = pisteidenmaara - 1
    N = N + 1
    if x ** 2 + y ** 2 < 1:
        n = n + 1


print("Piin likiarvo on " + str(4*n/N))