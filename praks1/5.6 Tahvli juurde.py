failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")
from datetime import *
kuupäev = int(datetime.now().day)
i = 0
for rida in fail:
    if rida == kuupäev:
        print("Vastama tuleb: ", rida )
    else:
        print("Vastama tuleb: ", rida)
        i += 1
    break
        
    


    
    
    
    
    
fail.close()

