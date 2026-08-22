# ========================================
# MANIPULASI STRING DI PYTHON
# ========================================

# Kebanyakan method string di Python punya kembaran di Dart:
# upper() ≈ toUpperCase(), strip() ≈ trim(), replace() ≈ replaceAll(), dll.
# Satu string contoh dipakai di beberapa bagian di bawah.

kalimat = "Belajar Python itu menyenangkan"
print("String awal:", kalimat)

# ========================================
# 1. MENGAKSES KARAKTER (INDEXING)
# ========================================
# Sama seperti Dart: index mulai dari 0.
# Kelebihan Python: ada index negatif (menghitung dari belakang).

print(kalimat[0])    # karakter pertama  -> 'B'
print(kalimat[4])    # karakter kelima   -> 'j'
print(kalimat[-1])   # karakter terakhir -> 'n'
print(kalimat[-3])   # ke-3 dari belakang-> 'k'

# ========================================
# 2. SLICING (MENGAMBIL POTONGAN)
# ========================================
# Dart pakai substring(0, 7). Python pakai [mulai:selesai].
# Index "selesai" TIDAK ikut diambil (eksklusif), sama seperti substring di Dart.
# Kalau mulai/selesai dikosongkan = dari awal / sampai akhir.

print(kalimat[0:7])    # 'Belajar'
print(kalimat[8:14])   # 'Python' (index 8 s.d. 13)
print(kalimat[:7])     # 'Belajar' (dari awal)
print(kalimat[8:])     # 'Python itu menyenangkan' (sampai akhir)
print(kalimat[-12:])   # 'menyenangkan' (12 karakter terakhir)
print(kalimat[:])      # seluruh string

# ========================================
# 3. UBAH HURUF BESAR/KECIL (CASE)
# ========================================
text = "belajar python"

print(text.upper())        # 'BELAJAR PYTHON'   (Dart: toUpperCase())
print(text.lower())        # 'belajar python'   (Dart: toLowerCase())
print(text.capitalize())   # 'Belajar python'   (huruf pertama saja)
print(text.title())        # 'Belajar Python'   (tiap awal kata)

# ========================================
# 4. MENCARI & MENGECEK ISI STRING
# ========================================
# Operator "in" ≈ contains() di Dart, hasilnya True/False
print("Python" in kalimat)             # True

# find() ≈ indexOf() di Dart: balikin index, -1 kalau tidak ada
print(kalimat.find("Python"))          # 8
print(kalimat.find("Java"))            # -1 (tidak ditemukan)

print(kalimat.count("a"))              # 4 (jumlah kemunculan)
print(kalimat.startswith("Belajar"))   # True  (Dart: startsWith())
print(kalimat.endswith("menyenangkan"))# True  (Dart: endsWith())

# ========================================
# 5. HAPUS SPASI & GANTI TEKS
# ========================================
text_kotor = "   belajar python   "

print(text_kotor.strip())     # 'belajar python'   (Dart: trim())
print(text_kotor.lstrip())    # 'belajar python   ' (kiri saja)
print(text_kotor.rstrip())    # '   belajar python' (kanan saja)

# replace() ≈ replaceAll() di Dart
print(kalimat.replace("Python", "Dart"))  # 'Belajar Dart itu menyenangkan'

# ========================================
# 6. SPLIT & JOIN
# ========================================
# split() memecah string menjadi list (mirip split() di Dart).
# join() menggabungkan list menjadi string (mirip join() di Dart).

data = "apel,jeruk,mangga"
buah = data.split(",")         # hasilnya list
print(buah)                    # ['apel', 'jeruk', 'mangga']
print(type(buah))              # <class 'list'>

print(" - ".join(buah))        # 'apel - jeruk - mangga'

# ========================================
# 7. VALIDASI ISI STRING (isXxx)
# ========================================
# Semua method ini mengembalikan True/False. Cukup ingat yang sering dipakai:

print("123456".isdigit())     # True  - semua angka?
print("Python".isdigit())     # False
print("Python".isalpha())     # True  - semua huruf?
print("Python3".isalnum())    # True  - huruf atau angka (tanpa spasi)?
print("   ".isspace())        # True  - semua spasi?
print("python".islower())     # True  - semua huruf kecil?
print("PYTHON".isupper())     # True  - semua huruf besar?

# ========================================
# 8. FORMAT ANGKA DI F-STRING
# ========================================
# F-string sudah dipelajari di file 7. Di sini bonus formatnya:
# :.1f ≈ toStringAsFixed(1) di Dart

tinggi = 165.5
print(f"Tinggi: {tinggi:.1f} cm")     # 165.5

# :>10 / :<10 ≈ padLeft(10) / padRight(10) di Dart
nama = "Alice"
print(f"[{nama:>10}]")     # [     Alice] rata kanan
print(f"[{nama:<10}]")     # [Alice     ] rata kiri
print(f"[{nama:^10}]")     # [  Alice   ] rata tengah
print(f"{42:05d}")         # 00042 (padding nol)

# Catatan: ada cara lama (% dan .format) tapi sudah jarang dipakai.
# F-string adalah cara modern dan paling enak dibaca - cukup kuasai ini.

# ========================================
# 9. MULTILINE & RAW STRING
# ========================================
# Triple quotes untuk teks banyak baris (Dart tidak punya, biasanya pakai \n)
pesan = """
Baris pertama
Baris kedua
"""
print(pesan)

# Raw string (r"..."): backslash tidak dianggap escape character.
# Praktis untuk path Windows atau regex.
path = r"C:\Users\Documents\file.txt"
print(path)

# ========================================
# LATIHAN: FORMAT NAMA & EMAIL
# ========================================
# Semua langkah berurutan dari atas ke bawah, tanpa function.

nama_kotor = "   alice   in   wonderland  "

# Langkah 1: buang spasi berlebih di awal/akhir/tengah
nama_bersih = " ".join(nama_kotor.split())
print("Bersih :", nama_bersih)          # alice in wonderland

# Langkah 2: kapitalisasi tiap awal kata
nama_rapi = nama_bersih.title()
print("Rapi   :", nama_rapi)            # Alice In Wonderland

# Langkah 3: buat email dari nama (spasi jadi titik, semua lowercase)
email = nama_bersih.replace(" ", ".") + "@example.com"
print("Email  :", email)                # alice.in.wonderland@example.com

# Langkah 4 (bonus): ambil inisial tiap kata lewat index bertingkat
# kata[0][0] = huruf pertama dari kata pertama
kata = nama_rapi.split()
inisial = kata[0][0] + kata[1][0] + kata[2][0]
print("Inisial:", inisial)              # AIW

# Catatan: cara otomatis mengambil inisial untuk jumlah kata berapa pun
# membutuhkan perulangan (for) - menyusul di materi perulangan.
