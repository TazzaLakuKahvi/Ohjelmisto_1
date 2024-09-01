#vähän epäselvää mitä tarkalleen tolla tehtävänannolla tarkoitetaan, mutta teen sen nyt vaikka näin.
#tulkitsen sen nyt, että ohjelma kysyy joka kerta tuumien määrän, eikä vain kirjoita niitä automaattisesti kunnes sanotaan toisin.
tuuma = input("anna tuumien määrä: ")
while float(tuuma) >= 0 and float(tuuma) != -0:
    print(str(tuuma),"tuumaa senttimetreinä on",str(float(float(tuuma)*float(2.54)))+".")
    tuuma = input("anna tuumien määrä:")
print("Annoit negatiivisen tuumien määrän.\nTehtävä on valmis.")