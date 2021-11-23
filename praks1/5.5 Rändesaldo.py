sisse = open("sisseranne.txt", encoding="UTF-8")
välja = open("valjaranne.txt", encoding="UTF-8")
ads = []
ränne = 1
for element_sisse in sisse:
    #print(element_sisse)
    for element_valja in välja:
        #print(element_valja)
        vahe = int(element_sisse) - int(element_valja)
        ads.append(vahe)
        break
    print()
    
    
sisse.close()
välja.close()
print(ads)

print("Suurim positiivne rändesaldo oli", ads.index(max(ads))+1,"." , "aastal.",)
