FROM python:3.11-slim

WORKDIR /app

# Copiar requerimientos e instalarlos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Variables de entorno para Flask
ENV FLASK_APP=app:create_app
ENV FLASK_ENV=production

EXPOSE 5000

# Ejecutar con gunicorn (usa la factory create_app)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"] install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
