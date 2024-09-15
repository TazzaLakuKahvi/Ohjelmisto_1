def parilliset(annettu_lista):
    lista_parillisia = []
    for i in annettu_lista:
        if int(i) % 2 == 0:
            lista_parillisia.append(i)
    return lista_parillisia


luvut = []
kysymys = "Anna kokonaisluku tai jätä tyhjäksi lopettaaksesi: "
annettu_luku = input(kysymys)
# Isä neuvoi mahdollisten errorien välttämisestä, niin jätän tämän try toiminnon tähän myöhemmäksi referenssiksi.
while annettu_luku != "":
    try:
        luvut.append(int(annettu_luku))
    except ValueError:
        print(f"{annettu_luku} ei ole kokonaisluku.")
    annettu_luku = input(kysymys)
print(parilliset(luvut))
