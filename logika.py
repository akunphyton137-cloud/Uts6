def konversi_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "A-"
    elif nilai >= 75:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "B-"
    elif nilai >= 60:
     	return "C+"
    elif nilai >= 55:
     	return "C"
    elif nilai >= 45:
     	return "D"
    else :
        return "E"


def konversi_bobot(huruf):
    if huruf == "A":
        return 4.0
    elif huruf == "A-":
        return 3.75
    elif huruf == "B+":
        return 3.5
    elif huruf == "B":
        return 3.0
    elif huruf == "B-":
        return 2.75
    elif huruf == "C+":
        return 2.5
    elif huruf == "C":
        return 2.0
    elif huruf == "D":
      	return 1.0
    else:
        return 0.0


def hitung_total_sks(sks):
    total = 0
    for s in sks:
        total += s
    return total


def total_nilai(nilai, sks):
    total = 0
    for i in range(len(nilai)):
        bobot = konversi_bobot(konversi_nilai(nilai[i]))
        total += bobot * sks[i]
    return total


def hitung_ips(nilai, sks):
    total_sks = hitung_total_sks(sks)
    if total_sks == 0:
        return 0
    return total_nilai(nilai, sks) / total_sks