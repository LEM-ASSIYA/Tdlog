class Inventaire :

    def __init__(self, idInventaire, listeIngrédients, quantitéIngrédient):
        self.idInventaire = idInventaire
        self.listeIngrédients = listeIngrédients
        self.quantitéIngrédient = quantitéIngrédient

    def mettreÀJourStock(self, Ingrédient, quantité):
        if quantité < 0:
            raise ValueError(f"Erreur : la quantité pour {Ingrédient} doit être positive.")
        if Ingrédient in self.listeIngrédients:
            self.quantitéIngrédient[Ingrédient] = quantité
        else:
            self.listeIngrédients.append(Ingrédient)
            self.quantitéIngrédient[Ingrédient] = 0  
            self.quantitéIngrédient[Ingrédient] = quantité
        return f"Stock de {Ingrédient} mis à jour à {quantité}."
    
    def consulterStock(self, ingrédient):
        if ingrédient not in self.listeIngrédients:
            raise KeyError(f"Erreur : {ingrédient} n'est pas dans la liste des ingrédients.")
        if self.quantitéIngrédient[ingrédient] < 0:
            raise ValueError(f"Erreur : la quantité de {ingrédient} est invalide.")
        else:
            return f"Stock de {ingrédient} : {self.quantitéIngrédient[ingrédient]}"