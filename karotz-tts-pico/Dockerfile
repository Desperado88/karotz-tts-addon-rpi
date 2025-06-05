ARG BUILD_FROM
FROM $BUILD_FROM

ENV DEBIAN_FRONTEND=noninteractive

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libttspico-utils \
        sox \
        ffmpeg \
        python3 \
        python3-pip \
        libmp3lame0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY pico_tts.py .

VOLUME ["/app/cache"]

EXPOSE 5000

# Labels
LABEL \
    io.hass.name="Karotz TTS Pico" \
    io.hass.description="TTS local pour Karotz utilisant Pico TTS" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION}

CMD ["python3", "pico_tts.py"] 