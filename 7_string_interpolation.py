# ========================================
# STRING INTERPOLATION DI PYTHON
# ========================================

# String interpolation = menyisipkan nilai variabel ke dalam string.
# Di Dart kita sudah ahli: "Nama saya $nama" atau "Total: ${a + b}"
# Di Python caranya disebut f-string: tambahkan huruf f sebelum string,
# lalu pakai kurung kurawal untuk variabelnya.

# ========================================
# 1. CONCATENATION (CARA LAMA - HINDARI)
# ========================================
# Menggabungkan string dengan operator + (Dart juga bisa).
# Kelemahan: panjang, susah dibaca, dan angka WAJIB dikonversi dengan str()
# atau langsung TypeError.

nama = "Budi"
umur = 25
pekerjaan = "Programmer"

print("Nama saya " + nama + ", umur " + str(umur) + " tahun")
# Bayangkan kalau variabelnya 10 - mimpi buruk.

# ========================================
# 2. F-STRING (CARA MODERN - PAKAI INI)
# ========================================
# Persis seperti '$var' di Dart, cukup tambah f di depan string.
# Tidak perlu str() - angka otomatis dikonversi.

print(f"Nama saya {nama}, umur {umur} tahun")

# Dart : "Tahun depan umur saya ${umur + 1}"
# Python: kurung kurawal bisa langsung berisi ekspresi (hitungan):
print(f"Tahun depan umur saya {umur + 1} tahun")

# Bisa juga memanggil method di dalam kurung kurawal:
kota = "jakarta"
print(f"Saya tinggal di {kota.upper()}")   # Saya tinggal di JAKARTA

# ========================================
# 3. FORMAT ANGKA DI F-STRING
# ========================================
# Tambahkan titik dua : setelah variabel untuk memformat angka.
# (Alignment rata kiri/kanan sudah dibahas di file 5 bagian 8)

gaji = 8500000

# :, = pemisah ribuan (yang sering dipakai untuk uang)
print(f"Gaji: Rp {gaji:,}")           # Gaji: Rp 8,500,000

# :.2f = dua angka di belakang koma (Dart: toStringAsFixed(2))
berat = 62.5678
print(f"Berat: {berat:.2f} kg")       # Berat: 62.57 kg

# :.0f = bulat tanpa desimal
print(f"Berat bulat: {berat:.0f} kg") # Berat bulat: 63 kg

# :.1% = persen otomatis (dikalikan 100 + tanda %)
diskon = 0.25
print(f"Diskon: {diskon:.0%}")        # Diskon: 25%

# Format bisa digabung, misal rata kanan + pemisah ribuan:
print(f"Harga: Rp {gaji:>12,}")

# ========================================
# 4. MENAMPILKAN KURUNG KURAWAL DI F-STRING
# ========================================
# Karena {} dipakai untuk variabel, untuk menampilkan kurung kurawal
# asli ditulis dua kali: {{ dan }}

print(f"Formatnya seperti ini: {{nama}}")   # Output: Formatnya seperti ini: {nama}

# ========================================
# 5. F-STRING DENGAN DICT
# ========================================
# Dict sudah dikenal sedikit dari file 3. Trik: petik dalam harus
# BEDA dengan petik luar (luar double, dalam single).

user = {"nama": "Andi", "email": "andi@email.com"}
print(f"User: {user['nama']} ({user['email']})")

# Alternatif lebih rapi: simpan dulu ke variabel, lalu interpolasi
nama_user = user["nama"]
print(f"Nama user: {nama_user}")

# ========================================
# 6. CARA LAIN: .format() (CADANGAN SAJA)
# ========================================
# Sebelum f-string ada (Python lama), orang pakai .format().
# Tidak perlu dihafal - cukup kenali kalau melihat kode lama:

print("Nama saya {}, umur {} tahun".format(nama, umur))

# ========================================
# LATIHAN
# ========================================
# Buat kalimat lengkap dari data di bawah dengan SATU f-string saja:
produk = "Laptop"
harga = 15000000
stok = 5

# Contoh hasil yang diharapkan:
# Produk: Laptop | Harga: Rp 15,000,000 | Stok: 5 unit

hasil = f"Produk: {produk} | Harga: Rp {harga:,} | Stok: {stok} unit"
print(hasil)

# ========================================
# CATATAN
# ========================================
# - Selalu pakai f-string untuk interpolasi (cara modern, paling enak dibaca)
# - Concatenation (+) hanya untuk menggabungkan 2 string singkat
# - f-string juga bisa memanggil function: f"{nama_function()}" - menyusul
#   di materi function
# - f-string bisa berisi if-else singkat (ternary) - menyusul di materi percabangan
