from flask import Flask, request, send_file
import hashlib
import os
import subprocess
from piper import PiperVoice
import json
import wave
import io

app = Flask(__name__)
CACHE_DIR = "/app/cache"
MODEL_PATH = "/app/models/fr_FR-upmc-medium.onnx"
CONFIG_PATH = "/app/models/fr_FR-upmc-medium.onnx.json"

# Initialisation de Piper TTS
with open(CONFIG_PATH) as f:
    config = json.load(f)
piper_tts = PiperVoice.load(MODEL_PATH, config_path=CONFIG_PATH)

@app.route("/service/KarotzRvTTS")
def tts():
    text = request.args.get("text", "")
    lang = request.args.get("language", "fr-FR")
    gender = request.args.get("gender", "female")

    if lang == "fr": 
        lang = "fr-FR"

    md5Hash = hashlib.md5((lang + gender + text).encode("utf-8")).hexdigest()
    mp3_path = f"{CACHE_DIR}/{md5Hash}.mp3"
    wav_path = f"{CACHE_DIR}/{md5Hash}.wav"

    if not os.path.isfile(mp3_path):
        # Génération du fichier WAV avec Piper
        wav_io = io.BytesIO()
        with wave.open(wav_io, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(piper_tts.config.sample_rate)
            piper_tts.synthesize(text, wav_file)
        
        # Écriture du fichier WAV temporaire
        with open(wav_path, 'wb') as f:
            f.write(wav_io.getvalue())
        
        # Conversion en MP3
        subprocess.run([
            "ffmpeg", "-y",
            "-i", wav_path,
            "-codec:a", "libmp3lame",
            "-q:a", "2",
            mp3_path
        ])
        os.remove(wav_path)

    return send_file(mp3_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 