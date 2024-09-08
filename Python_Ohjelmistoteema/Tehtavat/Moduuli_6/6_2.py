import random


def nopan_heitto():
    tulos = random.randint(1, tahkot)
    return tulos
tahkot = input("Kirjoita kuinka monta tahkoa haluat nopassa olevan: ")
tahkot = int(tahkot)
print("Heitetään noppaa...")
nopan_heitto()
silmaluku = nopan_heitto()

while silmaluku != tahkot:
    print(f"heiton tulos oli {silmaluku}.\nHeitetään uudestaan...")
    nopan_heitto()
    silmaluku = nopan_heitto()
else:
    print(f"heiton tulos oli {silmaluku}.\nLopetetaan heittäminen.")
