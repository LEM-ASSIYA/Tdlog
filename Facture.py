class Facture:

    def __init__(self, idFacture, dateFacture, montantTotal, modePaiement):
        self.idFacture = idFacture
        self.dateFacture = dateFacture
        self.montantTotal = montantTotal
        self.modePaiement = modePaiement
        self.modesPaiementValides = ["carte", "espèces", "chèque"]
        self.estPayée = False

    def genererFacture(self):
        return f"Facture {self.idFacture} générée le {self.dateFacture} pour un montant de {self.montantTotal}."
    
    def appliquerRéduction(self, réduction):
        if réduction >= self.montantTotal:
            raise ValueError(f"Erreur : la réduction de {réduction} dépasse ou est égale au montant total de la facture.")
        self.montantTotal -= réduction
        return f"Réduction de {réduction} appliquée. Nouveau montant : {self.montantTotal}."
    
    def payerFacture(self, paiement):
        if paiement in self.modesPaiementValides:
            raise ValueError(f"Erreur : le mode de paiement '{paiement}' n'est pas valide. Choisissez un mode parmi {self.modesPaiementValides}.")
        self.estPayée = True
        return f"Facture payée via {self.modePaiement}. Montant total : {self.montantTotal}."
    
    def étatPaiement(self):
        if self.estPayée:
            return "La facture a été payée."
        else:
            return "La facture n'a pas encore été payée."