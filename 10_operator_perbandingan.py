# ========================================
# OPERATOR PERBANDINGAN (COMPARISON) DI PYTHON
# ========================================

# Operator perbandingan membandingkan dua nilai.
# Hasilnya SELALU boolean: True atau False.
# Berita baik: keenam operator ini SAMA PERSIS dengan Dart,
# dan akan banyak dipakai di materi if/else berikutnya.

# ========================================
# 1. SAMA DENGAN (==) DAN TIDAK SAMA DENGAN (!=)
# ========================================
umur = 25
nama = "Budi"

print(umur == 25)    # True  (sama dengan)
print(umur == 20)    # False
print(umur != 20)    # True  (tidak sama dengan)
print(umur != 25)    # False

# String juga bisa dibandingkan, tapi CASE SENSITIVE (sama seperti Dart)
print(nama == "Budi")   # True
print(nama == "budi")   # False (huruf b kecil tidak sama dengan B besar)
print(nama != "Andi")   # True

# ========================================
# 2. LEBIH BESAR (>) DAN LEBIH KECIL (<)
# ========================================
print(umur > 20)     # True
print(umur > 25)     # False (25 tidak lebih besar dari 25)
print(umur < 30)     # True
print(umur < 25)     # False

# ========================================
# 3. LEBIH BESAR / KECIL SAMA DENGAN (>=, <=)
# ========================================
print(umur >= 25)    # True  (25 >= 25 lolos karena "sama dengan")
print(umur >= 30)    # False
print(umur <= 25)    # True
print(umur <= 20)    # False

# ========================================
# 4. PERBANDINGAN STRING (URUTAN ABJAD)
# ========================================
# Python bisa membandingkan huruf awal string lewat urutan abjad
# (dart juga bisa begini, perilakunya sama)

print("apple" < "banana")    # True  (a duluan dari b)
print("python" > "java")     # True  (p setelah j)

# Trik case-insensitive: samakan dulu hurufnya (ingat .lower() dari file 5)
print("Budi".lower() == "budi".lower())   # True

# ========================================
# 5. CHAINED COMPARISON (FITUR KHAS PYTHON)
# ========================================
# Python bisa merangkai perbandingan seperti matematika:
#   18 <= suhu <= 26
# Di Dart harus dua kondisi digabung &&:
#   suhu >= 18 && suhu <= 26
# Python membuatnya jauh lebih ringkas - dan hasilnya sama: True/False.

suhu = 28.5
print(18 <= suhu <= 26)   # False (28.5 di luar rentang 18-26)
print(0 <= suhu <= 100)   # True

nilai = 75
print(70 <= nilai <= 80)  # True

# ========================================
# 6. KASUS PRAKTIS: NILAI SISWA
# ========================================
nilai_mtk = 85

print(f"Nilai          : {nilai_mtk}")
print(f"Lulus?         : {nilai_mtk >= 70}")     # True
print(f"Dapat grade A? : {nilai_mtk >= 90}")     # False
print(f"Perlu remedial?: {nilai_mtk < 70}")      # False

# ========================================
# 7. JEBAKAN FLOAT: 0.1 + 0.2 != 0.3
# ========================================
# Masalah yang sama di Dart (double): floating point tidak presisi.
# Jangan bandingkan float dengan == secara langsung.

hasil = 0.1 + 0.2
print(hasil)                  # 0.30000000000000004 (bukan 0.3!)
print(hasil == 0.3)           # False <- mengejutkan tapi nyata

# Cara aman: cek selisihnya sangat kecil (toleransi)
print(abs(hasil - 0.3) < 0.0001)   # True

# ========================================
# 8. MEMBANDINGKAN TIPE YANG BERBEDA
# ========================================
# Angka 42 dan string "42" TIDAK sama (tipenya beda, sama seperti Dart).
print(42 == "42")         # False
print(str(42) == "42")    # True  (konversi dulu, baru bandingkan)

# ========================================
# CATATAN PENTING
# ========================================
# 1. Jangan tertukar = dengan == :
#      =   assignment (mengisi nilai)   -> umur = 25
#      ==  comparison (membandingkan)   -> umur == 25
#    (Dart juga sama, hati-hati yang sama)
# 2. Menggabung beberapa kondisi (and / or / not) dibahas di file 11
# 3. Untuk cek "variabel kosong/None" nanti dipakai: x is None
#    (operator is menyusul bersama materi object)

# ========================================
# RANGKUMAN
# ========================================
# ==   sama dengan                (sama seperti Dart)
# !=   tidak sama dengan          (sama seperti Dart)
# >    lebih besar dari           (sama seperti Dart)
# <    lebih kecil dari           (sama seperti Dart)
# >=   lebih besar sama dengan    (sama seperti Dart)
# <=   lebih kecil sama dengan    (sama seperti Dart)
# 18 <= x <= 26  chained comparison (Dart: x >= 18 && x <= 26)
# Hasil semua operator: True atau False
