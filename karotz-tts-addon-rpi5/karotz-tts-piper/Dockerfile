FROM python:3.11-slim

RUN apt-get update && \
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