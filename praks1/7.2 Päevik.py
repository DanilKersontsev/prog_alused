from datetime import datetime
f = open("paevik.txt", "a", encoding="UTF-8")

sissekande = input("Sisesta sissekande tekst: ")
kuupäev_kellaaeg = datetime.today()
f.write( "\n" + str(kuupäev_kellaaeg) + "\n")
f.write(sissekande + "\n")




f.close()




