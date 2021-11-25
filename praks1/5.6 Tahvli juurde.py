failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
from datetime import *
kuupäev = datetime.now().day
i = 1
for rida in fail:
    if i == kuupäev:
        print("Vastama tuleb: ", rida)
        break
    else:
        i += 1
    
        
        


    

fail.close()

