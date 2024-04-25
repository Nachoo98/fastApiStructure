FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar las dependencias
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . .

# Exponer el puerto en el que la aplicación FastAPI estará escuchando
EXPOSE 5000

# Ejecutar la aplicación FastAPI
CMD ["python", "app/main.py"]  # Ajustar la ruta según la ubicación de main.py
