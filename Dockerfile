# syntax=docker/dockerfile:1.6
# ------------------------------------------------------------
# Базовый образ с Python 3.12 (подойдёт как для CPU, так и GPU‑хостов)
# ------------------------------------------------------------
FROM python:3.12

# Добавляем необходимые системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
        git build-essential \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TRANSFORMERS_CACHE=/app/.cache

WORKDIR /app

# ------------------------------------------------------------
# Зависимости Python
# ------------------------------------------------------------
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# Копируем исходный код приложения
# ------------------------------------------------------------
COPY . ./

# ------------------------------------------------------------
# Запуск сервера
# ------------------------------------------------------------
EXPOSE 8000
CMD ["uvicorn", "rag_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
