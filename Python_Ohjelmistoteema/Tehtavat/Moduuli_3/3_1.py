print("Anna kalastamasi kuhan pituus, ole hyvä.")
kuhanpituus = input("Kuhan pituus (cm): ")
if float(kuhanpituus) < 37:
    print("Kuhasi on liian pieni.\nLaske kuha takaisin järveen.")
else:
    print("Kuhasi on syömäkelpoisen pituinen.\nHae perkaus tarvikkeet ja pannu.")
