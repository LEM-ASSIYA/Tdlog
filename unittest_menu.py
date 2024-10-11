import unittest
import Menu
import Plat
class TestMenu(unittest.TestCase):
    
    def test_initialisation(self):
        # Test de l'initialisation d'un menu
        menu = Menu(1, "Menu du soir")
        
        self.assertEqual(menu.id_menu, 1)
        self.assertEqual(menu.nom, "Menu du soir")
        self.assertEqual(len(menu.liste_plats), 0)

    def test_ajouter_plat(self):
        # Test de l'ajout d'un plat au menu
        menu = Menu(1, "Menu du soir")
        plat = Plat(1, "Pizza", 12.5, 20)
        
        menu.ajouter_plat(plat)
        
        self.assertIn(plat, menu.liste_plats)
        self.assertEqual(len(menu.liste_plats), 1)
        self.assertEqual(menu.liste_plats[0].nom, "Pizza")

    def test_modifier_menu(self):
        # Test de la modification du menu
        menu = Menu(1, "Menu du midi")
        
        with self.assertLogs(level='INFO') as log:
            menu.modifier_menu()
            self.assertIn("Le menu Menu du midi a été modifié.", log.output[0])

