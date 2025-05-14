#!/bin/bash

# Fichier de journal pour les températures
LOG_FILE="temperature.log"
CSV_FILE="temp_stats.csv"

# Étape 1 : Extraction - Générer des données de température simulées
echo "Génération de données de température..."
for i in {1..60}; do
    # Simuler une température aléatoire entre -10 et 40 degrés Celsius
    TEMP=$(($RANDOM % 51 - 10))
    echo "$(date '+%Y-%m-%d %H:%M:%S') $TEMP" >> $LOG_FILE
done

# Étape 2 : Transformation - Calculer la température moyenne
echo "Calcul des statistiques de température..."
awk '{sum+=$2; count++} END {if (count > 0) print "Moyenne:", sum/count}' $LOG_FILE > $CSV_FILE

# Étape 3 : Chargement - Charger les résultats dans un fichier CSV
echo "Chargement des résultats dans le fichier $CSV_FILE"
echo "Date, Température Moyenne" > $CSV_FILE
echo "$(date '+%Y-%m-%d %H:%M:%S'), $(cat $CSV_FILE | tail -n 1)" >> $CSV_FILE

echo "Processus ETL terminé."
