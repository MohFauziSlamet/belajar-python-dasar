# ========================================
# PERULANGAN (LOOPS)
# ========================================

# Perulangan = menjalankan blok kode berkali-kali, sampai kondisi berhenti terpenuhi.
# (Sumber: materi-pdf "Python Dasar.pdf" halaman 86 - 101)
#
# Jika di Dart seperti ini → di Python jadi seperti ini:
#   - Dart for (var i = 0; i < n; i++)  →  Python for i in range(n)
#   - Dart for (var item in list)       →  Python for item in koleksi
#   - Dart while (kondisi)              →  Python while kondisi: (sama persis)
#   - Dart break / continue             →  Python break / continue (sama persis)
#
# Jebakan untuk dev Dart:
#   1. Python TIDAK punya for (i = 0; i < n; i++) — selalu pakai range()
#   2. Python punya fitur unik: for-else dan while-else (Dart tidak punya)
#   3. range(5) = 0,1,2,3,4 (berhenti SEBELUM 5, mirip Dart i < 5)

# ========================================
# 1. FOR LOOP DENGAN range()
# ========================================
# range(n)      → 0 sampai n-1
# range(a, b)   → a sampai b-1
# range(a, b, s)→ a sampai b-1 dengan langkah s
#
# Jika di Dart: for (var i = 0; i < n; i++) { ... } → di Python: for i in range(n):

print("--- range(5): 0 sampai 4 ---")
for i in range(5):
    print(i)  # 0  1  2  3  4

print("--- range(1, 6): 1 sampai 5 ---")
for i in range(1, 6):
    print(i)  # 1  2  3  4  5

print("--- range(0, 10, 2): genap 0-8 ---")
for i in range(0, 10, 2):
    print(i)  # 0  2  4  6  8

# ========================================
# 2. FOR LOOP DENGAN STRING
# ========================================
# Iterasi setiap karakter dalam string, satu per satu.
# Jika di Dart: 'hello'.split('') dulu baru for-in → di Python: langsung for huruf in kata:

kata = "Python"
for huruf in kata:
    print(huruf)  # P  y  t  h  o  n  (satu per baris)

# ========================================
# 3. WHILE LOOP
# ========================================
# Mengulangi blok kode selama kondisi bernilai True.
# Hati-hati infinite loop! Pastikan kondisi akan False di suatu titik.
# Jika di Dart: while (kondisi) { ... } → di Python: sama persis, {} diganti indentasi + :

counter = 1
while counter <= 5:
    print(f"Hitungan ke-{counter}")  # Hitungan ke-1 ... ke-5
    counter += 1  # jangan lupa increment! (ingat: ++ tidak ada di Python, file 9)

# ========================================
# 4. BREAK — KELUAR DARI LOOP
# ========================================
# Menghentikan loop sepenuhnya saat kondisi tertentu terpenuhi.
# Jika di Dart: break; → di Python: break — sama persis.

print("--- break: cari angka 3 ---")
for i in range(1, 10):
    if i == 3:
        print(f"Ketemu {i}, berhenti!")  # Ketemu 3, berhenti!
        break
    print(i)  # 1  2

# ========================================
# 5. CONTINUE — LEWATI ITERASI SAAT INI
# ========================================
# Langsung lompat ke iterasi berikutnya, tanpa menjalankan kode di bawahnya.
# Jika di Dart: continue; → di Python: continue — sama persis.

print("--- continue: lewati angka genap ---")
for i in range(1, 6):
    if i % 2 == 0:
        continue  # skip 2 dan 4
    print(i)  # 1  3  5

# ========================================
# 6. FOR-ELSE (FITUR KHAS PYTHON!)
# ========================================
# Blok else dijalankan HANYA jika loop selesai secara NORMAL (tanpa break).
# Jika loop dihentikan oleh break, blok else di-skip.
# Dart TIDAK punya fitur ini — harus pakai variabel flag (bool found = false).
#
# Kasus: cari nama dalam daftar (belum pakai list, jadi pakai string + in)

target = "Dani"

print(f"--- cari '{target}' ---")
for nama in ["Andi", "Budi", "Citra"]:
    if nama == target:
        print(f"{target} ditemukan!")
        break
else:
    # Blok ini jalan karena loop selesai tanpa break (target tidak ada)
    print(f"{target} tidak ditemukan")  # Dani tidak ditemukan

# Bandingkan: di Dart kamu harus tulis begini:
#   bool found = false;
#   for (var nama in list) {
#     if (nama == target) { found = true; break; }
#   }
#   if (!found) print("tidak ditemukan");
# Python for-else jauh lebih ringkas.

# ========================================
# 7. WHILE-ELSE (FITUR KHAS PYTHON JUGA!)
# ========================================
# Sama seperti for-else: else dijalankan jika while selesai normal (tanpa break).

angka = 1
while angka <= 5:
    if angka == 99:  # kondisi yang tidak pernah terpenuhi
        break
    print(angka)  # 1  2  3  4  5
    angka += 1
else:
    print("While selesai normal, tidak kena break")  # While selesai normal, tidak kena break

# ========================================
# 8. NESTED LOOP (LOOP BERSARANG)
# ========================================
# Loop di dalam loop — setiap iterasi luar menjalankan seluruh loop dalam.
# Jika di Dart: for di dalam for → di Python: sama, blok dalam ditandai indentasi bertingkat.

print("--- tabel perkalian 1-3 ---")
for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris} x {kolom} = {baris * kolom}")
    # 1x1=1  1x2=2  1x3=3  2x1=2  2x2=4  2x3=6  3x1=3  3x2=6  3x3=9

# ========================================
# 9. KASUS PRAKTIS — HITUNG TOTAL BELANJA
# ========================================
# Kasir memasukkan harga barang satu per satu.
# Ketik 0 untuk berhenti dan lihat total.
# (Menggunakan while + break + input dari file 4)

# Catatan: bagian ini pakai input(), jadi dikomen agar file bisa dijalankan otomatis.
# Hapus komentar (#) untuk mencoba sendiri!

# total_belanja = 0
# while True:
#     harga = int(input("Masukkan harga barang (0 untuk selesai): "))
#     if harga == 0:
#         break
#     total_belanja += harga
#     print(f"  Subtotal: Rp {total_belanja}")
# print(f"Total belanja: Rp {total_belanja}")

# ========================================
# LATIHAN
# ========================================
# Kerjakan tanpa melihat contoh di atas:
#
# 1. Cetak angka 10, 9, 8, ... 1 menggunakan range() dengan langkah negatif.
#    (petunjuk: range(10, 0, -1))
#
# 2. Cetak semua angka 1-20 yang TIDAK habis dibagi 3.
#    (petunjuk: for + if + continue)
#
# 3. Buat countdown timer: while dari 5 ke 1, lalu print "GO!".
#    (petunjuk: while + decrement, "GO!" setelah loop selesai — bisa pakai while-else)

# ========================================
# RANGKUMAN
# ========================================
# 1. for i in range(n)   → ulangi dari 0 sampai n-1 (Dart: for i < n)
# 2. for item in koleksi → iterasi langsung per elemen (Dart: for-in)
# 3. while kondisi:      → ulangi selama True (sama dengan Dart)
# 4. break               → keluar loop sepenuhnya
# 5. continue            → lewati iterasi saat ini, lanjut ke iterasi berikutnya
# 6. for-else / while-else → else jalan jika loop selesai TANPA break (khas Python!)
# 7. Nested loop         → loop dalam loop, biasa untuk pola 2 dimensi
