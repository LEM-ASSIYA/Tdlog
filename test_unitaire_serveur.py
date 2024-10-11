import unittest
import Serveur, Table


class TestServeur(unittest.TestCase):
    def setUp(self):
        self.serveur = Serveur(2, "Bob", "bob@example.com", "motdepasse", 101)

    def test_prendre_commande(self):
        self.serveur.prendre_commande() 

    def test_servir_plat(self):
        self.serveur.servir_plat()  

    def test_assigner_table(self):
        table = Table(1, 5, 4)
        self.serveur.assigner_table(table) 
        self.assertIn(table, self.serveur.liste_tables_attribuees)  
        
if __name__ == '__main__':
    unittest.main()