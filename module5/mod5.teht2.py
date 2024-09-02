luku = input("Anna luku: ")

luvut = []
surrimmatLuvut = []

while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku: ")


luvut.sort(reverse=True)

for i in range(0,5):
    surrimmatLuvut.append(luvut[i])

print("Surrimmat luvut ovat " + str(surrimmatLuvut))





