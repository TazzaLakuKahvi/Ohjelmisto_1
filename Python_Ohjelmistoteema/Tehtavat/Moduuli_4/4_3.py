luku = input("Anna luku: ")
pienempiluku = 0 + int(luku)
suurempiluku= 0 - int(luku)
while luku != "":
    if int(pienempiluku) > int(luku):
        pienempiluku = 0 + int(luku)
    if int(suurempiluku) < int(luku):
        suurempiluku = 0 + int(luku)
    luku = input("Anna luku: ")
print(f"Annetuista luvuista pienin on {pienempiluku} ja suurin luku on {suurempiluku}")
