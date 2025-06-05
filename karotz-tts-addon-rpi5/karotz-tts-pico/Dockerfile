FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
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

CMD ["python3", "pico_tts.py"] 