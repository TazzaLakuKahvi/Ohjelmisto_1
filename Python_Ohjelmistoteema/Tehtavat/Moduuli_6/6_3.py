def litra_laskuri():
    tulos = float(gallonat) * 3.785
    print(tulos)
    return
gallonat = input("Anna gallonien määrä: ")
while float(gallonat) >= 0:
    litra_laskuri()
    gallonat = input("Anna uusi gallonien määrä, tai lopeta ohjelma antamalla negatiivinen luku: ")
print("Ohjelma on valmis.")