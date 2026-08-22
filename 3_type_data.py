# ========================================
# TIPE DATA DI PYTHON
# ========================================

# Python punya 8 tipe data dasar:
# 1. String (str)   -> teks
# 2. Integer (int)  -> bilangan bulat
# 3. Float (float)  -> bilangan pecahan/desimal
# 4. Boolean (bool) -> True / False
# 5. List           -> koleksi yang bisa diubah (mirip List di Dart)
# 6. Tuple          -> koleksi yang TIDAK bisa diubah
# 7. Set            -> koleksi item unik tanpa urutan
# 8. Dictionary     -> pasangan kunci-nilai (mirip Map di Dart)
#
# Bedanya dengan Dart: variabel Python tidak perlu deklarasi tipe.
# Tipenya otomatis mengikuti nilainya (seperti `var` di Dart).

# ========================================
# 1. STRING (str)
# ========================================
# Teks, ditulis dengan tanda petik tunggal atau ganda.
# Di Dart kita tulis: String nama = "Azka";
nama = "Azkafitra"
print("Nilai  :", nama)
print("Tipe   :", type(nama))

# ========================================
# 2. INTEGER (int)
# ========================================
# Bilangan bulat tanpa koma.
# Angka besar boleh pakai underscore biar mudah dibaca: 2_000_000
usia = 2
saldo = 2_000_000
print("Nilai  :", usia, "dan", saldo)
print("Tipe   :", type(usia))

# ========================================
# 3. FLOAT (float)
# ========================================
# Bilangan pecahan (pakai titik, bukan koma).
# Kalau di Dart: double berat = 11.5;
berat_badan = 11.5
suhu = 27.5
print("Nilai  :", berat_badan, "dan", suhu)
print("Tipe   :", type(berat_badan))

# ========================================
# 4. BOOLEAN (bool)
# ========================================
# Hanya dua nilai: True atau False (huruf pertama kapital!).
# Di Dart juga bool, tapi nilainya true/false huruf kecil semua.
sedang_belajar = True
sedang_tidur = False
print("Nilai  :", sedang_belajar, "dan", sedang_tidur)
print("Tipe   :", type(sedang_belajar))

# ========================================
# 5. LIST
# ========================================
# Koleksi berurutan dan BISA diubah (tambah, hapus, edit).
# Mirip List<T> di Dart.
daftar_buah = ["apel", "pisang", "jeruk"]
print("Nilai  :", daftar_buah)
print("Tipe   :", type(daftar_buah))

# Akses pakai index, mulai dari 0 (sama seperti Dart)
print("Buah pertama :", daftar_buah[0])

# Bisa ditambah item baru (mutable)
daftar_buah.append("mangga")
print("Setelah append:", daftar_buah)

# ========================================
# 6. TUPLE
# ========================================
# Seperti list, tapi TIDAK BISA diubah setelah dibuat (immutable).
# Anggap seperti list yang "dikunci" - aman dari perubahan tak sengaja.
koordinat = (-6.2, 106.8)
periode = (2023, "Q4")
print("Nilai  :", koordinat, "dan", periode)
print("Tipe   :", type(koordinat))

# Akses index juga bisa, tapi tidak bisa diubah:
# koordinat[0] = 7.0  <- baris ini akan error kalau dijalankan
print("Latitude:", koordinat[0])

# ========================================
# 7. SET
# ========================================
# Koleksi item UNIK, tidak berurutan, dan tidak punya index.
# Kalau ada data kembar, otomatis disimpan satu saja.
keahlian = {"python", "sql", "git"}
print("Nilai  :", keahlian)
print("Tipe   :", type(keahlian))

# Item duplikat otomatis dibuang
angka_favorit = {1, 2, 2, 3, 3, 3}
print("Unik saja:", angka_favorit)

# ========================================
# 8. DICTIONARY (dict)
# ========================================
# Pasangan kunci-nilai (key: value).
# Mirip Map<String, dynamic> di Dart.
profil = {
    "nama": "Azkafitra",
    "umur": 2,
    "kota": "Jakarta",
}
print("Nilai  :", profil)
print("Tipe   :", type(profil))

# Ambil nilai berdasarkan kunci (seperti profil['nama'] di Dart map)
print("Nama   :", profil["nama"])

# Ubah nilai berdasarkan kunci
profil["umur"] = 3
print("Umur baru:", profil["umur"])

# ========================================
# BONUS: MENGETAHUI TIPE DATA
# ========================================
# function type() untuk mengecek tipe data sebuah nilai/variabel
print(type("halo"))        # <class 'str'>
print(type(42))            # <class 'int'>
print(type(3.14))          # <class 'float'>
print(type(True))          # <class 'bool'>

# ========================================
# BONUS: MULTIPLE ASSIGNMENT
# ========================================
# Python bisa membuat beberapa variabel sekaligus dalam satu baris.
# Di Dart biasanya: var a = 1; var b = 2;
judul, penulis, tahun = "Belajar Python", "Guido van Rossum", 2024
print(judul, "-", penulis, "-", tahun)

# ========================================
# CATATAN: ATURAN PENAMAAN VARIABEL
# ========================================
# 1. Pakai snake_case untuk variabel dan function -> total_nilai_siswa
#    (Python tidak pakai camelCase seperti Dart)
# 2. Nama harus deskriptif -> "umur" lebih baik dari "u"
# 3. Tidak boleh diawali angka, tidak boleh ada spasi -> 1nama, nama siswa (salah)
# 4. Konstanta pakai UPPER_CASE -> MAX_RETRY
#    (Python tidak punya keyword const seperti Dart, hanya konvensi)
