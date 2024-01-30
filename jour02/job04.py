import mysql.connector

host = "localhost"
user = "root"
password = "Justine11081994."
database = "Laplateforme"

connexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

curseur = connexion.cursor()

requete = "SELECT nom, capacite FROM salle"
curseur.execute(requete)

resultats = curseur.fetchall()

for salle in resultats:
    nom, capacite = salle
    print(f"Nom: {nom}, Capacité: {capacite}")

curseur.close()
connexion.close()
