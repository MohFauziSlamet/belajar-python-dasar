# ========================================
# OPERATOR ASSIGNMENT (PENUGASAN) DI PYTHON
# ========================================

# Operator assignment = memberi nilai ke variabel.
# Compound assignment (+=, -=, dll) menggabungkan operasi + assignment dalam satu operator.
# Kabar baik: Dart juga punya semua compound assignment ini, jadi tinggal pakai.

# ========================================
# 1. ASSIGNMENT DASAR (=)
# ========================================
nama = "Budi"
umur = 25

print(nama)   # Budi
print(umur)   # 25

# Re-assignment: nilai bisa diganti kapan saja
umur = umur + 1
print(umur)   # 26

# ========================================
# 2. COMPOUND ASSIGNMENT (+=, -=, *=, /=)
# ========================================
# x += 5 artinya sama persis dengan x = x + 5, cuma lebih ringkas.

nilai = 10
print(nilai)   # 10

nilai += 5     # sama dengan: nilai = nilai + 5
print(nilai)   # 15

nilai -= 3     # sama dengan: nilai = nilai - 3
print(nilai)   # 12

nilai *= 2     # sama dengan: nilai = nilai * 2
print(nilai)   # 24

nilai /= 4     # sama dengan: nilai = nilai / 4
print(nilai)   # 6.0  <- jadi float! (pembagian selalu float, ingat file 8)

# ========================================
# 3. COMPOUND ASSIGNMENT LANJUTAN (//=, %=, **=)
# ========================================
angka = 17

angka //= 5    # sama dengan: angka = angka // 5
print(angka)   # 3  (17/5 = 3.4 -> desimal dibuang)

angka %= 2     # sama dengan: angka = angka % 2
print(angka)   # 1  (3 % 2, sisa pembagian)

pangkat = 3
pangkat **= 4  # sama dengan: pangkat = pangkat ** 4
print(pangkat) # 81 (3 x 3 x 3 x 3)

# ========================================
# 4. PENTING: TIDAK ADA ++ DAN -- DI PYTHON
# ========================================
# Di Dart kita terbiasa: counter++ atau counter--
# Di Python operator itu TIDAK ADA - kodenya langsung error (SyntaxError).
#
# counter++    <- error! tidak ada di Python
# counter--    <- error! tidak ada di Python
#
# Penggantinya: pakai += 1 dan -= 1

counter = 0
counter += 1    # cara Python menulis counter++
counter += 1
counter += 1
print(counter)  # 3

# ========================================
# 5. SWAP VARIABEL (FITUR KHAS PYTHON)
# ========================================
# Menukar isi dua variabel. Di Dart perlu variabel penampung sementara:
#   var temp = a;  a = b;  b = temp;
# Di Python cukup SATU BARIS:

a, b = 10, 20
print(a, b)     # 10 20

a, b = b, a     # tukar!
print(a, b)     # 20 10

# (Multiple assignment a, b = 10, 20 sudah dikenal dari file 3)

# ========================================
# 6. BONUS: += UNTUK STRING
# ========================================
# String juga bisa += , untuk menambah teks di belakangnya.

pesan = "Halo"
pesan += " Python"
pesan += "!"
print(pesan)    # Halo Python!

# ========================================
# 7. KASUS PRAKTIS: DISKON BERTAHAP
# ========================================
# Pola umum di aplikasi kasir: harga dasar lalu diskon bertahap.
harga = 100_000
print(f"Harga awal         : Rp {harga:,}")

harga *= 0.9    # diskon member 10% (kali 90%)
print(f"Setelah diskon 10% : Rp {harga:,.0f}")

harga *= 0.95   # diskon tambahan 5%
print(f"Setelah diskon 5%  : Rp {harga:,.0f}")

# Format :,.0f dipakai agar tampilan rupiah ratusan ribu tidak berantakan
# (hasil kali float seperti 85500.00000000001 -> dibulatkan tampilannya)

# ========================================
# RANGKUMAN
# ========================================
# x = 5    assignment dasar
# x += 5   x = x + 5   (penjumlahan)
# x -= 5   x = x - 5   (pengurangan)
# x *= 5   x = x * 5   (perkalian)
# x /= 5   x = x / 5   (pembagian -> hasil float)
# x //= 5  x = x // 5  (pembagian bulat)
# x %= 5   x = x % 5   (sisa pembagian)
# x **= 5  x = x ** 5  (pangkat)
# Catatan: tidak ada x++ / x-- di Python, gunakan x += 1 / x -= 1
