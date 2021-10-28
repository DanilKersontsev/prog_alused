kirja_suurus = float(input("Sisestage kirja suurus(MB): "))
kirja_teema = input("Sisestage kirja teema pealkiri: ")
kirjaga_fail = input("Kas kirjaga on kaasas fail? ")

if kirja_teema == "" or kirjaga_fail == "jah" and kirja_suurus > 1:
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")

