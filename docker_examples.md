# Contoh Penggunaan Docker

## 1. Menjalankan Container Pertama

Setelah Docker terinstal, coba perintah berikut:

```bash
# Menjalankan container hello-world
docker run hello-world
```

## 2. Menjalankan Web Server Nginx

```bash
# Menjalankan Nginx dan memetakan port 8080 ke port 80 container
docker run -d -p 8080:80 --name my-nginx nginx

# Akses di browser: http://localhost:8080
```

## 3. Menjalankan Container Interaktif

```bash
# Menjalankan container Ubuntu secara interaktif
docker run -it --name my-ubuntu ubuntu /bin/bash

# Di dalam container, Anda bisa:
# - apt update && apt install -y python3
# - python3 --version
# - exit (untuk keluar)
```

## 4. Mengelola Container

```bash
# Melihat container yang sedang berjalan
docker ps

# Melihat semua container (termasuk yang berhenti)
docker ps -a

# Menghentikan container
docker stop my-nginx

# Memulai container yang sudah berhenti
docker start my-nginx

# Menghapus container
docker rm my-nginx
```

## 5. Mengelola Image

```bash
# Melihat image yang tersedia
docker images

# Mengunduh image
docker pull python:3.9

# Menghapus image
docker rmi nginx
```

## 6. Dockerfile Sederhana

Buat file bernama `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Dan file `requirements.txt`:

```
flask==2.0.1
```

Dan file `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Kemudian build dan jalankan:

```bash
# Build image
docker build -t my-flask-app .

# Jalankan container
docker run -d -p 5000:5000 --name flask-app my-flask-app

# Akses di browser: http://localhost:5000
```

## 7. Docker Compose

Buat file `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

Jalankan dengan:

```bash
# Menjalankan semua services
docker-compose up -d

# Menghentikan semua services
docker-compose down

# Melihat logs
docker-compose logs