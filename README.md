# Karotz TTS Add-on

Ce dépôt permet d'ajouter un service TTS local pour Karotz à Home Assistant.

## Prérequis matériels

Cet addon nécessite au minimum un Raspberry Pi 3 B+ pour fonctionner correctement.

## Installation

1. Ajouter ce dépôt dans Home Assistant via `Paramètres > Modules complémentaires > ⚙️ Réglages > Dépôts` :
   ```
   https://github.com/Desperado88/karotz-tts-addon
   ```

2. Installer l'add-on "Karotz TTS"
3. Démarrer et activer le démarrage automatique

## Test

Tester depuis un autre appareil :
```
curl -L -o karotz.mp3 "http://[IP_DE_VOTRE_SERVEUR_HA]:5000/service/KarotzRvTTS?language=fr&gender=female&text=bonjour"
```

## Configuration du karotz

1. Connecter vous en ssh a votre karotz

2. Modifiez la ligne 49 du script Python dans `/www/cgi-bin/tts` :
   ```python
   baseUrl = "http://[IP_DE_VOTRE_SERVEUR_HA]:5000/service/KarotzRvTTS"
   ```