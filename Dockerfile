# Usa una imagen base de Python
FROM python:3.11.7-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Copia el resto de la aplicación al directorio de trabajo
COPY . .

# Exponer el puerto en el que la aplicación se ejecutará
EXPOSE 8000

# Define el comando por defecto para ejecutar la aplicación
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "myproject.asgi:application"]