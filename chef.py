from abc import ABC, abstractmethod

# Classe abstraite Utilisateur
class Utilisateur(ABC):
    def __init__(self, id, nom, email, mot_de_passe):
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.logged_in = False

    @abstractmethod
    def se_connecter(self, mot_de_passe):
        pass

    @abstractmethod
    def se_deconnecter(self):
        pass

# Classe Chef qui hérite de Utilisateur
class Chef(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe):
        super(Chef, self).__init__(id, nom, email, mot_de_passe)
        self.commandes = []

    def se_connecter(self, mot_de_passe):
        """Permet au chef de se connecter s'il fournit le bon mot de passe."""
        if self.mot_de_passe == mot_de_passe:
            self.logged_in = True
            print(f"{self.nom} s'est connecté avec succès.")
        else:
            print("Mot de passe incorrect.")

    def se_deconnecter(self):
        """Permet au chef de se déconnecter."""
        self.logged_in = False
        print(f"{self.nom} s'est déconnecté.")

    def consulter_commandes(self):
        """Affiche toutes les commandes en attente."""
        if not self.commandes:
            print("Aucune commande pour l'instant.")
        else:
            for commande in self.commandes:
                print(f"Commande {commande['id']} : {commande['plat']} - Statut: {commande['statut']}")

    def recevoir_commande(self, commande, serveur):
        """Le chef reçoit la commande du serveur et l'associe à son nom."""
        commande["chef"] = self.nom
        commande["statut"] = "Reçue par le chef"
        self.commandes.append(commande)
        print(f"Commande {commande['id']} reçue et assignée à {self.nom}.")

    def verifier_ingredients(self, commande, ingredients_disponibles):
        """Vérifie si les ingrédients de la commande sont disponibles."""
        ingredients_commande = commande["ingredients"]
        for ingredient in ingredients_commande:
            if ingredient not in ingredients_disponibles:
                return False
        return True

    def valider_commande(self, commande, ingredients_disponibles, allergies_client):
        """Valide ou annule la commande en fonction des ingrédients et allergies."""
        # Vérifier la disponibilité des ingrédients
        if self.verifier_ingredients(commande, ingredients_disponibles):
            print(f"Les ingrédients sont disponibles pour la commande {commande['id']}.")
            commande["statut"] = "En préparation"
            return "Commande validée et en préparation."
        else:
            print(f"Les ingrédients pour la commande {commande['id']} sont indisponibles.")
            commande["statut"] = "Annulée"
            return "Commande annulée en raison de l'indisponibilité des ingrédients."

    def consulter_allergies(self, commande, allergies_client):
        """Vérifie la commande pour les ingrédients allergènes."""
        ingredients_commande = commande["ingredients"]
        for allergie in allergies_client:
            if allergie in ingredients_commande:
                print(f"Attention : allergie détectée pour l'ingrédient {allergie}!")
                return True
        return False

    def consulter_informations_commande(self, commande):
        """Affiche les informations détaillées d'une commande."""
        print(f"Détails de la commande {commande['id']}:")
        print(f"Plat: {commande['plat']}")
        print(f"Statut: {commande['statut']}")
        print(f"Chef: {commande.get('chef', 'Aucun chef assigné')}")
        print(f"Ingrédients: {', '.join(commande['ingredients'])}")

    def notifier_client_plat_pret(self, commande):
        """Notifie le client que le plat est prêt."""
        if commande["statut"] == "En préparation":
            print(f"Le plat pour la commande {commande['id']} est prêt. Le client est informé.")
            commande["statut"] = "Prêt"
        else:
            print(f"Commande {commande['id']} non prête. Aucun message envoyé au client.")

    def notifier_serveur(self, commande, serveur):
        """Notifie le serveur que le plat est prêt pour être récupéré."""
        if commande["statut"] == "Prêt":
            print(f"Le serveur {serveur.nom} est informé que la commande {commande['id']} est prête.")
        else:
            print(f"Commande {commande['id']} non prête. Aucune notification envoyée.")

chef = Chef(1, "Chef Pierre", "pierre@example.com", "chef123")
chef.se_connecter("chef123")  # Mot de passe correct
chef.se_deconnecter()          