import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Justine11081994.",
    database="zoo"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    race VARCHAR(255) NOT NULL,
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    superficie FLOAT NOT NULL,
    capacite_max INT NOT NULL
)
""")

def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    cursor.execute("""
    INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
    VALUES (%s, %s, %s, %s, %s)
    """, (nom, race, id_cage, date_naissance, pays_origine))
    db.commit()

def supprimer_animal(animal_id):
    cursor.execute("DELETE FROM animal WHERE id = %s", (animal_id,))
    db.commit()

def modifier_animal(animal_id, nom, race, id_cage, date_naissance, pays_origine):
    cursor.execute("""
    UPDATE animal
    SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s
    WHERE id = %s
    """, (nom, race, id_cage, date_naissance, pays_origine, animal_id))
    db.commit()

def afficher_animaux():
    cursor.execute("SELECT * FROM animal")
    result = cursor.fetchall()
    for row in result:
        print(row)

def afficher_animaux_cage(cage_id):
    cursor.execute("SELECT * FROM animal WHERE id_cage = %s", (cage_id,))
    result = cursor.fetchall()
    for row in result:
        print(row)

def ajouter_cage(superficie, capacite_max):
    cursor.execute("""
    INSERT INTO cage (superficie, capacite_max)
    VALUES (%s, %s)
    """, (superficie, capacite_max))
    db.commit()

def supprimer_cage(cage_id):
    cursor.execute("DELETE FROM cage WHERE id = %s", (cage_id,))
    db.commit()

def modifier_cage(cage_id, superficie, capacite_max):
    cursor.execute("""
    UPDATE cage
    SET superficie = %s, capacite_max = %s
    WHERE id = %s
    """, (superficie, capacite_max, cage_id))
    db.commit()

def afficher_cages():
    cursor.execute("SELECT * FROM cage")
    result = cursor.fetchall()
    for row in result:
        print(row)

def calculer_superficie_totale():
    cursor.execute("SELECT SUM(superficie) FROM cage")
    result = cursor.fetchone()
    superficie_totale = result[0]
    print("Superficie totale de toutes les cages : {} m²".format(superficie_totale))

ajouter_cage(100, 5)
ajouter_cage(150, 10)

ajouter_animal("Lion", "Félin", 1, "2020-01-01", "Afrique")
ajouter_animal("Ours", "Ursidé", 1, "2018-05-15", "Amérique du Nord")
ajouter_animal("Girafe", "Giraffa camelopardalis", 2, "2019-08-20", "Afrique")

afficher_cages()
afficher_animaux()
afficher_animaux_cage(1)

calculer_superficie_totale()

db.close()
