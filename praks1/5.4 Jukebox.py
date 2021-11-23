
failinimi = input("Palun sisestage failinimi(jukebox.txt,80ndad.txt, eesti_muusika.txt, edm.txt): ")

fail = open(failinimi, encoding="UTF-8")
print("Muusikapalade valik: ")
i = 1
for rida in fail:
    print(i,".",rida)
    i += 1
    
jarjekorranumber = int(input("Valige laulu järjekorranumber: "))
fail.close()
fail = open(failinimi, encoding ="UTF-8")
a = 1
for rida in fail:
    if a == jarjekorranumber:
        print("Mängitav muusikapala on ", rida )
        break
    else:
        a += 1
    
    


fail.close()



