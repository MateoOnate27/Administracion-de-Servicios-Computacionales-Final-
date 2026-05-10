FROM python:3.11-slim

WORKDIR /app

# Instalamos todo en una sola línea para evitar capas corruptas
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn numpy python-multipart

COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
