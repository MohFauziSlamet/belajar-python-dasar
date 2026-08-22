# ========================================
# ESCAPE CHARACTER DI PYTHON
# ========================================

# Escape character = backslash (\) + karakter tertentu, untuk menulis
# "karakter khusus" di dalam string (enter, tab, tanda petik, dll).
#
# Kabar baik: Dart memakai aturan yang SAMA (\n, \t, \\, \"),
# jadi ini materi yang paling mudah berpindah dari Dart ke Python.

# ========================================
# 1. \n - NEW LINE (PALING SERING DIPAKAI)
# ========================================
# Pindah baris baru, seperti menekan Enter.
print("Baris pertama\nBaris kedua")
# Output:
# Baris pertama
# Baris kedua

# ========================================
# 2. \t - TAB
# ========================================
# Cocok untuk teks berkolom.
print("Nama\tUmur\tKota")
print("Budi\t25\tJakarta")
# Output:
# Nama   Umur   Kota
# Budi   25     Jakarta

# ========================================
# 3. \\ - BACKSLASH
# ========================================
# Backslash ditulis dua kali, karena satu backslash
# akan dianggap awal escape character.
print("C:\\Users\\Documents\\file.txt")
# Output: C:\Users\Documents\file.txt

# ========================================
# 4. \" dan \' - TANDA PETIK DI DALAM STRING
# ========================================
# Cara pertama: escape petiknya.
print("Dia bilang: \"Saya suka programming\"")
print("It\'s a beautiful day")

# Cara kedua (lebih ringkas): selang-seling jenis petiknya.
print('Dia berkata: "Halo, apa kabar?"')   # petik tunggal luar, ganda dalam
print("It's a beautiful day")              # petik ganda luar, tunggal dalam

# ========================================
# 5. \r - CARRIAGE RETURN (JARANG)
# ========================================
# Kursor kembali ke AWAL baris, lalu teks berikutnya menimpa teks lama.
print("Loading...\rSelesai!")
# Yang terlihat di terminal: Selesai!
# ("Loading..." tertimpa karena \r kembali ke awal baris)

# ========================================
# 6. \b - BACKSPACE (JARANG)
# ========================================
# Menghapus satu karakter sebelumnya.
print("Hello\bWorld")
# Output: HellWorld  (huruf "o" kehapus)

# ========================================
# 7. \f dan \v - SANGAT JARANG
# ========================================
# Form feed & vertical tab, warisan printer/gaya cetak lama.
# Cukup tahu bahwa ini ada, tidak perlu dihafal.
print("Halaman 1\fHalaman 2")
print("Baris1\vBaris2")

# ========================================
# 8. UNICODE: \u, \U, dan \N{name}
# ========================================
# Menulis karakter unicode lewat kode hex-nya.
# Beda sedikit dengan Dart:
#   Dart  : '\u{1F600}'  ->  Python: '\U0001F600' (harus tepat 8 digit)
print("Omega: \u03A9")            # \u     = 4 digit hex
print("Emoji: \U0001F600")        # \U     = 8 digit hex
print("Euro : \N{EURO SIGN}")     # \N{..} = pakai NAMA unicode (khas Python)

# ========================================
# 9. KODE OCTAL & HEX (JARANG)
# ========================================
print("\101")   # \ooo = octal, 101 = huruf 'A'
print("\x41")   # \xhh = hex,   41  = huruf 'A'

# ========================================
# CATATAN
# ========================================
# - Wajib dikuasai : \n  \t  \\  \"  \'
# - Cukup tahu ada : \r  \b  \f  \v  \ooo  \xhh  \u  \U  \N{}
# - Untuk path Windows, alternatif tanpa \\.: raw string r"C:\Users\..."
#   (sudah dibahas di file 5_manipulasi_string.py bagian 9)
