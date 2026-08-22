# ========================================
# VARIABEL DI PYTHON
# ========================================

# Variabel = "wadah" untuk menyimpan data.
# Bedanya dengan Dart: tidak perlu menulis tipe datanya,
# Python otomatis mengenali dari nilainya.
# Di Dart : var nama = "Azka";  atau  String nama = "Azka";
# Python  : nama = "Azka"

# ========================================
# 1. MEMBUAT VARIABEL (ASSIGNMENT)
# ========================================
# Pakai tanda = untuk mengisi nilai ke variabel.
# Catatan penting: di Python pakai snake_case (nama_depan),
# BUKAN camelCase (namaDepan) seperti kebiasaan kita di Dart/Flutter.

nama_depan = "Muhammad"
nama_belakang = "Azkafitra Ramadhan"
usia = 2
berat_badan = 11.0

print(nama_depan, nama_belakang)
print("usia :", usia)
print("berat badan :", berat_badan)

# ========================================
# 2. ISI VARIABEL BISA DIGANTI (REASSIGNMENT)
# ========================================
# Nilai variabel bisa diubah kapan saja.
# Di Dart, `var` mengunci tipe setelah pengisian pertama.
# Di Python bebas saja - bahkan tipe datanya boleh berbeda.

usia = 3   # setelah ulang tahun :)
print("usia sekarang :", usia)

status = "belum sekolah"   # awalnya string...
status = True              # ...berubah jadi bool, tidak error
print("status :", status)

# ========================================
# 3. MENGGUNAKAN VARIABEL DALAM OPERASI
# ========================================
# Variabel bisa dipakai untuk menghitung atau digabung dengan variabel lain.

tahun_lahir = 2023
tahun_sekarang = 2026
usia_hitung = tahun_sekarang - tahun_lahir

print("usia hasil hitung :", usia_hitung)

nama_lengkap = nama_depan + " " + nama_belakang
print("nama lengkap :", nama_lengkap)

# ========================================
# CATATAN PENAMAAN VARIABEL
# ========================================
# - snake_case untuk variabel -> nama_depan (bukan namaDepan)
# - Nama harus deskriptif -> "usia" lebih baik daripada "u"
# - Tidak boleh diawali angka / pakai spasi -> 2nama, nama siswa (salah)
# - Konstanta pakai UPPER_CASE -> MAX_RETRY
