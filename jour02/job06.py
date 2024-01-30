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

requete_capacite = "SELECT SUM(capacite) AS capacite_totale FROM salle"
curseur.execute(requete_capacite)

resultat_capacite = curseur.fetchone()

capacite_totale = resultat_capacite[0]

print(f"La capacité totale des salles est de {capacite_totale}")

curseur.close()
connexion.close()
