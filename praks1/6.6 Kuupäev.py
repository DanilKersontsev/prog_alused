def kuu_nimi(järjekorranumber):
    kuu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuu[int(järjekorranumber) - 1]

def kuupäev_sõnena(kuupäev):
    kuud = kuupäev.split(".")
    kuupäev = kuud[0] + "." + kuu_nimi(kuud[1]) + " " + kuud[2] + "." + "a"
    return kuupäev


kuupäev = str(input("Sisesta kuupäeva kujul DD.MM.YYYY: "))
print(str(kuupäev_sõnena(kuupäev)))
    