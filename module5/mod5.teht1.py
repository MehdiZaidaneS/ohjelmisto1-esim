import random
lukumaara = int(input("Syötä arpakuutioiden lukumäärän: " ))

summa = [0]

for i in range(lukumaara):

   arpakuutio = random.randint(1,6)
   print(arpakuutio)

   summa.append(arpakuutio + summa[0])
   summa.remove(summa[0])



print("Lukujen summa on " + str(summa[0]))

