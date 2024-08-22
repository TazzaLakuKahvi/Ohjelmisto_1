print("Tämä ohjelma laskee leivisköjen määrän kilogrammoina ja grammoina.\nAnna leivisköjen määrä, kiitos.")
leiviska = input("leivisköjen määrä: ")
naula = input("naulojen määrä: ")
luoti = input("luotien määrä: ")
luodinpaino = float(luoti) * 13.3
naulanpaino = float(naula) * 13.3 * 32
leiviskanpaino = float(leiviska) * 13.3 * 32 * 20
kokonaispaino = luodinpaino + naulanpaino + leiviskanpaino