pituus = float(input("Syötä kuhan pituus senttimetreinä: "))

if pituus <= 36:
    print("Laske kuhan takaisin järveen. " + str(36 - pituus) + " cm senttiä alimmasta sallitusta pyyntimitasta puuttuu!" )
else:
    print("Kuhan piitus on " + str(pituus))