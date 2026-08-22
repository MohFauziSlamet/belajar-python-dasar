# ========================================
# INPUT DATA DI PYTHON
# ========================================

# input() dipakai untuk membaca ketikan user dari keyboard.
# Di Dart kita biasanya pakai: stdin.readLineSync() (dari package dart:io)
#
# PENTING: hasil input() SELALU string, walaupun user mengetik angka.
# Kalau butuh angka untuk dihitung, harus dikonversi dulu (lihat bagian 2).

# ========================================
# 1. INPUT DASAR
# ========================================
nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")

print("Halo,", nama)
print("umur :", umur)

# Walau user mengetik angka, tipenya tetap string
print("tipe umur:", type(umur))   # <class 'str'>

# Karena string, ini akan ERROR (komentar saja biar program jalan):
# print(umur + 1)   <- TypeError: can only concatenate str to str

# ========================================
# 2. INPUT ANGKA (KONVERSI DULU)
# ========================================
# Pola yang sering dipakai: bungkus input() dengan int() atau float().
# Di Dart padanannya: int.parse(stdin.readLineSync()!)
umur_angka = int(umur)

print("umur tahun depan:", umur_angka + 1)   # sekarang bisa dihitung
print("tipe umur_angka :", type(umur_angka)) # <class 'int'>

# ========================================
# 3. KONVERSI TIPE DATA
# ========================================
# Konversi = mengubah data dari satu tipe ke tipe lain.
# Function yang dipakai: int(), float(), str(), bool()

# String ke Integer  (Dart: int.parse("1995"))
tahun_lahir_str = "1995"
tahun_lahir = int(tahun_lahir_str)
print("str -> int  :", tahun_lahir, type(tahun_lahir))

# String ke Float  (Dart: double.parse("170.5"))
tinggi_str = "170.5"
tinggi = float(tinggi_str)
print("str -> float:", tinggi, type(tinggi))

# Integer ke String  (Dart: angka.toString())
jumlah_adik = 2
jumlah_adik_str = str(jumlah_adik)
print("int -> str  :", jumlah_adik_str, type(jumlah_adik_str))

# ========================================
# 4. KONVERSI KE/FROM BOOLEAN
# ========================================
# Kaidah "kosong = False, ada isinya = True"
print("bool(0)   :", bool(0))      # nol -> False
print("bool(3)   :", bool(3))      # selain nol -> True
print("bool(\"\") :", bool(""))     # string kosong -> False
print("bool(\"a\"):", bool("a"))    # ada isinya -> True

# Sebaliknya, bool ke angka: True = 1, False = 0
print("int(True) :", int(True))
print("int(False):", int(False))

# ========================================
# CATATAN
# ========================================
# - Konversi gagal kalau formatnya tidak cocok:
#   int("abc")  <- error ValueError (cara menangani error dibahas nanti)
# - input() menghentikan program sampai user menekan Enter.
