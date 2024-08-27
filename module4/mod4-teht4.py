import random
arvaus = int(input("Arvaa numero 1-10: "))
kokonaisluku = random.randint(1,10)


while kokonaisluku != arvaus:

   if arvaus > kokonaisluku:
       print("Liian suuri arvaus")
       arvaus = int(input("Arvaa numero 1-10: "))
   elif arvaus < kokonaisluku:
       print("Liian pieni arvaus")
       arvaus = int(input("Arvaa numero 1-10: "))

print("Oikein!")