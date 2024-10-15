class Livreur:
    def __init__(self, id, nom, telephone):
        self.id = id
        self.nom = nom
        self.telephone = telephone
        self.commande_en_livraison = None

    def recevoir_notification(self, commande):
        """Recevoir une notification du serveur pour une commande prête à être livrée."""
        if commande["statut"] == "Prêt":
            self.commande_en_livraison = commande
            print(f"Livreur {self.nom} a reçu la notification pour la commande {commande['id']} à livrer.")
        else:
            print(f"Aucune commande prête pour livraison.")


