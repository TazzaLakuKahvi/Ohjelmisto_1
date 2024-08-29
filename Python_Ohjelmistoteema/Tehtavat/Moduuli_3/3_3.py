print("Mikä on sinun biologinen sukupuolesi sekä hemoglobiiniarvosi?")
sukupuoli = input("Sukupuoli: ")
hemoglobiini = input("Hemoglobiiniarvo (g/l): ")
if sukupuoli.lower() == "nainen" or "n" or "tyttö":
    if int(117) <= float(hemoglobiini) <= int(175):
        print("Hemoglobiini arvosi on normaali.")
    elif float(hemoglobiini) < float(117):
        print("Hemoglobiini arvosi on alhainen.")
    elif float(hemoglobiini) > float(175):
        print("Hemoglobiini arvosi on korkea.")
elif sukupuoli.lower() == "mies" or "m" or "poika":
    if int(134) <= float(hemoglobiini) <= int(195):
        print("Hemoglobiini arvosi on normaali.")
    elif float(hemoglobiini) < float(134):
        print("Hemoglobiini arvosi on alhainen.")
    elif float(hemoglobiini) > float(195):
        print("Hemoglobiini arvosi on korkea.")
else: print("Antamasi tiedot ovat virheelliset.")