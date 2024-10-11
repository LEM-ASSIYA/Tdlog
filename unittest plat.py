import unittest

class TestPlat(unittest.TestCase):
    
    def test_initialisation(self):
        # Test de l'initialisation d'un plat
        plat = plat(1, "Pizza", 12.5, 20)
        
        self.assertEqual(plat.id_plat, 1)
        self.assertEqual(plat.nom, "Pizza")
        self.assertEqual(plat.prix, 12.5)
        self.assertEqual(plat.temps_preparation, 20)

    def test_attributs_types(self):
        # Test des types des attributs
        plat = plat(1, "Pizza", 12.5, 20)
        
        self.assertIsInstance(plat.id_plat, int)
        self.assertIsInstance(plat.nom, str)
        self.assertIsInstance(plat.prix, float)
        self.assertIsInstance(plat.temps_preparation, int)

