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

requete_superficie = "SELECT SUM(superficie) AS superficie_totale FROM etage"
curseur.execute(requete_superficie)

resultat_superficie = curseur.fetchone()

superficie_totale = resultat_superficie[0]

print(f"La superficie de La Plateforme est de {superficie_totale} m2")

curseur.close()
connexion.close()
