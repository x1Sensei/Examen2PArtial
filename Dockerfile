# Usar una imagen base de Python 3
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos locales dentro del contenedor
COPY . /app

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto donde Flask escuchará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
