

täringute_arv = int(input("Sisestage täringu arvu: "))
from random import randint
i = 0
while i < täringute_arv:
    f = randint(1, 6)
    i += 1
    print(f)
    
