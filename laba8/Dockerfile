# Dockerfile
FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Запускаем Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
