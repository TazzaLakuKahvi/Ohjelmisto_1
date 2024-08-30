print("Mikä on sinun biologinen sukupuolesi sekä hemoglobiiniarvosi?")
sukupuoli = input("Sukupuoli: ")
hemoglobiini = input("Hemoglobiiniarvo (g/l): ")
if sukupuoli.lower() == "nainen" or sukupuoli.lower() == "n" or sukupuoli.lower() == "tyttö":
    if 117 <= float(hemoglobiini) <= 175:
        print("Hemoglobiini arvosi on normaali.")
    elif float(hemoglobiini) < 117:
        print("Hemoglobiini arvosi on alhainen.")
    elif float(hemoglobiini) > 175:
        print("Hemoglobiini arvosi on korkea.")
elif sukupuoli.lower() == "mies" or sukupuoli.lower() == "m" or sukupuoli.lower() == "poika":
    if 134 <= float(hemoglobiini) <= 195:
        print("Hemoglobiini arvosi on normaali.")
    elif float(hemoglobiini) < 134:
        print("Hemoglobiini arvosi on alhainen.")
    elif float(hemoglobiini) > 195:
        print("Hemoglobiini arvosi on korkea.")
else: print("Antamasi tiedot ovat virheelliset.")