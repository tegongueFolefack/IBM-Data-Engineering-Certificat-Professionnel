#!/bin/bash


USER="root"
PASSWORD="Ii09yMcESUvRV1s5lCyXUa9p"
DATABASE="sales"
OUTPUT_FILE="sales_data.sql"

mysqldump -u $USER -p$PASSWORD $DATABASE sales_data > $OUTPUT_FILE

echo "Les données de la table sales_data ont été exportées vers $OUTPUT_FILE."
