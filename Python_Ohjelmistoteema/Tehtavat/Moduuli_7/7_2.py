nimet = set()
kysymys = "Anna nimi tai jätä tyhjäksi lopettaaksesi ohjelman: "
uusi = "Uusi nimi"
vanha = "Aiemmin syötetty nimi"
nimi = input(kysymys)
print(uusi)
while nimi != "":
    nimet.add(nimi)
    nimi = input(kysymys)
    if nimi == "":
        break
    elif nimi not in nimet and nimi != "":
        print(uusi)
    else:
        print(vanha)
for i in nimet:
    print(i)