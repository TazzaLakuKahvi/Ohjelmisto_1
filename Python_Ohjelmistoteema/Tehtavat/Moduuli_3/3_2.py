print("Mikä on varaamanne hytin luokka?\n(LUX,A,B,C)")
luokka = input("hytin luokka: ")
if luokka.upper() == str("LUX"): print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka.upper() == str("A"): print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka.upper() == str("B"): print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka.upper() == str("C"): print("C on ikkunaton hytti autokannen alapuolella.")
else: print("Virheellinen hyttiluokka")