from urllib.request import urlopen
kuu = input("Sisestage kuu: ")
päev = int(input("Sisestage päev: "))
failVeebis = urlopen("https://kodu.ut.ee/~eno/mooc/" + kuu)
baidid = failVeebis.read()
tekst = baidid.decode() 
ridadeKaupa = tekst.splitlines()
failVeebis.close()
i = 1

for nimi in ridadeKaupa:
    if i == päev:
        break
    i += 1
print("Kuupäeval", päev, ".", kuu, "on nimepäevad järgmiste nimedega inimestel: ", "\n", nimi)

