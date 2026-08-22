# ========================================
# OPERATOR ARITMATIKA DI PYTHON
# ========================================

# Operator aritmatika = simbol untuk operasi matematika.
# Berita baik untuk kita: hampir semua sama dengan Dart.
# Yang BEDA dan penting:
#   - Dart  ~/  (truncating division)  ->  Python //
#   - Dart  pow(a, b) dari dart:math   ->  Python a ** b (ada operator pangkat!)

# Variabel contoh yang dipakai di beberapa bagian
a = 10
b = 3

# ========================================
# 1. OPERATOR DASAR (SAMA SEPERTI DART)
# ========================================
print(a + b)   # 13   penjumlahan
print(a - b)   # 7    pengurangan
print(a * b)   # 30   perkalian
print(a / b)   # 3.3333333333333335  pembagian (SELALU hasil float, walau habis dibagi)

# Catatan penting soal / :
print(10 / 2)  # 5.0  <- tetap float! (di Dart int/int juga menghasilkan double)

# ========================================
# 2. PEMBAGIAN BULAT (//) DAN MODULO (%)
# ========================================
# // = pembagian yang dibuang desimalnya (Dart: operator ~/)
print(a // b)      # 3   (10/3 = 3.333 -> ambil 3 saja)
print(15 // 4)     # 3   (15/4 = 3.75 -> dibuang, BUKAN dibulatkan ke atas)

# % = modulo, sisa pembagian (Dart juga pakai %)
print(a % b)       # 1   (10 = 3*3 + 1 -> sisanya 1)
print(15 % 4)      # 3   (15 = 4*3 + 3 -> sisanya 3)
print(20 % 5)      # 0   (habis dibagi -> sisa 0)

# Kegunaan sehari-hari % : cek genap/ganjil & kelipatan
print(7 % 2)       # 1 -> ganjil (sisa 1)
print(8 % 2)       # 0 -> genap  (habis dibagi 2)

# ========================================
# 3. PANGKAT (**)
# ========================================
# Dart tidak punya operator pangkat (harus pow(2, 3) dari dart:math).
# Python punya: ** langsung.
print(2 ** 3)      # 8    (2 x 2 x 2)
print(3 ** 2)      # 9    (3 x 3)
print(10 ** 2)     # 100

# ========================================
# 4. PRIORITAS OPERASI (PRESEDENSI)
# ========================================
# Sama seperti matematika & Dart:
# 1. kurung ()        2. pangkat **
# 3. kali/bagi * / // %    4. tambah/kurang + -

print(2 + 3 * 4)         # 14 (kali dulu, baru tambah)
print((2 + 3) * 4)       # 20 (kurung selalu didahulukan)
print(10 + 8 // 3 * 2 - 1)  # 13 (// dan * dulu dari kiri: 8//3=2, 2*2=4, 10+4-1=13)

# ========================================
# 5. KASUS PRAKTIS: BELANJA
# ========================================
harga_apel = 5000      # per kg
harga_jeruk = 7000     # per kg
berat_apel = 2         # kg
berat_jeruk = 1.5      # kg

total = (harga_apel * berat_apel) + (harga_jeruk * berat_jeruk)
uang_bayar = 30000
kembalian = uang_bayar - total

# Perhatikan: hasilnya 20500.0 (float) karena berat_jeruk = 1.5 adalah float.
# Int dan float dijumlahkan -> hasil float (aturan yang sama dengan Dart).
print(f"Total belanja: Rp {total:,}")       # Rp 20,500.0
print(f"Kembalian    : Rp {kembalian:,}")   # Rp 9,500.0

# ========================================
# 6. KASUS PRAKTIS: DISKON & RATA-RATA
# ========================================
# Diskon 10% dari harga laptop
harga_laptop = 15000000
jumlah_diskon = harga_laptop * (10 / 100)
harga_final = harga_laptop - jumlah_diskon
print(f"Harga setelah diskon: Rp {harga_final:,}")   # Rp 13,500,000

# Rata-rata nilai (format :.2f agar rapi, seperti toStringAsFixed(2))
rata_rata = (85 + 90 + 78) / 3
print(f"Rata-rata: {rata_rata:.2f}")                 # 84.33

# ========================================
# RANGKUMAN
# ========================================
# +   penjumlahan            (sama seperti Dart)
# -   pengurangan            (sama seperti Dart)
# *   perkalian              (sama seperti Dart)
# /   pembagian -> float     (sama seperti Dart int/int)
# //  pembagian bulat        (Dart: ~/)
# %   modulo / sisa bagi     (sama seperti Dart)
# **  pangkat                (Dart: pow() dari dart:math)
