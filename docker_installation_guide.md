# Panduan Instalasi Docker di macOS

## Metode 1: Menggunakan Homebrew (Direkomendasikan)

1. **Instal Docker Desktop menggunakan Homebrew Cask:**
   ```bash
   brew install --cask docker
   ```

2. **Setelah instalasi selesai:**
   - Buka aplikasi Docker dari folder Applications
   - Docker akan memulai proses inisialisasi (mungkin membutuhkan beberapa menit)
   - Ikuti instruksi yang muncul di layar

3. **Verifikasi instalasi:**
   ```bash
   docker --version
   docker-compose --version
   ```

## Metode 2: Download Manual

1. Kunjungi [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
2. Download Docker Desktop for Mac
3. Buka file .dmg yang telah diunduh
4. Seret Docker ke folder Applications
5. Buka aplikasi Docker dari folder Applications

## Konfigurasi Awal

1. **Buka Docker Desktop** setelah instalasi
2. **Accept terms and conditions** jika diminta
3. **Masukkan password** sistem Anda saat diminta
4. **Tunggu hingga Docker daemon berjalan** (ikon Docker di menu bar akan berhenti beranimasi)

## Verifikasi Instalasi

1. **Cek versi Docker:**
   ```bash
   docker --version
   ```

2. **Jalankan container test:**
   ```bash
   docker run hello-world
   ```

3. **Cek Docker Compose:**
   ```bash
   docker-compose --version
   ```

## Perintah Dasar Docker

- `docker ps` - Menampilkan container yang sedang berjalan
- `docker images` - Menampilkan image yang tersedia
- `docker pull <image>` - Mengunduh image dari registry
- `docker run <image>` - Menjalankan container dari image
- `docker stop <container>` - Menghentikan container
- `docker rm <container>` - Menghapus container
- `docker rmi <image>` - Menghapus image

## Troubleshooting

### Jika Docker tidak berjalan:
1. Pastikan Docker Desktop sedang berjalan (cek menu bar)
2. Restart Docker Desktop
3. Restart komputer jika perlu

### Jika mendapat error permission:
1. Pastikan user Anda memiliki akses ke Docker
2. Tambahkan user ke group docker jika menggunakan Docker Engine

### Jika command tidak ditemukan:
1. Pastikan Docker Desktop sudah berjalan
2. Restart terminal
3. Cek PATH environment variable

## Sumber Daya Tambahan

- [Docker Documentation](https://docs.docker.com/)
- [Docker Get Started](https://www.docker.com/101-tutorial)
- [Docker Hub](https://hub.docker.com/)