from random import randint

istekoha_valik = str(input("Kas soovite istekohta ise valida (ise) või loosida (loos)?  "))


if istekoha_valik == "ise":
    istekoha_valik = str(input("Kas soovite istuda akna ääres (aken) või mitte (muu)?  "))
else:
    if randint(1, 3) == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")
if istekoha_valik == "aken":
    print("Valisite ise. Aknakoht")
elif istekoha_valik == "muu":
    print("Valisite ise. Vahekäigukoht")
