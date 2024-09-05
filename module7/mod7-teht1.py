
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä",
              "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausinumero = int(input("Syötä kuukauden numero (1-12): "))

print(f"{kuukausinumero} kuukauden vuodenaika on {vuodenajat[kuukausinumero-1]}")