
fail = open("rebased.txt", encoding="UTF-8")

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

aasta1 = 2011

for rida in fail:
    if aasta == aasta1:
        break
    aasta1 += 1
print(aasta1, "aastal oli vastuvõetuid", rida)
        


    

fail.close()