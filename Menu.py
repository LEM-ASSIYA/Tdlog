class Menu:
    def __init__(self, id_menu, nom):
        self.id_menu = id_menu
        self.nom = nom
        self.liste_plats = []

    def ajouter_plat(self, plat):
        self.liste_plats.append(plat)
        print(f"Le plat {plat.nom} a été ajouté au menu {self.nom}.")

    def modifier_menu(self):
        print(f"Le menu {self.nom} a été modifié.")