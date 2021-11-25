def pronksikarva_summa(täisarv):
    summ = 0
    for mündid in täisarv:
        if int(mündid) <= 5:
            summ += int(mündid)
    return summ

failinimi = input("Sisesta failinimi: ")
fail = open(failinimi, encoding="UTF-8")
print("Hoiupõrsasse läheb " + str(pronksikarva_summa(fail)) + " senti.")
    