def tervitus(järjekorranumber):
    i = 1
    while i <= järjekorranumber:
        print('Võõrustaja: "Tere!" ')
        print("Täna " + str(i) + ". kord tervitada, mõtiskleb võõrustaja" )
        print('Külaline:' + "Tere, suur tänu kutse eest!")
        i += 1
        



külaliste_arv = int(input("Sisestage külaliste arv: "))
tervitus(külaliste_arv)
