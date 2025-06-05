# Karotz TTS Addons pour Home Assistant

Ce dépôt contient deux versions de l'addon TTS pour Karotz :

1. **karotz-tts-pico** : Version utilisant Pico TTS (recommandé pour Raspberry Pi 3 et 4)
2. **karotz-tts-piper** : Version utilisant Piper TTS (recommandé pour Raspberry Pi 5)

## Installation

1. Dans Home Assistant, allez dans "Paramètres" > "Modules complémentaires" > "Boutique des modules complémentaires"
2. Cliquez sur les trois points en haut à droite et sélectionnez "Dépôts"
3. Ajoutez ce dépôt : `https://github.com/mathieucourcelle/karotz-tts-addon-rpi5`
4. Redémarrez Home Assistant
5. Les deux addons apparaîtront dans la boutique des modules complémentaires

## Choix de l'addon

- **Pour Raspberry Pi 3/4** : Installez `karotz-tts-pico`
- **Pour Raspberry Pi 5** : Installez `karotz-tts-piper`

## Configuration

Les deux addons utilisent la même interface et sont compatibles avec le script Python existant. La seule différence est le moteur de synthèse vocale utilisé.

## Utilisation

L'addon expose un service web sur le port 5000 (ou le port configuré) qui peut être utilisé avec le script Python existant :

```python
baseUrl = "http://localhost:5000/service/KarotzRvTTS"
```

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub. 