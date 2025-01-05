import json
import osc

class Inventaire:
    def __init__(self, idInventaire=None, listeIngrédients=None, quantitéIngrédient=None, database_file='database.json'):
        self.database_file = database_file
        self.stock = {}


        if idInventaire is not None and listeIngrédients is not None and quantitéIngrédient is not None:
            # Si les ingrédients et quantités sont fournis, initialisez l'inventaire
            if len(listeIngrédients) != len(quantitéIngrédient):
                raise ValueError("La longueur de 'listeIngrédients' doit correspondre à celle de 'quantitésIngrédients'.")
            self.stock = dict(zip(listeIngrédients, quantitéIngrédient))
            self.sauvegarder_inventaire()  # Sauvegarder l'inventaire dans le fichier JSON
        else:
            self.stock = self.charger_inventaire()  # Charger l'inventaire depuis le fichier JSON




    def charger_inventaire(self):
        """Charger l'inventaire depuis la base de données JSON"""
        if not os.path.exists(self.database_file):
            raise FileNotFoundError(f"Le fichier {self.database_file} n'a pas été trouvé.")
        
        with open(self.database_file, 'r') as db:
            data = json.load(db)
            return data.get("inventaire", {})
        

    def sauvegarder_inventaire(self):
        """Sauvegarder l'inventaire mis à jour dans la base de données JSON"""
        with open(self.database_file, 'r') as db:
            data = json.load(db)
        
        data["inventaire"] = self.stock
        
        with open(self.database_file, 'w') as db:
            json.dump(data, db, indent=4)

    def mettre_à_jour_stock(self, ingrédient, quantité):
        """Mettre à jour la quantité d'un ingrédient dans l'inventaire"""
        if quantité < 0:
            raise ValueError(f"Erreur : la quantité pour {ingrédient} doit être positive.")
        
        if ingrédient in self.stock:
            self.stock[ingrédient] = quantité
        else:
            self.stock[ingrédient] = quantité




        self.sauvegarder_inventaire()  # Sauvegarder après modification
        return f"Stock de {ingrédient} mis à jour à {quantité}."
    
    def consulter_stock(self, ingrédient):
        """Consulter le stock d'un ingrédient"""
        if ingrédient not in self.stock:
            raise KeyError(f"Erreur : {ingrédient} n'est pas dans la liste des ingrédients.")
        
        return f"Stock de {ingrédient} : {self.stock[ingrédient]}"



