class Utilisateur:
    def _init_(self, id, nom, email, mot_de_passe):
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe

    def se_connecter(self):
        print(f"{self.nom} connecté.")

    def se_deconnecter(self):
        print(f"{self.nom} déconnecté.")
        
        
class Serveur(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe, id_serveur):
        super().__init__(id, nom, email, mot_de_passe)
        self.id_serveur = id_serveur
        self.liste_tables_attribuees = []

    def prendre_commande(self):
        print(f"{self.nom} a pris une commande.")

    def servir_plat(self):
        print(f"{self.nom} sert un plat.")

    def assigner_table(self, table):
        self.liste_tables_attribuees.append(table)
        print(f"{self.nom} a assigné la table {table.num_table}.")