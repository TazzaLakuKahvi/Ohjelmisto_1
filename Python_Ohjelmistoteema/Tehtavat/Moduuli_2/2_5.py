print("Tämä ohjelma laskee leivisköjen, naulojen ja luotien massan kilogrammoina ja grammoina.")
print("Anna mittojen määrä, kiitos.")
leiviska = input("leivisköjen määrä: ")
naula = input("naulojen määrä: ")
luoti = input("luotien määrä: ")
luodinpaino = float(luoti) * 13.3
naulanpaino = float(naula) * 13.3 * 32
leiviskanpaino = float(leiviska) * 13.3 * 32 * 20
kokonaispaino = luodinpaino + naulanpaino + leiviskanpaino
kilot = int(kokonaispaino / 1000)
grammat = kokonaispaino - (kilot * 1000)
print(f"Massa nykymittojen mukaan: {kilot}kg {grammat:.2f}g")
