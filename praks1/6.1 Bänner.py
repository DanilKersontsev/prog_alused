def banner(reklaamlause):
    return(reklaamlause.upper())

korda = int(input("Mitu korda soovite reklaamlauset kuvada?  "))
reklaamlause = input("Sisestage reklaamlause: ")

i = 1
while i <= korda:
    print(banner(reklaamlause))
    i += 1
