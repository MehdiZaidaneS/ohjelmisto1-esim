luku = input("Anna luku: ")

suurimmanLuvu = int(luku)
pienimmanLuvu = int(luku)

while luku != "":
  if int(luku) >= suurimmanLuvu:
      suurimmanLuvu = int(luku)
      luku = input("Anna luku: ")
  elif int(luku) <= pienimmanLuvu:
       pienimmanLuvu = int(luku)
       luku = input("Anna luku: ")
  else:
      luku = input("Anna luku: ")


print(str(suurimmanLuvu) + " oli suurimman luku ja " + str(pienimmanLuvu) + " oli pienimman luku.")













