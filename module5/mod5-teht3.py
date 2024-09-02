kokonaisluku = int(input("Syötä kokonaisluku: "))

jaollinen = []


for i in range(1, kokonaisluku+1):
    if kokonaisluku % i == 0:
        jaollinen.append(i)


if len(jaollinen) == 2:
    print("Se on alkuluku")
else:
    print("Ei ole alkuluku")
