FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala venv y crea un entorno virtual
RUN python -m venv /opt/venv

# Activa el entorno virtual y actualiza pip
RUN /opt/venv/bin/pip install --upgrade pip

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias en el entorno virtual
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Establece las variables de entorno para usar el venv
ENV PATH="/opt/venv/bin:$PATH"

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]