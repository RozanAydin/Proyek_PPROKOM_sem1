import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def soal_survei():
    global daftar_soal
    global poin
    poin = []
    global poin_jawaban
    poin_jawaban = 0
    print("Tuliskan angka dari skala yang telah disediakan!")

    soal_1 = """Kondisi Ruang Kelas
    Bagaimana kondisi ruang kelas di sekolah ini?
    [4] Sangat Baik (terawat, cukup luas, pencahayaan dan ventilasi memadai)
    [3] Baik (terawat, ventilasi cukup)
    [2] Cukup (butuh perbaikan pada beberapa aspek)
    [1] Buruk (kondisi ruang kelas tidak layak)"""

    soal_2 = """Ketersediaan Fasilitas Teknologi
    Apakah sekolah ini memiliki fasilitas teknologi yang memadai untuk mendukung proses belajar mengajar?
    [4] Sangat Memadai (komputer, internet, proyektor, dan peralatan multimedia lainnya tersedia)
    [3] Memadai (komputer dan internet tersedia)
    [2] Kurang Memadai (beberapa fasilitas teknologi ada tetapi terbatas)
    [1] Tidak Memadai (tidak ada fasilitas teknologi yang memadai)"""

    soal_3 = """Kondisi Perpustakaan
    Bagaimana kondisi perpustakaan di sekolah ini?
    [4] Sangat Baik (terawat, koleksi buku lengkap dan bervariasi)
    [3] Baik (terawat, koleksi buku cukup)
    [2] Cukup (koleksi buku terbatas, ruangan kurang nyaman)
    [1] Buruk (koleksi buku sedikit, ruang perpustakaan tidak nyaman)"""

    soal_4 = """Fasilitas Kesehatan
    Apakah sekolah memiliki fasilitas kesehatan yang memadai untuk mendukung kesehatan siswa?
    [4] Sangat Memadai (ada ruang UKS lengkap dengan peralatan medis dan tenaga medis)
    [3] Memadai (ada ruang UKS dengan beberapa fasilitas dasar)
    [2] Kurang Memadai (ruang UKS terbatas dan fasilitas kesehatan kurang lengkap)
    [1] Tidak Memadai (tidak ada ruang UKS atau fasilitas kesehatan)"""

    soal_5 = """Fasilitas Olahraga
    Apakah fasilitas olahraga yang tersedia di sekolah ini cukup untuk mendukung kegiatan olahraga siswa?
    [4] Sangat Memadai (beragam fasilitas olahraga tersedia, lapangan, peralatan olahraga lengkap)
    [3] Memadai (beberapa fasilitas olahraga ada, lapangan cukup baik)
    [2] Kurang Memadai (lapangan terbatas, peralatan olahraga kurang lengkap)
    [1] Tidak Memadai (tidak ada fasilitas olahraga)"""

    soal_6 = """Ketersediaan Air Bersih
    Bagaimana kondisi pasokan air bersih di sekolah ini?
    [4] Sangat Baik (air bersih tersedia secara cukup dan terjaga kualitasnya)
    [3] Baik (air bersih tersedia, namun kualitas kadang kurang)
    [2] Cukup (air bersih terbatas, kualitas kadang bermasalah)
    [1] Buruk (air bersih sulit didapat atau kualitas buruk)"""

    soal_7 = """Kondisi Sanitasi dan Kamar Mandi
    Bagaimana kondisi fasilitas sanitasi dan kamar mandi di sekolah ini?
    [4] Sangat Baik (kamar mandi bersih, cukup jumlahnya, dan terawat)
    [3] Baik (kamar mandi cukup bersih, sedikit kurang jumlahnya)
    [2] Cukup (kamar mandi kurang bersih, perlu perbaikan)
    [1] Buruk (kamar mandi tidak bersih, jumlah terbatas)"""

    soal_8 = """Keamanan Sekolah
    Bagaimana tingkat keamanan sekolah ini dalam mendukung kegiatan belajar mengajar?
    [4] Sangat Aman (keamanan terjamin, dilengkapi dengan petugas dan sistem keamanan)
    [3] Aman (keamanan cukup, ada petugas atau sistem pengawasan)
    [2] Kurang Aman (keamanan terbatas, kurang pengawasan)
    [1] Tidak Aman (keamanan tidak terjamin, tidak ada sistem pengawasan)"""

    soal_9 = """Fasilitas Parkir
    Bagaimana kondisi fasilitas parkir di sekolah ini?
    [4] Sangat Memadai (parkir luas dan teratur untuk kendaraan motor dan mobil)
    [3] Memadai (parkir cukup luas untuk kendaraan motor)
    [2] Kurang Memadai (parkir terbatas, sering penuh)
    [1] Tidak Memadai (tidak ada fasilitas parkir yang memadai)"""

    soal_10 = """Ketersediaan Ruang Ekstrakurikuler
    Apakah sekolah ini menyediakan ruang yang memadai untuk kegiatan ekstrakurikuler?
    [4] Sangat Memadai (ada ruang khusus untuk berbagai kegiatan ekstrakurikuler)
    [3] Memadai (ruang tersedia, namun terbatas)
    [2] Kurang Memadai (kegiatan ekstrakurikuler terbatas pada ruang yang tidak memadai)
    [1] Tidak Memadai (tidak ada ruang yang mendukung kegiatan ekstrakurikuler)"""

    daftar_soal = [soal_1, soal_2, soal_3, soal_4, soal_5,soal_6,soal_7,soal_8,soal_9,soal_10]

    for soal in daftar_soal:
        print(soal)
        jawaban_valid = False
        while not jawaban_valid:
            jawaban = input("Masukkan angka yang sesuai dengan kondisi fasilitas: ")
            if jawaban.isdigit():
                jawaban = int(jawaban)
                if 1 <= jawaban <= 4:
                    poin_jawaban += jawaban
                    poin.append(jawaban)
                    bersihkan_layar()
                    jawaban_valid = True
                else:
                    print("Input tidak valid, masukkan angka antara 1 hingga 4.")
            else:
                print("Input tidak valid, masukkan angka.")

    print("Terima Kasih karena telah mengisi survei")
    print("")

def lihat_jawaban():
    if not daftar_sekolah:
        print("Data Survei Belum Tersedia")
        return
    
    lihat_survei()
    while True:
        try:
            pilihan = int(input("Pilih Survei berdasarkan indexnya: "))
            if 1 <= pilihan <= len(daftar_sekolah):
                bersihkan_layar()
                data_terpilih = sorted(daftar_sekolah, key=lambda x: x['Skala'])[pilihan - 1]
                print("\n======== DETAIL SURVEI ========")
                print(f"Nama Pengisi    : {data_terpilih['Nama']}")
                print(f"Sekolah         : {data_terpilih['Sekolah']}")
                print(f"Alamat Sekolah  : {data_terpilih['Alamat_Sekolah']}")
                print(f"Poin Kelayakan  : {data_terpilih['Skala']}")
                print(f"Catatan         : {data_terpilih['Catatan']}\n")

                print("========== JAWABAN SURVEI ==========")
                for i, (soal, nilai) in enumerate(zip(daftar_soal, poin), start=1):
                    print(f"{i}. {soal}\n   Poin: {nilai}\n")
                    input("")
                break
            else:
                print("Indeks tidak valid. Silakan pilih indeks yang tersedia.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka indeks.")


daftar_sekolah = []
def isi_survei():
    print("Selamat datang di fitur Isi Survei!")
    nama = input("Silahkan masukkan Nama: ")
    sekolah = input("Silahkan masukkan nama Sekolah: ")
    daerah = input("Silahkan masukkan Alamat Sekolah: ")
    bersihkan_layar()
    soal_survei()
    catatan = input("Silahkan tambahkan catatan mengenai sekolah tersebut: ")
    bersihkan_layar()
    data = {
        "Nama":nama,
        "Sekolah":sekolah,
        "Alamat_Sekolah":daerah,
        "Skala":poin_jawaban,
        "Catatan":catatan
    }
    daftar_sekolah.append(data)

def lihat_survei():
    if daftar_sekolah:
        print("\n======== DATA SURVEI ========")
        daftar_sekolah_sorted = sorted(daftar_sekolah, key=lambda x: x['Skala'])
        for i, data in enumerate(daftar_sekolah_sorted, start=1):
            print(f"Index           : {i}")
            print(f"Nama Pengisi    : {data['Nama']}")
            print(f"Sekolah         : {data['Sekolah']}")
            print(f"Alamat Sekolah  : {data['Alamat_Sekolah']}")
            print(f"Poin Kelayakan  : {data['Skala']}")
            print(f"Catatan         : {data['Catatan']}\n")
    else:
        print("Data Survei Belum Tersedia")

def menu_fitur2():
    while True:
        print("\n") 
        print("===== Menu Relung Opini =====") 
        print("[1] Isi Survei")
        print("[2] Lihat Hasil Survei")
        print("[3] Lihat Jawaban")
        print("[4] Kembali Ke Menu")
        pilih = input("Masukkan Nomor Pilihan: ")
        print("\n")

        if pilih == "1":
            bersihkan_layar()
            isi_survei()
        elif pilih == "2":
            bersihkan_layar()
            lihat_survei()
        elif pilih == "3":
            bersihkan_layar()
            lihat_jawaban()
        elif pilih == "4":
            bersihkan_layar()
            break
        else:
            bersihkan_layar()
            print("Pilihan tidak valid!\n")
