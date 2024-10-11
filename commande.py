class Commande:
    def _init_(self, id_commande, date_commande):
        self.id_commande = id_commande
        self.date_commande = date_commande
        self.plats = []
        self.status_commande = "En attente"

    def ajouter_plat(self, plat):
        self.plats.append(plat)
        print(f"Le plat {plat.nom} a été ajouté à la commande {self.id_commande}.")

    def calculer_total(self):
        total = sum(plat.prix for plat in self.plats)
        return total

    def changer_status(self, status):
        self.status_commande = status
        print(f"Le statut de la commande {self.id_commande} a été changé à {status}.")