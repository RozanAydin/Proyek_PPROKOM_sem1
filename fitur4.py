import os
import datetime

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

daftar_lomba = []

def deadline():
    while True:
        print("\nMasukkan tenggat lomba")
        tahun = input("Masukkan tahun: ")
        bulan = input("Masukkan bulan (1-12): ")
        tanggal = input("Masukkan tanggal (1-31): ")
        jam = input("Masukkan jam (0-23): ")
        menit = input("Masukkan menit (0-59): ")

        if tahun.isdigit() and bulan.isdigit() and tanggal.isdigit() and jam.isdigit() and menit.isdigit():
            tahun = int(tahun)
            bulan = int(bulan)
            tanggal = int(tanggal)
            jam = int(jam)
            menit = int(menit)

            if 1 <= bulan <= 12:
                if 1 <= tanggal <= 31:
                    if (bulan == 2 and tanggal > 29) or (bulan in [4, 6, 9, 11] and tanggal > 30):
                        print("Tanggal tidak valid! Bulan tersebut hanya memiliki 30 hari.")
                        continue
                    if bulan == 2 and tanggal == 29 and not (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)):
                        print("Tanggal tidak valid! Tahun tersebut bukan tahun kabisat.")
                        continue
                    if 0 <= jam <= 23 and 0 <= menit <= 59:
                        global tenggat
                        tenggat = datetime.datetime(tahun, bulan, tanggal, jam, menit)
                        return tenggat
                    else:
                        print("Jam atau menit tidak valid! Pastikan jam 0-23, dan menit 0-59.")
                else:
                    print("Tanggal harus antara 1 dan 31.")
            else:
                print("Bulan harus antara 1 dan 12.")
        else:
            print("Input tidak valid! Pastikan Anda memasukkan angka yang benar.")

def input_lomba():
    global lomba
    while True:
        nama = input("Silahkan masukkan nama lomba: ")
        deskripsi = input("Silakan masukkan deskripsi lomba: ")
        syarat = input("Silakan masukkan syarat lomba: ")
        alamat = input("Silahkan masukkan alamat pengiriman: ")
        deadline()

        lomba = {
            "nama" : nama,
            "deskripsi" : deskripsi,
            "syarat" : syarat,
            "alamat"  : alamat,
            "tenggat" : tenggat
        }
        daftar_lomba.append(lomba)
        print("Lomba berhasil ditambahkan")
        while True:
            pilihan = input("\nInput lomba lain? [Y/N]")
            if pilihan.capitalize() == "Y":
                bersihkan_layar()
                break
            elif pilihan.capitalize() == "N":
                bersihkan_layar()
                return
            else:
                print("Input Salah! Masukkan hanya 'Y' atau 'N'.")

def lihat_lomba():
    if daftar_lomba:
        print("\n======== DAFTAR LOMBA ========")
        sekarang = datetime.datetime.now()
        for lomba in daftar_lomba:
            if sekarang >= lomba['tenggat']:
                daftar_lomba.remove(lomba)
        
        for lomba in daftar_lomba:
            print(f"Nama        :{lomba['nama']}")
            print(f"Deskripsi   :{lomba['deskripsi']}")
            print(f"Syarat      :{lomba['syarat']}")
            print(f"Tenggat     :{lomba['tenggat']}")
            print(f"Kirim ke    :{lomba['alamat']}\n")
    else:
        print("Belum ada lomba yang terdaftar")


def menu_fitur4():
    while True:
        print("\n") 
        print("===== Menu Relung Kompetisi =====") 
        print("[1] Input Lomba")
        print("[2] Lihat Lomba")
        print("[3] Kembali Ke Menu")
        menu = (input("Masukkan Nomor Pilihan: "))
        print("\n")

        if menu == "1": 
            bersihkan_layar()
            input_lomba()
        elif menu == "2": 
            bersihkan_layar()
            lihat_lomba() 
        elif menu == "3":
            bersihkan_layar()
            break
        else:
            bersihkan_layar()
            print("Pilihan tidak valid!\n")
