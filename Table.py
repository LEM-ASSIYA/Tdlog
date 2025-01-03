import random

class Table:
    def __init__(self, id_table, capacite):
        self.id_table = id_table
        self.capacite = capacite
        self.occupee = False  # Par défaut, la table est libre

    def assigner_table(self):
        if not self.occupee:
            self.occupee = True
            print(f"La table {self.id_table} est maintenant occupée.")
        else:
            print(f"La table {self.id_table} est déjà occupée.")

    def liberer_table(self):
        if self.occupee:
            self.occupee = False
            print(f"La table {self.id_table} est maintenant libre.")
        else:
            print(f"La table {self.id_table} est déjà libre.")

    def __str__(self):
        etat = "occupée" if self.occupee else "libre"
        return f"Table {self.id_table} (Capacité: {self.capacite}) - {etat}"



# Création des tables avec une capacité aléatoire entre 1 et 4
tables = [Table(i, random.randint(1, 4)) for i in range(1, 11)]  # 10 tables avec des capacités aléatoires

# Affichage des tables
for table in tables:
    print(table)
