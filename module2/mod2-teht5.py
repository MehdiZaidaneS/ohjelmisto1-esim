import math

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))


naulatSumma = (leiviskat * 20) + naulat
luoditSumma = (naulatSumma * 32) + luodit


grammaSumma = (luoditSumma * 13.3)
kilogramma = int(grammaSumma / 1000)



print(f"\nMassa nykymittojen mukaan:\n{kilogramma} kilogrammaa ja {grammaSumma%1000:.2f} grammaa.")

