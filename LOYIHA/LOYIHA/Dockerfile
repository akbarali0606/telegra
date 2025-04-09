# Pythonni o‘rnatish
FROM python:3.9-slim

# Ishchi katalogni yaratish
WORKDIR /app

# requirements.txt faylini konteynerga ko‘chirish
COPY requirements.txt .

# Kerakli kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Barcha fayllarni konteynerga ko‘chirish
COPY . .

# FastAPI serverini ishga tushirish
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
