# ========================================
# PRIORITAS OPERATOR DI PYTHON
# ========================================

# Prioritas operator (precedence) = urutan eksekusi operator saat mereka
# ada dalam SATU ekspresi yang sama. Prioritas tinggi dieksekusi duluan.
# (Sumber: materi-pdf "Python Dasar.pdf" halaman 69)
#
# Kabar baik: struktur prioritas Dart mirip:
#   Dart  : !  >  * / %  >  + -  >  == != < >  >  &&  >  ||
#   Python: ** >  * / // % > + - > perbandingan > not > and > or
# Tapi ada satu jebakan penting untuk orang Dart - lihat bagian 4.

# ========================================
# 1. TABEL PRIORITAS LENGKAP (TINGGI KE RENDAH)
# ========================================
# 1. **              pangkat
# 2. *  /  //  %     perkalian & pembagian (dari kiri ke kanan)
# 3. +  -            penjumlahan & pengurangan
# 4. ==  !=  <  >  <=  >=   perbandingan
# 5. not             logika not
# 6. and             logika and
# 7. or              logika or
#
# Intinya mudah diingat: HITUNG dulu -> BANDINGKAN -> LOGIKA terakhir.
# (Kurung () selalu paling didahulukan, di atas segalanya)

# ========================================
# 2. DALAM ARITMATIKA (REVIEW FILE 8)
# ========================================
print(2 + 3 * 4)          # 14  (3*4 dulu, baru +2)
print(10 + 8 // 3 * 2 - 1) # 13  (8//3=2, 2*2=4, 10+4-1=13; // dan * satu level, kiri ke kanan)

# ========================================
# 3. ARITMATIKA LEBIH TINGGI DARI PERBANDINGAN
# ========================================
# Di ekspresi campuran: hitung angkanya dulu, baru dibandingkan.

print(5 + 3 > 7)          # True   (5+3=8 dulu, baru 8 > 7)
print(2 * 3 == 6)         # True   (2*3=6 dulu, baru 6 == 6)

# ========================================
# 4. JEBAKAN UNTUK ORANG DART: not vs PERBANDINGAN
# ========================================
# Di Python, perbandingan LEBIH TINGGI dari not.
# Artinya:  not 5 > 3  dibaca  not (5 > 3)  ->  not True  ->  False
print(not 5 > 3)          # False

# Di Dart kebalikannya: ! punya prioritas PALING TINGGI (unary),
# jadi !(5 > 3) harus pakai kurung, dan !5 sendiri error.
# Kesimpulan: di Python not cenderung "membalik hasil perbandingan" -
# perilaku yang justru kita inginkan. Tapi tetap tulis kurung kalau ragu.

# ========================================
# 5. not -> and -> or (REVIEW FILE 11)
# ========================================
print(not True and False)      # False  (not True=False dulu, lalu False and False)
print(True or False and False) # True   (and dulu: False and False=False, lalu True or False)

# ========================================
# 6. SATU EKSPRESI PENUH: SEMUA LEVEL
# ========================================
# Baca urutannya: ** dan % dulu, lalu == dan >, terakhir and.

print(1 + 2 == 3 and 4 * 2 > 7)     # True  (3==3 True, 8>7 True, True and True)
print(10 % 3 == 1 or 2 ** 3 > 10)   # True  (10%3=1 True, 2**3=8 >10 False, True or False)

# ========================================
# 7. KURUNG () : OVERRIDE + KEJELASAN
# ========================================
# Kurung selalu menang atas prioritas apa pun.
# Lebih penting lagi: kurung membuat MAKSUD kode jelas.

# Kasus praktis - aturan diskon toko:
#   "Dapat diskon kalau total >= 500rb, ATAU total >= 200rb DAN member."
total = 600000
member = False

# Tanpa kurung (mengandalkan prioritas: and dieksekusi sebelum or):
dapat_diskon = total >= 500000 or total >= 200000 and member
print(dapat_diskon)        # True (600rb >= 500rb, aturan bekerja benar)

# Kurung di posisi salah -> logika berubah total:
salah = (total >= 500000 or total >= 200000) and member
print(salah)               # False (member False ikut menahan semua)

# Kurung di posisi benar -> sama dengan tanpa kurung, tapi maksudnya jelas:
benar = total >= 500000 or (total >= 200000 and member)
print(benar)               # True

# ========================================
# RANGKUMAN
# ========================================
# Urutan lengkap (tinggi -> rendah):
#   ()  >  **  >  * / // %  >  + -  >  perbandingan  >  not  >  and  >  or
# Cara gampang ingat: HITUNG -> BANDINGKAN -> LOGIKA
# Perbedaan dengan Dart: not lebih RENDAH dari perbandingan
#   (Dart: ! tertinggi), jadi not 5 > 3 == not (5 > 3)
# Best practice: pakai kurung untuk kondisi campuran or/and -
# bukan karena wajib, tapi agar maksud kode terbaca sekali lihat
