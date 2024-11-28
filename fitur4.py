import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

daftar_lomba = []

def input_lomba():
    while True:
        nama = input("Silahkan masukkan nama lomba: ")
        deskripsi = input("Silakan masukkan deskripsi lomba: ")
        syarat = input("Silakan masukkan syarat lomba: ")
        tenggat = input("Silakan masukkan tenggat lomba: ")
        alamat = input("Silakan masukkan alamat pengiriman: ")

        lomba = {
            "nama" : nama,
            "deskripsi" : deskripsi,
            "syarat" : syarat,
            "tenggat" : tenggat
        }
        daftar_lomba.append(lomba)
        print("Lomba berhasil ditambahkan")
        pilihan = input("\nInput lomba lain? [Y/N]")
        if pilihan.capitalize() == "Y":
            continue
        elif pilihan.capitalize() == "N":
            break
        else:
            print("Input Salah!")

def lihat_lomba():
    if daftar_lomba:
        print("\n======== DAFTAR LOMBA ========")
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
        print("========== MENU ==========") 
        print("[1] Input Lomba")
        print("[2] Lihat Lomba")
        print("[3] Kembali Ke Menu")
        menu = (input("PILIH MENU> "))
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
