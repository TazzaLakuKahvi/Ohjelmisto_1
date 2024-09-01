print("Anna käyttäjätunnus ja salasana")
yritykset = 1
kayttajatunnus = input("Käyttäjätunnus: ")
salasana = input("Salasana: ")
while yritykset < 5 and kayttajatunnus != "python" and salasana != "rules":
        print(f"Salasana tai käyttäjä tunnus on väärin\n{5 - yritykset} yritystä jäljellä")
        yritykset = yritykset + 1
        kayttajatunnus = input("Käyttäjätunnus: ")
        salasana = input("Salasana: ")
if yritykset >= 5:
    print("Pääsy evätty")
if kayttajatunnus == "python" and salasana == "rules":
    print("Tervetuloa")