# Usamos una imagen ligera de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias de ML
RUN pip install scikit-learn

# Copiar el script
COPY train.py .

# Comando por defecto
CMD ["python", "train.py"]
