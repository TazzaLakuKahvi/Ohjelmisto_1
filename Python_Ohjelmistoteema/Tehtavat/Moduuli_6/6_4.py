luvut = []
lukujen_maara = 0
def summa(maara):
    lukujen_summa = 0
    for i in range(len(maara)):
        lukujen_summa = lukujen_summa + int(luvut[i])
    print(lukujen_summa)
    return
annettu_luku = input("Anna kokonaisluku tai jätä tyhjäksi lopettaaksesi: ")
while annettu_luku != "":
    luvut.append(annettu_luku)
    lukujen_maara = lukujen_maara + 1
    annettu_luku = input("Anna kokonaisluku tai jätä tyhjäksi lopettaaksesi: ")
summa(luvut)