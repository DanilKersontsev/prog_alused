pöialpoissi = int(input("Mitu pöialpoissi tahab õunu? "))
from random import randint
i = 0
õun = 14
while i < pöialpoissi:
    i += 1
    p = randint(1, 2)
    õun = õun - p
    print(p)
print("Lumivalgekesele jäi " + str(õun))
