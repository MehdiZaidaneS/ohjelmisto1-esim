

def muunnin(nestegallonaa):
    litraa = nestegallonaa * 3.785
    return litraa

def main():
    maara = float(input("Syötä nestegallonamäärä: "))
    while maara >= 0:
      print(f"{maara} nestegallonaa on {muunnin(maara)} litraa")
      maara =float(input("Syötä nestelonamäärä: "))
    print("\nSyötit negatiivisen gallonamäärä")


main()