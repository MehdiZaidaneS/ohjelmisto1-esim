

def listafunkito(lista):
    uusilista = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            uusilista.append(lista[i])
    return uusilista



def main():
    lista = []
    numero = input("Syötä numero, jonka haluat lisätä listaan: ")

    while numero != "":
        lista.append(int(numero))
        numero = input("Syötä numero, jonka haluat lisätä listaan: ")

    print("\nOlet luonut tämän listan: " + str(lista))
    print(f"Uuden listan luvut: {listafunkito(lista)}")


main()