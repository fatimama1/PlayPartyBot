FROM python:3.11-slim

# Рабочая директория
WORKDIR /app

# Копируем зависимости и ставим
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь код
COPY . /app


CMD ["python", "-m", "app.main"]
