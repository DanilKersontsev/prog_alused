def mahlapakkide_arv(õuntekogus):
    mahlapakkide_arv = õuntekogus * 0.4/3
    return round(mahlapakkide_arv)


õuntekogus = float(input("Mitu kilogrammi õunu on? "))
print(mahlapakkide_arv(õuntekogus))

