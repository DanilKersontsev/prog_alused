failinimi = input("Sisestage failinimi: ")
fail = open(failinimi + ".txt", encoding="UTF-8")
failist = fail.read().upper().replace("Ä","AE").replace("Õ","OE").replace("Ü", "UE")
fail.close()
print(failist)



