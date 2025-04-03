# Import des bibliothèques nécessaires
import mysql.connector
from dotenv import load_dotenv
import os

# Charge les variables d'environnement depuis .env
load_dotenv("C:\DATA\mon_projet_data_etl_mysql\config\.env")  

# Création de la configuration de connexion à la base de données
config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'raise_on_warnings': True
}

# Connexion à la base de données
print("Debut de la connexion à la base de données...")

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # récupération des données de la table clients
    query = "SELECT * FROM clients"
    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    print(f"Erreur : {err}")


