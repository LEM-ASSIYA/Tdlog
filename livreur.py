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





    def recuperer_adresse_client(self, commande):
        """Retourne l'adresse du client pour une commande donnée."""
        if "adresse_client" in commande:
            adresse = commande["adresse_client"]
            print(f"L'adresse du client pour la commande {commande['id']} est {adresse}.")
            return adresse
        else:
            print(f"Aucune adresse trouvée pour la commande {commande['id']}.")
            return None




    def effectuer_livraison(self, commande):
        """Effectuer la livraison et notifier le restaurant, avec gestion des problèmes éventuels."""
        if not self.commande_en_livraison:
            print(f"Aucune commande en cours de livraison pour le livreur {self.nom}.")
            return

        print(f"Livreur {self.nom} effectue la livraison pour la commande {commande['id']}.")

        # Demander des retours après la livraison
        probleme = input("Avez-vous rencontré un problème pendant la livraison (mauvais plat, client indisponible, etc.) ? (oui/non) ").strip().lower()
        
        if probleme == "oui":
            description_probleme = input("Veuillez décrire le problème : ")
            self.notifier_probleme_livraison(commande, description_probleme)
        else:
            print(f"Livreur {self.nom} a effectué la livraison sans problème.")
            self.notifier_restaurant_livraison_effectuee(commande)

        # Réinitialiser la commande en cours de livraison
        self.commande_en_livraison = None



    def notifier_probleme_livraison(self, commande, description_probleme):
        """Notifie le restaurant d'un problème lors de la livraison."""
        print(f"Problème signalé pour la commande {commande['id']}: {description_probleme}. Le restaurant est informé.")



    def notifier_restaurant_livraison_effectuee(self, commande):
        """Notifie le restaurant que la livraison est effectuée."""
        print(f"Livreur {self.nom} informe le restaurant que la commande {commande['id']} a été livrée avec succès.")


commande = {
    "id": 101,
    "plat": "Pizza Margherita",
    "ingredients": ["tomate", "fromage", "basilic"],
    "statut": "Prêt",
    "adresse_client": "123 Rue de la Pizzeria"
}

livreur = Livreur(1, "Livreur Paul", "0601020304")

# Le serveur notifie le livreur que la commande est prête
livreur.recevoir_notification(commande)

# Le livreur récupère l'adresse du client
livreur.recuperer_adresse_client(commande)

# Le livreur effectue la livraison
livreur.effectuer_livraison(commande)
