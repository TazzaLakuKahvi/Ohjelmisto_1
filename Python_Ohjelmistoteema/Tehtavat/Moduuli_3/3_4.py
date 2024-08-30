print("Anna vuosiluku, ja kerron onko se karkausvuosi.")
vuosi = input("Vuosi: ")
if float(int(vuosi) / 400) == int(int(vuosi) / 400):
    print(str(vuosi) + " on karkaus vuosi.")
elif float(int(vuosi) / 4) == int(int(vuosi) / 4) and float(int(vuosi) / 100) != int(int(vuosi) / 100):
    print(str(vuosi) + " on karkaus vuosi.")
else:
    print(str(vuosi) + " ei ole karkaus vuosi.")