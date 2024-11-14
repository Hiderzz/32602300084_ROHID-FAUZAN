# Kelas Kamar
class Kamar:
    def __init__(self, nomor_kamar, tipe_kamar):
        print(f"Membuat Kamar dengan nomor: {nomor_kamar} dan tipe: {tipe_kamar}")
        self.nomor_kamar = nomor_kamar
        self.tipe_kamar = tipe_kamar
        self.harga_per_malam = self.tentukan_harga(tipe_kamar)
        self.status = 'tersedia' 

    def tentukan_harga(self, tipe_kamar):
        tipe_kamar = tipe_kamar.lower()
        if tipe_kamar == "single":
            return 200000
        elif tipe_kamar == "double":
            return 350000
        elif tipe_kamar == "suite":
            return 500000
        else:
            return 0

    def tampilkan_info_kamar(self):
        print(f"Kamar No: {self.nomor_kamar}, Tipe: {self.tipe_kamar}, Harga: {self.harga_per_malam}, Status: {self.status}")

# Kelas Tamu
class Tamu:
    def __init__(self, nama, nomor_identitas, kontak):
        print(f"Menambahkan Tamu dengan nama: {nama}")
        self.nama = nama
        self.nomor_identitas = nomor_identitas
        self.kontak = kontak
        self.daftar_reservasi = []

    def tampilkan_info_tamu(self):
        print(f"Nama: {self.nama}, ID: {self.nomor_identitas}, Kontak: {self.kontak}")
        if self.daftar_reservasi:
            print("Reservasi Aktif:")
            for reservasi in self.daftar_reservasi:
                reservasi.tampilkan_info_reservasi()
        else:
            print("Tidak ada reservasi aktif")

# Kelas Reservasi
class Reservasi:
    def __init__(self, tamu, kamar, tanggal_check_in, tanggal_check_out):
        print(f"Membuat Reservasi untuk tamu {tamu.nama} pada kamar {kamar.nomor_kamar}")
        self.tamu = tamu
        self.kamar = kamar
        self.tanggal_check_in = tanggal_check_in
        self.tanggal_check_out = tanggal_check_out
        self.status = 'aktif'  

    def tampilkan_info_reservasi(self):
        print(f"Reservasi: {self.tamu.nama} memesan {self.kamar.tipe_kamar} (No: {self.kamar.nomor_kamar})")
        print(f"Check-in: {self.tanggal_check_in}, Check-out: {self.tanggal_check_out}, Status: {self.status}")

# Kelas Hotel
class Hotel:
    def __init__(self):
        print("Hotel sistem diinisialisasi.")
        self.daftar_kamar = []
        self.daftar_tamu = []
        self.daftar_reservasi = []

    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)
        print("Kamar ditambahkan!")

    def tambah_tamu(self, tamu):
        self.daftar_tamu.append(tamu)
        print("Tamu baru didaftarkan!")

    def buat_reservasi(self, tamu, kamar, tanggal_check_in, tanggal_check_out):
        if kamar.status == 'tersedia':
            reservasi = Reservasi(tamu, kamar, tanggal_check_in, tanggal_check_out)
            self.daftar_reservasi.append(reservasi)
            tamu.daftar_reservasi.append(reservasi)
            kamar.status = 'dipesan'
            print("Reservasi berhasil dibuat!")
        else:
            print("Kamar tidak tersedia.")

    def batalkan_reservasi(self, reservasi):
        if reservasi in self.daftar_reservasi:
            reservasi.status = 'dibatalkan'
            reservasi.kamar.status = 'tersedia'
            print("Reservasi dibatalkan.")

    def daftar_kamar_tersedia(self):
        print("Daftar Kamar Tersedia:")
        for kamar in self.daftar_kamar:
            if kamar.status == 'tersedia':
                kamar.tampilkan_info_kamar()


# Menu Aplikasi
hotel = Hotel()

while True:
    print("\nMenu Hotel")
    print("1. Tambah Kamar")
    print("2. Daftar Kamar Tersedia")
    print("3. Daftarkan Tamu")
    print("4. Buat Reservasi")
    print("5. Batalkan Reservasi")
    print("6. Tampilkan Info Tamu")
    print("0. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nomor = input("Nomor Kamar: ")
        tipe = input("Tipe Kamar (Single/Double/Suite): ")
        kamar = Kamar(nomor, tipe)  
        hotel.tambah_kamar(kamar)
    
    elif pilihan == "2":
        hotel.daftar_kamar_tersedia()

    elif pilihan == "3":
        nama = input("Nama Tamu: ")
        nomor_identitas = input("Nomor Identitas: ")
        kontak = input("Kontak: ")
        tamu = Tamu(nama, nomor_identitas, kontak)
        hotel.tambah_tamu(tamu)
    
    elif pilihan == "4":
        nama_tamu = input("Nama Tamu: ")
        nomor_kamar = input("Nomor Kamar: ")
        check_in = input("Tanggal Check-In: ")
        check_out = input("Tanggal Check-Out: ")

        # Cari tamu dan kamar
        tamu = next((t for t in hotel.daftar_tamu if t.nama == nama_tamu), None)
        kamar = next((k for k in hotel.daftar_kamar if k.nomor_kamar == nomor_kamar), None)

        if tamu and kamar:
            hotel.buat_reservasi(tamu, kamar, check_in, check_out)
        else:
            print("Tamu atau kamar tidak ditemukan.")
    
    elif pilihan == "5":
        nama_tamu = input("Nama Tamu: ")
        reservasi = next((r for r in hotel.daftar_reservasi if r.tamu.nama == nama_tamu and r.status == 'aktif'), None)
        if reservasi:
            hotel.batalkan_reservasi(reservasi)
        else:
            print("Reservasi tidak ditemukan.")
    
    elif pilihan == "6":
        nama_tamu = input("Nama Tamu: ")
        tamu = next((t for t in hotel.daftar_tamu if t.nama == nama_tamu), None)
        if tamu:
            tamu.tampilkan_info_tamu()
        else:
            print("Tamu tidak ditemukan.")

    elif pilihan == "0":
        print("Terima kasih telah menggunakan layanan hotel Fauzan Jaya, Sampai jumpa Kembali")
        break
            
    else:
        print("Pilihan tidak valid.")
