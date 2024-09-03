
def summa(lista):
    summa = 0

    for i in range(len(lista)):
        summa += lista[i]

    return summa



def main():
    lista = []
    numero = input("Syötä numero, jonka haluat lisätä listaan: ")

    while numero != "":
        lista.append(int(numero))
        numero = input("Syötä numero, jonka haluat lisätä listaan: ")

    print(f"Listan lukujen summa on {summa(lista)}")


main()