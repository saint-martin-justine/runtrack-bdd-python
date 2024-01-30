import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employe (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nom VARCHAR(255),
                prenom VARCHAR(255),
                salaire DECIMAL(10, 2),
                id_service INT
            )
        """)
        self.conn.commit()

    def insert_employe(self, nom, prenom, salaire, id_service):
        self.cursor.execute("""
            INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)
        """, (nom, prenom, salaire, id_service))
        self.conn.commit()

    def retrieve_employes(self):
        self.cursor.execute("SELECT * FROM employe")
        return self.cursor.fetchall()

    def update_employe(self, employe_id, new_salaire):
        self.cursor.execute("UPDATE employe SET salaire = %s WHERE id = %s", (new_salaire, employe_id))
        self.conn.commit()

    def delete_employe(self, employe_id):
        self.cursor.execute("DELETE FROM employe WHERE id = %s", (employe_id,))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "Justine11081994."
    database = "travail"

    employe_manager = Employe(host, user, password, database)
    employe_manager.create_table()

    employe_manager.insert_employe("Nemar", "Jean", 3500.00, 1)
    employe_manager.insert_employe("Ticipe", "Jean", 2800.50, 2)
    employe_manager.insert_employe("Porte", "Emma", 4000.75, 1)

    employes = employe_manager.retrieve_employes()
    for employe in employes:
        print(employe)

    employe_manager.update_employe(1, 3800.00)

    employes_apres_mise_a_jour = employe_manager.retrieve_employes()
    for employe in employes_apres_mise_a_jour:
        print(employe)

    employe_manager.delete_employe(2)

    employes_apres_suppression = employe_manager.retrieve_employes()
    for employe in employes_apres_suppression:
        print(employe)

    employe_manager.close_connection()
