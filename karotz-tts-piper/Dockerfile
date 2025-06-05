ARG BUILD_FROM
FROM $BUILD_FROM

# Install system packages
RUN \
    apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        ffmpeg \
        libmp3lame0 \
        git \
        cmake \
        pkg-config \
        libespeak-ng-dev \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Installation de Piper TTS
RUN pip3 install --no-cache-dir piper-tts flask

# Téléchargement du modèle français
RUN mkdir -p /app/models && \
    wget -O /app/models/fr_FR-upmc-medium.onnx https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/upmc/medium/fr_FR-upmc-medium.onnx && \
    wget -O /app/models/fr_FR-upmc-medium.onnx.json https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/upmc/medium/fr_FR-upmc-medium.onnx.json

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY piper_tts.py /app/
RUN mkdir -p /app/cache

CMD ["python3", "/app/piper_tts.py"]

# Labels
LABEL \
    io.hass.name="Karotz TTS Piper" \
    io.hass.description="TTS local pour Karotz utilisant Piper TTS" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} 