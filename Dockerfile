# 1. Базовый образ — используем Python 3.11
FROM python:3.13-slim

# 2. Создаём не-root пользователя (требование Hugging Face)[reference:1]
RUN useradd -m -u 1000 user
USER user

# 3. Настраиваем пути
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /app

# 4. Копируем и устанавливаем зависимости (слой для кэширования)
COPY --chown=user requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 5. Копируем весь код приложения
COPY --chown=user . /app

# 6. Порт 7860 — стандартный для Hugging Face Spaces[reference:2][reference:3]
EXPOSE 7860

# 7. Команда запуска
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]