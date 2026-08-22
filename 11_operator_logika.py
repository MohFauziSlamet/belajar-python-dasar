# ========================================
# OPERATOR LOGIKA DI PYTHON
# ========================================

# Operator logika menggabungkan kondisi boolean (True/False).
# Ganti kata kuncinya dari Dart:
#   Dart: &&    Python: and
#   Dart: ||    Python: or
#   Dart: !x    Python: not x
# Perilakunya sama persis - tinggal ganti simbol jadi kata.

# ========================================
# 1. AND (Dart: &&)
# ========================================
# Hasilnya True hanya kalau SEMUA kondisi True.
# Cukup satu False, hasilnya langsung False.

print(True and True)     # True
print(True and False)    # False
print(False and False)   # False

# Contoh praktis: boleh nyetir harus cukup umur DAN punya SIM
umur = 25
punya_sim = True

boleh_nyetir = (umur >= 17) and punya_sim
print(boleh_nyetir)      # True

# Kasus login (lanjutan dari file 10): username DAN password harus benar
username = "admin"
password = "12345"

login_valid = (username == "admin") and (password == "rahasia")
print(login_valid)       # False (password salah, cukup satu saja untuk gagal)

# ========================================
# 2. OR (Dart: ||)
# ========================================
# Hasilnya True kalau MINIMAL SATU kondisi True.
# Semua False baru hasilnya False.

print(True or False)     # True
print(False or False)    # False

# Contoh praktis: bisa bayar pakai tunai ATAU kartu
punya_tunai = False
punya_kartu = True

bisa_bayar = punya_tunai or punya_kartu
print(bisa_bayar)        # True (cukup satu saja)

# Contoh: hari libur (Sabtu atau Minggu)
hari = "Sabtu"
bisa_santai = (hari == "Sabtu") or (hari == "Minggu")
print(bisa_santai)       # True

# ========================================
# 3. NOT (Dart: !)
# ========================================
# Membalik nilai boolean: True jadi False, False jadi True.
# Di Dart simbolnya !x, di Python ditulis not x (lebih mirip bahasa manusia).

hujan = False
print(not hujan)         # True  (tidak hujan)

sudah_login = True
perlu_login = not sudah_login
print(perlu_login)       # False

# ========================================
# 4. TABEL KEBENARAN (RANGKUMAN)
# ========================================
# AND (semua harus True):
#   True  and True  -> True
#   True  and False -> False
#   False and True  -> False
#   False and False -> False
#
# OR (cukup satu True):
#   True  or True  -> True
#   True  or False -> True
#   False or True  -> True
#   False or False -> False
#
# NOT (dibalik):
#   not True  -> False
#   not False -> True

# ========================================
# 5. PRIORITAS OPERATOR
# ========================================
# Urutan (paling tinggi dulu): not -> and -> or
# Sama seperti Dart: ! -> && -> ||
#
# Tips: selalu pakai kurung () agar jelas, meski tidak wajib.

print(True or False and False)    # True  (and dulu: False and False = False, lalu True or False)
print((True or False) and False)  # False (kurung mengubah urutan: True and False)

# ========================================
# 6. SHORT-CIRCUIT EVALUATION
# ========================================
# Python (dan Dart juga!) berhenti mengevaluasi begitu hasilnya pasti:
# - False and ...  -> langsung False, sisa kondisi TIDAK dicek
# - True or ...    -> langsung True, sisa kondisi TIDAK dicek
#
# Analogi Dart yang mungkin pernah kamu pakai:
#   data != null && data.isNotEmpty   <- kalau null, isNotEmpty tidak dijalankan
#   (mencegah null check error)

umur = 15
# (umur >= 17) sudah False, jadi punya_sim tidak perlu dicek
hasil = (umur >= 17) and True
print(hasil)             # False

# ========================================
# 7. KASUS PRAKTIS: GABUNGAN SEMUANYA
# ========================================
# Seleksi admin: usia 20-30, punya sertifikat, bukan mantan terdakwa
usia = 25
punya_sertifikat = True
terdakwa = False

# Perhatikan pemisahan ke variabel bernama - lebih mudah dibaca
# daripada satu baris panjang (best practice yang sama di Dart)
usia_cukup = (usia >= 20) and (usia <= 30)   # bisa juga: 20 <= usia <= 30
bersih = not terdakwa

lolos = usia_cukup and punya_sertifikat and bersih
print(lolos)             # True

# ========================================
# RANGKUMAN
# ========================================
# and  : semua True -> True           (Dart: &&)
# or   : satu saja True -> True       (Dart: ||)
# not  : membalik True/False          (Dart: !)
# Prioritas: not -> and -> or         (Dart: ! -> && -> ||)
# Kedua bahasa sama-sama short-circuit
# Catatan: hasil operasi logika siap dipakai di if/else (materi berikutnya!)
