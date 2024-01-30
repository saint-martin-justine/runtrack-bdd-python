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


requete = "SELECT * FROM etudiant"
curseur.execute(requete)

# Récupere les resultats 
resultats = curseur.fetchall()  

for etudiant in resultats:
    print(etudiant)

# Fermeture de la connexion
curseur.close()
connexion.close()


  

