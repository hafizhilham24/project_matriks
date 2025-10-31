# Gunakan image Python resmi sebagai dasar
FROM python:3.11-slim

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# Salin file daftar library terlebih dahulu
COPY requirements.txt .

# Install semua library yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file proyek Anda ke dalam direktori kerja di container
COPY . .

# Beri tahu Docker port mana yang akan diekspos oleh aplikasi Anda
EXPOSE 5000

# Perintah untuk menjalankan aplikasi Flask saat container dimulai
# --host=0.0.0.0 penting agar bisa diakses dari luar container
CMD ["flask", "run", "--host=0.0.0.0"]
