def eelarve(külalistearv):
    eelarve = 55 + külalistearv * 10
    return eelarve


külalistearv = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest tuleb? "))
print("Maksimaalne eelarve: " + str(eelarve(külalistearv)))
print("Minimaalne eelarve: " + str(eelarve(tuleb)))
