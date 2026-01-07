import os
from logika import (
    konversi_nilai,
    konversi_bobot,
    hitung_total_sks,
    total_nilai,
    hitung_ips
)

def clear():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    clear()
    print("===== MENU PROGRAM =====")
    print("1. Konversi Nilai Angka ke Huruf")
    print("2. Konversi Nilai Huruf ke Bobot")
    print("3. Hitung Total SKS")
    print("4. Hitung Total Nilai")
    print("5. Hitung IPS")
    print("0. Keluar")

    pilih = input("Pilih Menu: ")

    # ================= MENU 1 =================
    if pilih == "1":
        clear()
        nilai = float(input("Masukkan Nilai Angka: "))
        print("Nilai Huruf:", konversi_nilai(nilai))
        input("\nTekan ENTER untuk kembali ke menu...")

    # ================= MENU 2 =================
    elif pilih == "2":
        clear()
        huruf = input("Masukkan Nilai Huruf (A, B+, C): ").upper()
        print("Bobot Nilai:", konversi_bobot(huruf))
        input("\nTekan ENTER untuk kembali ke menu...")

    # ================= MENU 3 =================
    elif pilih == "3":
        clear()
        sks = []

        jumlah = int(input("Masukkan jumlah mata kuliah: "))
        for i in range(jumlah):
            s = int(input(f"SKS Mata Kuliah {i+1}: "))
            sks.append(s)

        print("\nTotal SKS =", hitung_total_sks(sks))
        input("\nTekan ENTER untuk kembali ke menu...")

    # ================= MENU 4 =================
    elif pilih == "4":
        clear()
        sks = []
        nilai = []

        jumlah = int(input("Masukkan jumlah mata kuliah: "))

        print("\n=== Input SKS ===")
        for i in range(jumlah):
            s = int(input(f"SKS Mata Kuliah {i+1}: "))
            sks.append(s)

        print("\n=== Input Nilai ===")
        for i in range(jumlah):
            n = float(input(f"Nilai Mata Kuliah {i+1}: "))
            nilai.append(n)

        print("\nTotal Nilai =", total_nilai(nilai, sks))
        input("\nTekan ENTER untuk kembali ke menu...")

    # ================= MENU 5 =================
    elif pilih == "5":
        clear()
        sks = []
        nilai = []

        jumlah = int(input("Masukkan jumlah mata kuliah: "))

        print("\n=== Input SKS ===")
        for i in range(jumlah):
            s = int(input(f"SKS Mata Kuliah {i+1}: "))
            sks.append(s)

        print("\n=== Input Nilai ===")
        for i in range(jumlah):
            n = float(input(f"Nilai Mata Kuliah {i+1}: "))
            nilai.append(n)

        print("\nIPS Mahasiswa =", round(hitung_ips(nilai, sks), 2))
        input("\nTekan ENTER untuk kembali ke menu...")

    # ================= KELUAR =================
    elif pilih == "0":
        clear()
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid!")
        input("\nTekan ENTER untuk kembali ke menu...")