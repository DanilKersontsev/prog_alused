vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ").upper()
treeningtüüp = int(input("Sisestage treeningu tüüp(1,2,3): "))

if (sugu == "M"):
    tervisetreening = 220 - vanus
if (sugu == "N"):
    tervisetreening = 206 - (vanus * 0.88)

if treeningtüüp == 1:
    tervisetreening_min = round(tervisetreening * 0.5)
    tervisetreening_max = round(tervisetreening * 0.7)
if treeningtüüp == 2:
    tervisetreening_min = round(tervisetreening * 0.7)
    tervisetreening_max = round(tervisetreening * 0.8)
if treeningtüüp == 3:
    tervisetreening_min = round(tervisetreening * 0.8)
    tervisetreening_max = round(tervisetreening * 0.87)
print("Pulsisagedus peaks olema vahemikus " + str(tervisetreening_min) + " kuni " + str(tervisetreening_max) + ".")