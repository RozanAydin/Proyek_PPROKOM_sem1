import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

siswa = []

def tambah_siswa():
    nama_siswa = input("Masukkan nama siswa    : ")
    daerah_asal = input("Masukkan daerah asal   : ")
    nama_sekolah = input("Masukkan nama sekolah  : ")
    nama_prestasi = input("Masukkan prestasi      : ")

    siswa_baru = {"nama": nama_siswa, "daerah_asal": daerah_asal, "nama_sekolah": nama_sekolah, "nama_prestasi": nama_prestasi}
    siswa.append(siswa_baru)
    bersihkan_layar()
    print("Nama siswa berhasil ditambahkan.")

def tampilkan_siswa_berprestasi():
    print("Daftar siswa berprestasi:")
    print()
    if len(siswa) == 0:
        print("Belum ada data siswa.")
    for s in siswa:
        print(f"Nama         : {s['nama']}")
        print(f"Daerah asal  : {s['daerah_asal']}")
        print(f"Nama sekolah : {s['nama_sekolah']}")
        print(f"Prestasi     : {s['nama_prestasi']}\n")

def menu_fitur3():
    while True:
        print("\n========== MENU ==========")
        print("[1.] Tambahkan nama siswa")
        print("[2.] Tampilkan siswa berprestasi")
        print("[3.] Kembali Ke Menu")

        pilihan = input("Masukkan Nomor Pilihan: ")

        if pilihan == '1':
            bersihkan_layar()
            tambah_siswa()
        elif pilihan == '2':
            bersihkan_layar()
            tampilkan_siswa_berprestasi()
        elif pilihan == '3':
            bersihkan_layar()
            break
        else:
            bersihkan_layar()
            print("Pilihan tidak valid!\n")
