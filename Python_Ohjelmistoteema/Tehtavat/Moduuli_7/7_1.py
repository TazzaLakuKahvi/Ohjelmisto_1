vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausi = int(input("Anna kuukauden numero (1-12): "))
kuukausi_muunnos = 0
if 0 < kuukausi <= 2 or kuukausi == 12:
    kuukausi_muunnos = 1
elif 3 <= kuukausi <= 5:
    kuukausi_muunnos = 2
elif 6 <= kuukausi <= 8:
    kuukausi_muunnos = 3
elif 9 <= kuukausi <= 11:
    kuukausi_muunnos = 4
else: print("Annettu luku ei vastaa olemassa olevaa kuukautta.")

vuodenaika = vuodenajat[kuukausi_muunnos-1]
if 1 <= kuukausi <= 12:
    print(f"{kuukausi}. kuukausi on {vuodenaika}")