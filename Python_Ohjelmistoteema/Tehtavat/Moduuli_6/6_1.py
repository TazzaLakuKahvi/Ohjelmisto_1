import random


def nopan_heitto():
    tulos = random.randint(1, 6)
    return tulos

print("Heitetään noppaa...")
nopan_heitto()
silmaluku = nopan_heitto()
while silmaluku != 6:
    print(f"heiton tulos oli {silmaluku}.\nHeitetään uudestaan...")
    nopan_heitto()
    silmaluku = nopan_heitto()
else:
    print(f"heiton tulos oli {silmaluku}.\nLopetetaan heittäminen.")
