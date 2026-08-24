# ========================================
# OPERATOR STRING DI PYTHON
# ========================================

# Operator string = operator yang bekerja pada string.
# Ada 4: + (gabung), * (ulang), in (cari ada), not in (cari tidak ada).
#
# Jika di Dart seperti ini → di Python jadi seperti ini:
#   +       : sama seperti Dart, menggabungkan string
#   *       : TIDAK ADA di Dart! (di Dart harus List.filled(3, "x").join())
#   in      : Dart pakai method .contains()
#   not in  : Dart: !teks.contains(...)

# ========================================
# 1. OPERATOR + : MENGGABUNGKAN (CONCATENATION)
# ========================================
# Sama seperti Dart: string + string = string gabungan.

nama_depan = "John"
nama_belakang = "Doe"

print(nama_depan + " " + nama_belakang)   # John Doe

# JEBAKAN: string + angka = error (TypeError), harus konversi dulu.
# (sudah dibahas juga di file 7 bagian 1)
umur = 25
# print("Umur: " + umur)        <- error!
print("Umur: " + str(umur))     # Umur: 25  <- benar, konversi dulu

# Itulah kenapa untuk menyisipkan variabel, f-string lebih enak:
print(f"Umur: {umur}")          # Umur: 25

# ========================================
# 2. OPERATOR * : MENGULANG STRING
# ========================================
# Fitur khas Python yang tidak ada di Dart: string * angka = string diulang.
# Di Dart untuk hasil sama harus: List.filled(3, "na").join() -> "nanana"

print("=" * 30)        # ==============================
print("na " * 3)       # na na na
print("abc" * 2)       # abcabc

# Kombinasi + dan * (dikali dulu, baru digabung - ingat presedensi file 8)
print("-" * 5 + ">" + "-" * 5)   # ----->-----

# ========================================
# 3. OPERATOR in : CEK ADA / TIDAK ADA
# ========================================
# "kata" in teks -> True kalau kata itu ada di dalam teks.
# Dart memakai method: teks.contains("kata")
# (operator in ini juga sudah diperkenalkan di file 5 bagian 4)

kalimat = "Belajar Python itu menyenangkan"

print("Python" in kalimat)      # True
print("Java" in kalimat)        # False

# not in = kebalikannya
print("Java" not in kalimat)    # True  (Java tidak ada -> benar)
print("Python" not in kalimat)  # False

# Hasilnya boolean - pas dikombinasi dengan operator logika (file 11):
ada_python = "Python" in kalimat
ada_java = "Java" in kalimat
print(ada_python and not ada_java)   # True (ada Python, tidak ada Java)

# ========================================
# 4. KASUS PRAKTIS: PEMISAH GARIS & CEK EMAIL
# ========================================
# Pola "*" * n sering dipakai untuk garis pemisah output di terminal.

judul = "STRUK BELANJA"
print("=" * 20)
print(judul)
print("=" * 20)

# Pola "in" untuk validasi sederhana:
email = "azka@example.com"
berisi_at = "@" in email
print(f"Email valid (ada @)? {berisi_at}")   # True

# ========================================
# RANGKUMAN
# ========================================
# +       menggabungkan string           (Dart: sama, + juga)
# *       mengulang string n kali        (Dart: tidak ada -> List.filled().join())
# in      cek ada di dalam string        (Dart: .contains())
# not in  cek tidak ada di dalam string  (Dart: !.contains())
# Catatan: "angka" + 5 -> TypeError, konversi dengan str() atau pakai f-string
