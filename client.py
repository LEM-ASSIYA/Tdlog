
from utilisateur import Utilisateur
class Client(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe, adresse, allergies=None):
        super().__init__(id, nom, email, mot_de_passe)
        self.adresse = adresse
        self.allergies = allergies  # Liste ou chaîne de caractères décrivant les allergies
        self.historique_commandes = []

    def passer_commande(self, commande):
        self.historique_commandes.append(commande)
        print(f"Commande {commande.id_commande} passée pour le client {self.nom} avec considération des allergies et maladies chroniques")

    def payer_facture(self, facture):
        print(f"Facture {facture.id_facture} payée pour le montant de {facture.montant_total}€")

    def faire_reservation(self, reservation):
        print(f"Réservation {reservation.id_reservation} faite au nom de {self.nom}") 


    def mettre_a_jour_infos(self, adresse=None, email=None, allergies=None, maladies_chroniques=None):
        if adresse:
            self.adresse = adresse
        if email:
            self.email = email
        if allergies:
            self.allergies = allergies
        print("Informations mises à jour avec succès.")

    def afficher_historique_commandes(self):
        if not self.historique_commandes:
            print("Aucune commande passée jusqu'à présent.")
        for commande in self.historique_commandes:
            print(f"Commande ID: {commande.id_commande}, Date: {commande.date_commande}, Total: {commande.calculer_total()}€")


    def donner_avis(self, commande, avis):
        commande.avis = avis
        print(f"Avis ajouté pour la commande {commande.id_commande}: {avis}")
        
        
    def obtenir_recommandations(self, menu):
        recommandations = []
        for plat in menu.liste_plats:
            if not any(allergene in plat.ingredients for allergene in self.allergies):
                recommandations.append(plat)
        return recommandations
    