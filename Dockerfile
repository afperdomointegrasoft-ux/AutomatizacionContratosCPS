# Dockerfile para automatización de pruebas
FROM python:3.9-slim

# Instalar dependencias del sistema para Selenium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium-driver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Configurar Chrome para modo headless
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_PATH=/usr/lib/chromium/
ENV DISPLAY=:99

WORKDIR /app

# Copiar el proyecto de automatización
COPY AutomatizacionContratosCPS/ ./

# Crear requirements.txt si no existe
RUN echo "selenium==4.15.2\npytest==7.4.3\nrequests==2.31.0" > requirements.txt

# Instalar dependencias de Python
RUN pip install -r requirements.txt

# Exponer puerto (opcional, para reportes web)
EXPOSE 8000

# Comando para ejecutar las pruebas
CMD ["python", "main.py"]
