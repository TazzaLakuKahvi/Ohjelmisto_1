luku = input("Anna kokonaisluku: ")
luku = int(luku)
if luku == 0 or luku == 1:
    print(f"{luku} ei ole alkuluku")
elif luku > 1:
    for i in range(2, luku):
        if luku % i == 0:
            print(f"{luku} ei ole alkuluku")
            break
    else: print(f"{luku} on alkuluku")
else: print(f"{luku} ei ole alkuluku")