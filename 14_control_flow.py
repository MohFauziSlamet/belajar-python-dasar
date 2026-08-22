# ========================================
# KONTROL ALUR PROGRAM (CONTROL FLOW)
# ========================================

# Kontrol alur program (control flow) adalah cara mengatur eksekusi kode
# berdasarkan kondisi tertentu.
# (Sumber: materi-pdf "Python Dasar.pdf" halaman 70 - 85)
#
# Jika di Dart seperti ini → di Python jadi seperti ini:
#   - Dart if / else if / else   →  Python if / elif / else
#   - Dart switch-case           →  Python match-case
#   - Dart cond ? x : y          →  Python x if cond else y
#
# Jebakan untuk dev Dart:
#   1. Tidak menggunakan kurung kurawal {}, melainkan Indentasi (4 spasi) & titik dua (:)
#   2. "else if" di Python ditulis "elif" (singkat)
#   3. Ternary operator urutannya dibalik: [Nilai True] if [Kondisi] else [Nilai False]

# ========================================
# 1. PERNYATAAN IF (IF STATEMENT)
# ========================================
# Menjalankan blok kode HANYA jika kondisi bernilai True.

age = 20
if age >= 17:
    print("Sudah punya KTP")  # Sudah punya KTP

# ========================================
# 2. PERNYATAAN IF-ELSE
# ========================================
# Menjalankan kode A jika True, atau kode B jika False.

score = 55
if score >= 60:
    print("Anda lulus")
else:
    print("Anda tidak lulus")  # Anda tidak lulus

# ========================================
# 3. PERNYATAAN ELIF (ELSE IF)
# ========================================
# Mengecek beberapa kondisi secara berurutan. (Di Dart: else if)

grade_score = 85

if grade_score >= 90:
    print("Grade A")
elif grade_score >= 80:
    print("Grade B")  # Grade B
elif grade_score >= 70:
    print("Grade C")
else:
    print("Grade D")

# ========================================
# 4. KONDISI DENGAN OPERATOR LOGIKA
# ========================================
# Menggabungkan beberapa syarat dalam satu if menggunakan and / or / not.

user_age = 20
has_license = True

if user_age >= 17 and has_license:
    print("Boleh mengendarai kendaraan")  # Boleh mengendarai kendaraan

# ========================================
# 5. NESTED IF (IF BERSARANG)
# ========================================
# Menempatkan pernyataan if di dalam if lainnya.

username = "admin"
password = "123"

if username == "admin":
    if password == "123456":
        print("Login berhasil")
    else:
        print("Password salah")  # Password salah
else:
    print("Username tidak ditemukan")

# ========================================
# 6. MATCH-CASE (SWITCH-CASE DI DART)
# ========================================
# Alternatif lebih bersih untuk pengujian banyak nilai (Python 3.10+).
# Khas Python: gunakan '|' untuk multiple value, dan '_' untuk default (else/default).

day = "sabtu"

match day:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari kerja")
    case "sabtu" | "minggu":
        print("Hari libur")  # Hari libur
    case _:
        print("Nama hari tidak valid")

# ========================================
# 7. CONDITIONAL EXPRESSION (TERNARY OPERATOR)
# ========================================
# Menulis kondisi sederhana dalam 1 baris.
# Perbedaan sintaks:
#   Dart  : kondisi ? nilai_true : nilai_false
#   Python: nilai_true if kondisi else nilai_false

status_code = 200
result = "OK" if status_code == 200 else "Error"
print(result)  # OK

number = -5
label = "Positif" if number > 0 else "Non-positif"
print(label)  # Non-positif

# ========================================
# LATIHAN
# ========================================
# Kerjakan tanpa melihat contoh di atas. Buat file kecil atau tulis di sini:
#
# 1. Program cek harga tiket:
#    - umur < 3      : "Gratis"
#    - umur 3 - 12   : "Tiket anak Rp 25.000"
#    - umur 13 - 64  : "Tiket dewasa Rp 50.000"
#    - umur >= 65    : "Tiket senior Rp 30.000"
#    (petunjuk: elif berurutan, gunakan chained comparison dari file 10)
#
# 2. Cek kelayakan promo: dapat diskon jika total >= 100000 ATAU punya kartu member,
#    TAPI tidak berlaku untuk hari pembukaan (is_opening_day = True).
#    (petunjuk: and / or / not dari file 11)
#
# 3. Tulis versi ternary dari: "Genap" jika angka % 2 == 0, "Ganjil" jika tidak.

# ========================================
# RANGKUMAN
# ========================================
# 1. Struktur dasar: if <kondisi>: diakhiri titik dua (:), isi blok pakai indentasi 4 spasi.
# 2. Banyak kondisi berurutan: gunakan elif (bukan else if).
# 3. Multiple match: match-case pakai `case v1 | v2:` dan wildcard `case _:` untuk default.
# 4. Ternary: `nilai_true if kondisi else nilai_false` (kebalikan urutan Dart `cond ? a : b`).
