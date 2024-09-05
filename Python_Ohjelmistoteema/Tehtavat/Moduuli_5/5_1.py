import random
heitot = input("Anna heitettävien noppien määrä: ")
noppa = random.randint(1,6)
summa = 0
heitot_teksti = 1
for i in range(int(heitot)):
    print(f"Noppa {heitot_teksti} on {noppa}")
    summa = summa + noppa
    noppa = random.randint(1,6)
    heitot_teksti = heitot_teksti + 1
print(f"Noppien silmälukujen yhteen laskettu summa on {summa}.")
