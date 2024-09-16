lentoasemat = {}
uusi_asema = 0

print("Haluatko lisätä uuden lentokentän(uusi), hakea jo syötettyä kenttää(hae) vai lopettaa ohjelman(lopeta)?")
paatos_teksti = "Valitse yllä olevista vaihtoehdoista syöttämällä uusi, hae tai lopeta: "
paatos = input(paatos_teksti)
paatos = paatos.lower()

while paatos != "lopeta":
    if paatos == "uusi":
        uusi_koodi = input("Anna uuden lentokentän ICAO-koodi: ")
        uusi_koodi = uusi_koodi.upper()
        uusi_asema = input("Anna uuden lentokentän nimi: ")+" lentokenttä"
        lentoasemat[uusi_koodi] = uusi_asema
    elif paatos == "hae":
        haku = input("Anna haettavan lentokentän ICAO-koodi: ")
        haku = haku.upper()
        if haku in lentoasemat:
            print(f"{haku}-koodia vastaava lentokenttä on {lentoasemat[haku]}.")
        else:
            print(f"Koodille {haku} ei löydy vastaavaa lentokenttää.")
    else: print("Annettulle päätökselle ei ole komentoa.")
    paatos = input(paatos_teksti)

print("Lopetetaan ohjelma...\nOhjelma lopetettu.")
