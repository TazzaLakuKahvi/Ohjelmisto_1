import math


def yksikkohinta(halkaisija, hinta):
    pitsan_pinta_ala_metri = float(halkaisija) / 100 * math.pi
    pitsan_yksikkohinta = float(hinta) / pitsan_pinta_ala_metri
    return pitsan_yksikkohinta


halkaisija_kysymys = "pitsan halkaisija senttimetreinä: "
hinta_kysymys = "pitsan hinta euroina: "
pitsan_halkaisija1 = input("Anna " + halkaisija_kysymys)
pitsan_hinta1 = input("Anna " + hinta_kysymys)
pitsan_halkaisija2 = input("Anna toisen" + halkaisija_kysymys)
pitsan_hinta2 = input("Anna toisen" + hinta_kysymys)

print(f"Pitsan 1 yksikköhinta on: {yksikkohinta(pitsan_halkaisija1, pitsan_hinta1)}")
print(f"Pitsan 2 yksikköhinta on: {yksikkohinta(pitsan_halkaisija2, pitsan_hinta2)}")

if yksikkohinta(pitsan_halkaisija1, pitsan_hinta1) < yksikkohinta(pitsan_halkaisija2, pitsan_hinta2):
    print("Pitsa numero yhdestä saat paremman vastineen rahallesi.")
elif yksikkohinta(pitsan_halkaisija1, pitsan_hinta1) == yksikkohinta(pitsan_halkaisija2, pitsan_hinta2):
    print("Pitsat ovat kokoonsa nähden saman arvoisia.")
else:
    print("Pitsa numero kahdesta saat paremman vastineen rahallesi")
