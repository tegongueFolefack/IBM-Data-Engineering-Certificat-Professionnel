#!/bin/bash

# Initialiser le fichier journal
touch temperature.log

# Extraire une lecture de température
temperature=$(./get_temp_api)  # Remplace cette ligne par l'appel réel de l'API
echo "$(date +'%Y-%m-%d %H:%M:%S') - $temperature" >> temperature.log

# Conserver uniquement les 60 dernières lectures
tail -n 60 temperature.log > temp.log && mv temp.log temperature.log

# Appeler le script Python pour obtenir les statistiques
python3 get_stats.py temperature.log temp_stats.csv
