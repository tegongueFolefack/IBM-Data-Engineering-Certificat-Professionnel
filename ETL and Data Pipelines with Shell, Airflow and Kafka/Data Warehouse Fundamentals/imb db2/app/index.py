import os
import ibm_db

# Récupération des variables d'environnement
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# URL de connexion Db2
dsn = (
    f"DATABASE={DB_NAME};"
    f"HOSTNAME={DB_HOST};"
    f"PORT={DB_PORT};"
    f"PROTOCOL=TCPIP;"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    f"SECURITY=SSL;"
)

try:
    # Connexion à la base de données
    conn = ibm_db.connect(dsn, "", "")
    print("Connexion réussie à IBM Db2 !")

    # Exécution d'une requête de test
    sql = "SELECT CURRENT_DATE FROM sysibm.sysdummy1"
    stmt = ibm_db.exec_immediate(conn, sql)
    result = ibm_db.fetch_assoc(stmt)
    print("Résultat de la requête :", result)

    # Fermeture de la connexion
    ibm_db.close(conn)
except Exception as e:
    print("Échec de la connexion :", str(e))
