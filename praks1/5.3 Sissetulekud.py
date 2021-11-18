fail = open("konto.txt", encoding="UTF-8")
for posarv in fail:
    if float(posarv) > 0:
        print(posarv[:])
    
    
    



fail.close()