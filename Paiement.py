class Paiement:
    def _init_(self, id_paiement, mode_paiement, montant):
        self.id_paiement = id_paiement
        self.mode_paiement = mode_paiement
        self.montant = montant

    def effectuer_paiement(self):
        print(f"Paiement de {self.montant} effectué par {self.mode_paiement}.")

    def rembourser_paiement(self):
        print(f"Le paiement de {self.montant} a été remboursé.")