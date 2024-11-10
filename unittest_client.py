import unittest
import Client, Commande,Facture, Reservation, Plat, Menu

class TestClient(unittest.TestCase):

    def setUp(self):
        # Création d'un client pour les tests
        self.client = Client(
            id=1,
            nom="Jean Dupont",
            email="jean.dupont@example.com",
            mot_de_passe="securepassword123",
            adresse="123 Rue de la Paix, Paris",
            allergies=["arachides", "gluten"]
        )

    def test_initialisation_client(self):
        # Vérification de l'initialisation correcte de l'objet client
        self.assertEqual(self.client.id, 1)
        self.assertEqual(self.client.nom, "Jean Dupont")
        self.assertEqual(self.client.email, "jean.dupont@example.com")
        self.assertEqual(self.client.mot_de_passe, "securepassword123")
        self.assertEqual(self.client.adresse, "123 Rue de la Paix, Paris")
        self.assertEqual(self.client.allergies, ["arachides", "gluten"])

    def test_passer_commande(self):
        # Simulation de l'ajout d'une commande
        commande = Commande(id_commande=101, date_commande="2023-11-01")
        self.client.passer_commande(commande)
        self.assertIn(commande, self.client.historique_commandes)

    def test_payer_facture(self):
        # Simulation du paiement d'une facture
        facture = Facture(id_facture=201, montant_total=50)
        with self.assertLogs(level='INFO') as log:
            self.client.payer_facture(facture)
            self.assertIn('Facture 201 payée pour le montant de 50€', log.output[0])

    def test_faire_reservation(self):
        # Test de la méthode faire_reservation
        reservation = Reservation(id_reservation=301, nom=self.client.nom)
        with self.assertLogs(level='INFO') as log:
            self.client.faire_reservation(reservation)
            self.assertIn('Réservation 301 faite au nom de Jean Dupont', log.output[0])

    def test_mettre_a_jour_infos(self):
        # Mise à jour des informations du client
        self.client.mettre_a_jour_infos(adresse="456 Rue du Faubourg, Paris", email="jean.nouveau@example.com")
        self.assertEqual(self.client.adresse, "456 Rue du Faubourg, Paris")
        self.assertEqual(self.client.email, "jean.nouveau@example.com")

    def test_afficher_historique_commandes(self):
        # Vérification de l'affichage de l'historique des commandes
        commande = Commande(id_commande=101, date_commande="2023-11-01")
        self.client.passer_commande(commande)
        with self.assertLogs(level='INFO') as log:
            self.client.afficher_historique_commandes()
            self.assertIn('Commande ID: 101', log.output[0])

    def test_donner_avis(self):
        # Ajout d'un avis pour une commande
        commande = Commande(id_commande=101, date_commande="2023-11-01")
        self.client.passer_commande(commande)
        with self.assertLogs(level='INFO') as log:
            self.client.donner_avis(commande, "Très bon service")
            self.assertIn('Avis ajouté pour la commande 101: Très bon service', log.output[0])

    def test_obtenir_recommandations(self):
        # Test des recommandations basées sur les allergies
        menu = Menu(liste_plats=[
            Plat(nom="Pizza", ingredients=["farine", "tomate"]),
            Plat(nom="Salade", ingredients=["salade", "tomate", "noix"])
        ])
        recommandations = self.client.obtenir_recommandations(menu)
        self.assertIn(menu.liste_plats[0], recommandations)
        self.assertNotIn(menu.liste_plats[1], recommandations)

if __name__ == "__main__":
    unittest.main()
