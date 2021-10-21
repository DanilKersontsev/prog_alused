nimi = input("Sisestage oma nimi: ")
lubat_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegel_kiirus = int(input("Sisestage tegelik kiirus (km/h):" ))
ule_kiirus = tegel_kiirus - lubat_kiirus
trahv = ule_kiirus *3
trahv_min = min(190, trahv)
print(nimi + ", kiirus ületamise eest on teie trahv " + str(trahv_min) + " eurot.")
                     