import unittest
import Plat
from commande import Commande


class TestCommande(unittest.TestCase):

    def setUp(self):
        self.commande = Commande(id_commande=1, date_commande="2023-11-01")
        self.plat1 = Plat(nom="Pizza", prix=12.5)
        self.plat2 = Plat(nom="Pâtes", prix=15.0)

    def test_initialisation_commande(self):
        self.assertEqual(self.commande.id_commande, 1)
        self.assertEqual(self.commande.date_commande, "2023-11-01")
        self.assertEqual(self.commande.status_commande, "En attente")
        self.assertEqual(len(self.commande.plats), 0)

    def test_ajouter_plat(self):
        self.commande.ajouter_plat(self.plat1)
        self.assertIn(self.plat1, self.commande.plats)
        self.assertEqual(len(self.commande.plats), 1)

    def test_calculer_total(self):
        self.commande.ajouter_plat(self.plat1)
        self.commande.ajouter_plat(self.plat2)
        total = self.commande.calculer_total()
        self.assertEqual(total, 27.5)

    def test_changer_status(self):
        self.commande.changer_status("En cours de préparation")
        self.assertEqual(self.commande.status_commande, "En cours de préparation")
        self.commande.changer_status("Livrée")
        self.assertEqual(self.commande.status_commande, "Livrée")


if __name__ == "__main__":
    unittest.main(exit=False)