print("Tämä ohjelma laskee ympyrän pinta-alan säteen perusteella.\nKerro ympyrän säde, ole hyvä.")
sade_str = input("Säde: ")
sade = float(sade_str)
import math
pintaala = float(math.pi*sade**2)
print(f"Pintaala: {pintaala}")