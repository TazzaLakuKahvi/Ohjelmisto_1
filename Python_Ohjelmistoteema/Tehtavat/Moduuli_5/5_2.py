luvut = []
luku = input("Anna luku tai jätä kenttä tyhjäksi päättääksesi ohjelman: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna seuraava luku tai jätä kenttä tyhjäksi päättääksesi ohjelman: ")
    luvut.sort(reverse=True)
print(f"Annetuista luvuista suurimmasta pienimpään viisi suurinta ovat {luvut[0:5]}.")
