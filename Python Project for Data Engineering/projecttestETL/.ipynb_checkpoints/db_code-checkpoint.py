# Importation des bibliothèques nécessaires
import sqlite3  # Pour interagir avec la base de données SQLite
import pandas as pd  # Pour manipuler les données sous forme de DataFrame

# Définition du nom de la base de données SQLite
db_name = 'STAFF.db'

# Connexion à la base de données SQLite (crée la base si elle n'existe pas)
conn = sqlite3.connect('STAFF.db')

# Nom de la table dans laquelle les données seront insérées
table_name = 'INSTRUCTOR'

# Définition de la liste des attributs (colonnes) pour les données
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Chemin d'accès au fichier CSV contenant les données à insérer
file_path = '/home/tegongue/Documents/formations/Data/IBM Data Engineering Certificat Professionnel/Python Project for Data Engineering/project/INSTRUCTOR.csv'

# Lecture du fichier CSV dans un DataFrame pandas avec les colonnes définies
df = pd.read_csv(file_path, names=attribute_list)

# Insertion du DataFrame dans la table SQLite. 
# Si la table existe déjà, elle sera remplacée.
df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready')  # Indique que la table est prête

# Requête SQL pour sélectionner la colonne 'FNAME' dans la table 'INSTRUCTOR'
query_statement = f"SELECT FNAME FROM {table_name}"
# Exécution de la requête SQL et récupération du résultat dans un DataFrame
query_output = pd.read_sql(query_statement, conn)
# Affichage de la requête et du résultat
print(query_statement)
print(query_output)

# Requête SQL pour sélectionner toutes les colonnes de la table 'INSTRUCTOR'
query_statement = f"SELECT * FROM {table_name}"
# Exécution de la requête SQL et récupération du résultat dans un DataFrame
query_output = pd.read_sql(query_statement, conn)
# Affichage de la requête et du résultat
print(query_statement)
print(query_output)

# Requête SQL pour compter le nombre de lignes dans la table 'INSTRUCTOR'
query_statement = f"SELECT COUNT(*) FROM {table_name}"
# Exécution de la requête SQL et récupération du résultat dans un DataFrame
query_output = pd.read_sql(query_statement, conn)
# Affichage de la requête et du résultat
print(query_statement)
print(query_output)

# Création d'un dictionnaire avec des données à ajouter à la table
data_dict = {'ID': [100],
             'FNAME': ['John'],
             'LNAME': ['Doe'],
             'CITY': ['Paris'],
             'CCODE': ['FR']}
# Conversion du dictionnaire en DataFrame pandas
data_append = pd.DataFrame(data_dict)

# Insertion des nouvelles données dans la table SQLite. 
# Les données seront ajoutées à la table existante sans la remplacer.
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')  # Indique que les données ont été ajoutées avec succès

# Fermeture de la connexion à la base de données SQLite
conn.close()
