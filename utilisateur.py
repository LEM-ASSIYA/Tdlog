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