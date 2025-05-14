# Ce script effectue des opérations ETL (Extraction, Transformation, Chargement) sur des données de PIB (Produit Intérieur Brut) de différents pays.

# Importation des bibliothèques nécessaires
from bs4 import BeautifulSoup  # Pour l'extraction des données d'une page web (parsing HTML)
import requests  # Pour envoyer des requêtes HTTP afin d'accéder aux pages web
import pandas as pd  # Pour manipuler les données sous forme de tableaux (dataframes)
import numpy as np  # Pour effectuer des calculs numériques, ici notamment pour manipuler les nombres flottants
import sqlite3  # Pour interagir avec une base de données SQLite
from datetime import datetime  # Pour enregistrer les horodatages (timestamps) lors de l'exécution du code

# Fonction d'extraction des données à partir d'un site web
def extract(url, table_attribs):
    ''' Cette fonction a pour but d'extraire les informations d'une page web
    et de les stocker dans un dataframe Pandas. Elle retourne ce dataframe pour des traitements ultérieurs. '''
    
    # Récupération de la page web sous forme de texte HTML
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')  # Analyse du code HTML avec BeautifulSoup

    # Création d'un dataframe vide avec les colonnes spécifiées (pays, PIB en millions de dollars)
    df = pd.DataFrame(columns=table_attribs)
    
    # Recherche des tables HTML dans le contenu de la page
    tables = data.find_all('tbody')  # 'tbody' correspond aux tables contenant les données dans HTML
    
    # Extraction des lignes de la troisième table ('tables[2]')
    rows = tables[2].find_all('tr')
    
    # Parcours de chaque ligne de la table
    for row in rows:
        col = row.find_all('td')  # Extraction des colonnes de la ligne
        if len(col) != 0:  # Vérification si la ligne n'est pas vide
            # Vérification que la colonne 0 (nom du pays) contient un lien ('a') et que la colonne 2 (PIB) n'a pas de symbole spécial
            if col[0].find('a') is not None and '—' not in col[2]:
                # Extraction des données de chaque pays (nom du pays et PIB en millions de dollars)
                data_dict = {"Country": col[0].a.contents[0],  # Nom du pays
                             "GDP_USD_millions": col[2].contents[0]}  # PIB en millions de dollars
                # Ajout des données au dataframe
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)  # Concaténation du nouveau dataframe avec les précédents
    return df  # Retourne le dataframe contenant les données extraites

# Fonction de transformation des données extraites
def transform(df):
    ''' Cette fonction convertit les informations du PIB de format monétaire
    en valeur flottante et transforme le PIB de millions à milliards de dollars.
    Le dataframe transformé est retourné. '''
    
    # Conversion du PIB de chaîne de caractères en nombres flottants
    GDP_list = df["GDP_USD_millions"].tolist()
    GDP_list = [float("".join(x.split(','))) for x in GDP_list]  # Suppression des virgules et conversion en float
    
    # Conversion des valeurs de millions à milliards et arrondi à deux décimales
    GDP_list = [np.round(x/1000, 2) for x in GDP_list]
    
    # Mise à jour du dataframe avec les nouvelles valeurs (en milliards)
    df["GDP_USD_millions"] = GDP_list
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})  # Renommage de la colonne en "PIB en milliards"
    
    return df  # Retourne le dataframe transformé

# Fonction pour sauvegarder les données dans un fichier CSV
def load_to_csv(df, csv_path):
    ''' Cette fonction sauvegarde le dataframe final sous la forme d'un fichier CSV
    à l'emplacement spécifié. La fonction ne retourne rien. '''
    
    df.to_csv(csv_path)  # Enregistrement du dataframe en CSV

# Fonction pour charger les données dans une base de données SQLite
def load_to_db(df, sql_connection, table_name):
    ''' Cette fonction enregistre le dataframe final dans une table de la base de données SQLite
    avec le nom fourni. La fonction ne retourne rien. '''
    
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)  # Chargement des données dans la table

# Fonction pour exécuter une requête SQL et afficher les résultats
def run_query(query_statement, sql_connection):
    ''' Cette fonction exécute une requête SQL sur la base de données et
    affiche les résultats dans le terminal. La fonction ne retourne rien. '''
    
    print(query_statement)  # Affiche la requête
    query_output = pd.read_sql(query_statement, sql_connection)  # Exécution de la requête
    print(query_output)  # Affichage des résultats

# Fonction pour enregistrer des messages de progression dans un fichier journal
def log_progress(message):
    ''' Cette fonction enregistre un message d'étape à chaque point clé du traitement 
    dans un fichier journal avec un horodatage. La fonction ne retourne rien. '''
    
    # Format de l'horodatage
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()  # Récupération de l'heure actuelle
    timestamp = now.strftime(timestamp_format)  # Formatage de l'horodatage
    
    # Enregistrement du message avec horodatage dans un fichier log
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')  # Ajout d'une nouvelle ligne dans le fichier log

''' Bloc principal du script où les fonctions précédentes sont appelées
dans l'ordre pour accomplir le projet ETL. Ce bloc ne fait partie d'aucune fonction.'''

# Définition de l'URL et des attributs de la table pour l'extraction
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]

# Définition des noms de fichiers pour la base de données et le fichier CSV
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'

# Enregistrement du début du processus ETL
log_progress('Preliminaries complete. Initiating ETL process')

# Extraction des données
df = extract(url, table_attribs)

# Enregistrement de la progression après l'extraction
log_progress('Data extraction complete. Initiating Transformation process')

# Transformation des données
df = transform(df)

# Enregistrement de la progression après la transformation
log_progress('Data transformation complete. Initiating loading process')

# Sauvegarde des données transformées dans un fichier CSV
load_to_csv(df, csv_path)

# Enregistrement de la progression après la sauvegarde dans un fichier CSV
log_progress('Data saved to CSV file')

# Connexion à la base de données SQLite
sql_connection = sqlite3.connect(db_name)

# Enregistrement de la progression après la connexion à la base de données
log_progress('SQL Connection initiated.')

# Chargement des données dans la base de données
load_to_db(df, sql_connection, table_name)

# Enregistrement de la progression après le chargement dans la base de données
log_progress('Data loaded to Database as table. Running the query')

# Définition de la requête SQL pour sélectionner les pays avec un PIB supérieur ou égal à 100 milliards de dollars
query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"

# Exécution de la requête et affichage des résultats
run_query(query_statement, sql_connection)

# Enregistrement de la progression après la fin du processus ETL
log_progress('Process Complete.')

# Fermeture de la connexion à la base de données
sql_connection.close()
