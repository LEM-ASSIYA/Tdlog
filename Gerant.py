class Gerant(Utilisateur):
    def _init_(self, id, nom, email, mot_de_passe):
        super()._init_(id, nom, email, mot_de_passe)

    def gerer_employes(self):
        print(f"Le gérant {self.nom} gère les employés.")

    def consulter_rapports(self):
        print(f"Le gérant {self.nom} consulte les rapports.")