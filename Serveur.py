class Serveur(Utilisateur):
    def __init__(self, ids, nom, email, mot_de_passe):
        super().__init__(ids, nom, email, mot_de_passe)
        self.liste_tables_attribuees = []

    def prendre_commande(self):
        print(f"{self.nom} a pris une commande.")

    def servir_plat(self):
        print(f"{self.nom} sert un plat.")

    def assigner_table(self, table):
        self.liste_tables_attribuees.append(table)
        print(f"{self.nom} a assigné la table {table.num_table}.")