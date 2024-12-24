# Usamos una imagen base oficial de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requisitos y luego instalamos las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente dentro del contenedor
COPY . /app/

# Exponemos el puerto donde Sanic ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación Sanic
CMD ["python", "app.py"]