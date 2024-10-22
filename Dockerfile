# Gunakan image Python sebagai base
FROM python:3.11-slim

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file proyek ke dalam container
COPY . /app/

# Jalankan perintah untuk menyiapkan container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
