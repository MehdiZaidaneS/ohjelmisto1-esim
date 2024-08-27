sukupuoli = input("Sukupuoli: ")
hemoglobiiniarvo = int(input("Hemoglobiiniarvo (g/l): "))

if sukupuoli == "Nainen" and 117 <=  hemoglobiiniarvo <= 175 :
    print("Sinun hemoglobiiniarvo on normaali")
elif sukupuoli == "Nainen" and hemoglobiiniarvo < 117:
    print("Sinun hemoglobiiniarvo on alhainen")
elif sukupuoli == "Nainen" and hemoglobiiniarvo > 175:
    print("Sinun hemoglobiiniarvo on korkea")
elif sukupuoli == "Mies" and 134 <= hemoglobiiniarvo <= 195:
    print("Sinun hemoglobiiniarvo on normaali")
elif sukupuoli == "Mies" and hemoglobiiniarvo < 134:
    print("Sinun hemoglobiiniarvo on alhainen")
elif sukupuoli == "Mies" and hemoglobiiniarvo > 195:
    print("Sinun hemoglobiiniarvo on korkea")
