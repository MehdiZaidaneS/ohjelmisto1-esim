import math

def yksikkohinta(halkaisija, euro):

    neliometri = math.pi * ((halkaisija / 2) ** 2 / 100)

    return neliometri



def main():
    halkaisija1 = float(input("Pizza 1 halkaisijan senttimetreinä: "))
    hinta1 = float(input("Pizza 1 hinnan euroina: "))

    print(f"Ensimmäisen pizzan yksikköhinta on {yksikkohinta(halkaisija1, hinta1)}")

    halkaisija2 = float(input("Pizza 2 halkaisijan senttimetreinä: "))
    hinta2 = float(input("Pizza 2 hinnan euroina: "))

    print(f"Toisen pizzan yksikköhinta on {yksikkohinta(halkaisija2, hinta2)}")

    if yksikkohinta(halkaisija1, hinta1) < yksikkohinta(halkaisija2, hinta2):
        print("\nPizza 1 tarjoaa paremman vastineen rahalle.")
    else:
        print("\nPizza 2 tarjoaa paremman vastineen rahalle.")



main()