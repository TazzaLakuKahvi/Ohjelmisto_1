luku = 1
print("Tässä on kolmella jaolliset luvut väliltä 1-1000:")
while luku <= 1000:
    if float(float(luku) / 3) == int(float(luku) / 3):
        print(str(luku), "/ 3 =", str(int(luku / 3)))
    luku = luku + 1
