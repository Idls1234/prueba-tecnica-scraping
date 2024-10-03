# Usa la imagen base de Playwright
FROM python:3.12-bookworm

# Establece el directorio de trabajo
WORKDIR /app

# Instala Playwright y sus dependencias
RUN pip install playwright==1.47.0 && \
    playwright install --with-deps


# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias en el entorno virtual
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "routes.py"]