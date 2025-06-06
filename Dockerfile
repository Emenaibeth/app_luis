# Descargar la imagen oficial de python
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear Directorio de trabajo
WORKDIR /home/app

# Instalar paquetes

COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el directorio del entorno virtual
COPY . /home/app

# Exponer el puerto 8000
EXPOSE 40000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:40000" ]