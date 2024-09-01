print("Tämä peli valitsee luvun 1-10 väliltä.\nSinun tehtäväsi on arvata mikä tämä luku on.\nOhjelma kertoo oliko arvaus liian pieni vai suuri.")
import random
numero = random.randint(1, 10)
arvaus = input("Arvaa numero: ")
while int(arvaus) != numero:
    if int(arvaus) < numero:
        print("Liian pieni arvaus")
    elif int(arvaus) > numero:
        print("Liian suuri arvaus")
    arvaus = input("Arvaa numero: ")
print("Oikein")