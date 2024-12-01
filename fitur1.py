import os

materi_pembelajaran = []

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("\n========== MENU ==========")
    print("[1.] Tambah Materi Pembelajaaran ")
    print("[2.] Lihat Materi Pembelajaran")
    print("[3.] Revisi Materi Pembelajaran")
    print("[4.] Kembali Ke Menu")

def tambah_materi():
    judul = input("Masukkan judul materi: ")
    isi = input("Masukkan isi materi: ")
    materi = {"judul": judul, "isi": isi}
    materi_pembelajaran.append(materi)
    print("Materi berhasil ditambahkan.\n")

def lihat_semua_materi():
    if materi_pembelajaran:
        print("\nDaftar Materi:")
        for i, materi in enumerate(materi_pembelajaran, start=1):
            print(f"{i}. {materi['judul']}")
    else:
        print(" ")

def lihat_isi_materi():
    while True:
        if materi_pembelajaran:
            try:
                nomor = int(input("Masukkan nomor materi yang ingin dilihat, ketik -1 untuk keluar: ")) - 1
                if 0 <= nomor < len(materi_pembelajaran):
                    materi = materi_pembelajaran[nomor]
                    print(f"\nJudul: {materi['judul']}")
                    print(f"Isi: {materi['isi']}\n")
                elif nomor == -2:
                    break
                else:
                    print("Nomor materi tidak valid.\n")
            except ValueError:
                print("Masukkan nomor yang valid.\n")
        else:
            print("Belum ada materi yang tersedia.\n")
            break

def revisi_materi():
    if materi_pembelajaran:
        while True:
            try:
                nomor = int(input("Masukkan nomor materi yang ingin direvisi: ")) - 1
                if 0 <= nomor < len(materi_pembelajaran):
                    materi = materi_pembelajaran[nomor]
                    print(f"\nJudul saat ini: {materi['judul']}")
                    print(f"Isi saat ini: {materi['isi']}")
                    
                    judul_baru = input("Masukkan judul baru (tekan Enter jika tidak ada perubahan): ")
                    isi_baru = input("Masukkan isi baru (tekan Enter jika tidak ada perubahan): ")
                    
                    if judul_baru:
                        materi["judul"] = judul_baru
                    if isi_baru:
                        materi["isi"] = isi_baru
                    
                    print("Materi berhasil diperbarui.\n")
                    break
                else:
                    print("Nomor materi tidak valid.\n")
            except ValueError:
                print("Masukkan nomor yang valid.\n")
    else:
        print("Belum ada materi yang tersedia.\n")

def menu_fitur1():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan Nomor Pilihan: ")
        
        if pilihan == '1':
            bersihkan_layar()
            tambah_materi()
        elif pilihan == '2':
            bersihkan_layar()
            lihat_semua_materi()
            lihat_isi_materi()
        elif pilihan == '3':
            bersihkan_layar()
            lihat_semua_materi()
            revisi_materi()
        elif pilihan == '4':
            bersihkan_layar()
            break
        else:
            bersihkan_layar()
            print("Pilihan tidak valid.\n")
