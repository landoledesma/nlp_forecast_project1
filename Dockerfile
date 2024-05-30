# Usar una imagen base de Python
FROM python:3.9

# Instalar dependencias necesarias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    firefox-esr \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalar geckodriver
RUN GECKODRIVER_VERSION=$(curl -sS https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d\" -f4) \
    && wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ \
    && rm /tmp/geckodriver.tar.gz



# Crear el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos al contenedor
COPY requirements_scraping.txt /app/requirements_scraping.txt

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r /app/requirements_scraping.txt

# Copiar el script de scraping al contenedor
COPY scripts/web_scraping.py /app/scripts/web_scraping.py

# Crear el directorio de datos
RUN mkdir -p /app/data

CMD ["python", "/app/scripts/web_scraping.py"]