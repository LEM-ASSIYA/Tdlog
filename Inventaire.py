class Inventaire :

    def __init__(self, idInventaire, listeIngrédients, quantitéIngrédient):
        if len(listeIngrédients) != len(quantitéIngrédient):
            raise ValueError("La longueur de 'listeIngrédients' doit correspondre à celle de 'quantitésIngrédients'.")
        self.idInventaire = idInventaire
        self.stock = dict(zip(listeIngrédients, quantitéIngrédient))

    def mettreÀJourStock(self, Ingrédient, quantité):
        if quantité < 0:
            raise ValueError(f"Erreur : la quantité pour {Ingrédient} doit être positive.")
        if Ingrédient in self.stock:
            self.stock[Ingrédient] = quantité
        else:
            self.stock[Ingrédient] = quantité  

        return f"Stock de {Ingrédient} mis à jour à {quantité}."
    
    def consulterStock(self, ingrédient):
        if ingrédient not in self.stock:
            raise KeyError(f"Erreur : {ingrédient} n'est pas dans la liste des ingrédients.")
        if self.stock[ingrédient] < 0:
            raise ValueError(f"Erreur : la quantité de {ingrédient} est invalide.")
        else:
            return f"Stock de {ingrédient} : {self.stock[ingrédient]}"

invent = Inventaire([1, 2, 3], ["Tomates", "Fromage", "Viande"], [15, 5, 10])
print(invent.mettreÀJourStock("Viande", 20)) 
print(invent.consulterStock("Fromage"))