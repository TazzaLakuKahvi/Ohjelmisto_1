lentoasemat = {}
uusi_asema = 0
print("Haluatko lisätä uuden lentokentän(1), hakea jo syötettyä kenttää(2) vai lopettaa ohjelman(3)?")
paatos = int(input("Valitse yllä olevista vaihtoehdoista painamalla 1, 2 tai 3: "))

if paatos == 1:
    uusi_asema = input("Anna uusi lentokenttä")