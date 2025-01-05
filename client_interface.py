
import tkinter as tk
from tkinter import messagebox

class InterfaceClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Client")
        self.root.geometry("600x500")
        
        # Page principale
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill="both", expand=True)

        tk.Label(self.frame_principal, text="Tableau de Bord - Client", font=("Arial", 20, "bold")).pack(pady=20)
        
        tk.Button(self.frame_principal, text="Passer commande", command=self.page_allergies).pack(pady=10)
        tk.Button(self.frame_principal, text="Payer Facture", command=self.payer_facture).pack(pady=10)
        tk.Button(self.frame_principal, text="Donner un avis", command=self.donner_avis).pack(pady=10)
        tk.Button(self.frame_principal, text="Afficher l'historique", command=self.afficher_historique).pack(pady=10)
        tk.Button(self.frame_principal, text="Obtenir des recommandations", command=self.afficher_recommandations).pack(pady=10)
        tk.Button(self.frame_principal, text="Se Déconnecter", command=root.quit).pack(pady=10)
        
        self.historique_commandes = []
        self.total = 0
        self.selection = []
        self.allergies = ""
    
    def page_allergies(self):
        self.frame_allergies = tk.Toplevel(self.root)
        self.frame_allergies.title("Informations sur les allergies")
        
        tk.Label(self.frame_allergies, text="Avez-vous des allergies ? (Laissez vide si non)").pack(pady=5)
        self.entry_allergies = tk.Entry(self.frame_allergies)
        self.entry_allergies.pack(pady=5)
        
        tk.Button(self.frame_allergies, text="Suivant", command=self.page_commande).pack(pady=10)
    
    def page_commande(self):
        self.allergies = self.entry_allergies.get()
        self.frame_allergies.destroy()
        
        self.frame_commande = tk.Toplevel(self.root)
        self.frame_commande.title("Passer commande")
        
        tk.Label(self.frame_commande, text="Sélectionnez vos plats").pack(pady=5)
        
        self.plats = [
            {"nom": "Pizza", "prix": 10},
            {"nom": "Salade", "prix": 5},
            {"nom": "Pâtes", "prix": 8}
        ]
        
        self.selection = []
        self.total = 0
        
        for plat in self.plats:
            var = tk.IntVar()
            chk = tk.Checkbutton(
                self.frame_commande,
                text=f"{plat['nom']} - {plat['prix']}€",
                variable=var,
                command=lambda p=plat, v=var: self.ajouter_au_total(p, v)
            )
            chk.pack(anchor="w")
        
        self.label_total = tk.Label(self.frame_commande, text=f"Total : {self.total}€")
        self.label_total.pack(pady=10)
        
        tk.Button(self.frame_commande, text="Confirmer la commande", command=self.confirmer_commande).pack(pady=10)
    
    def ajouter_au_total(self, plat, var):
        if var.get():
            self.total += plat["prix"]
            self.selection.append(plat["nom"])
        else:
            self.total -= plat["prix"]
            self.selection.remove(plat["nom"])
        self.label_total.config(text=f"Total : {self.total}€")
    
    def confirmer_commande(self):
        self.historique_commandes.append({"plats": self.selection, "total": self.total, "allergies": self.allergies})
        messagebox.showinfo("Commande", f"Commande confirmée. Total : {self.total}€\nAllergies : {self.allergies}")
        self.frame_commande.destroy()
    
    def payer_facture(self):
        paiement_fenetre = tk.Toplevel(self.root)
        paiement_fenetre.title("Payer Facture")
        
        tk.Label(paiement_fenetre, text=f"Montant total : {self.total}€").pack(pady=10)
        
        tk.Button(paiement_fenetre, text="Payer par Carte", command=self.payer_par_carte).pack(pady=5)
        tk.Button(paiement_fenetre, text="Payer en Espèces", command=lambda: self.finaliser_paiement(paiement_fenetre)).pack(pady=5)
    
    def payer_par_carte(self):
        carte_fenetre = tk.Toplevel(self.root)
        carte_fenetre.title("Paiement par Carte")
        
        tk.Label(carte_fenetre, text="Numéro de carte :").pack(pady=5)
        tk.Entry(carte_fenetre).pack(pady=5)
        
        tk.Label(carte_fenetre, text="Date d'expiration :").pack(pady=5)
        tk.Entry(carte_fenetre).pack(pady=5)
        
        tk.Label(carte_fenetre, text="CVV :").pack(pady=5)
        tk.Entry(carte_fenetre, show='*').pack(pady=5)
        
        tk.Button(carte_fenetre, text="Valider Paiement", command=lambda: self.finaliser_paiement(carte_fenetre)).pack(pady=10)
    
    def finaliser_paiement(self, fenetre):
        messagebox.showinfo("Paiement", "Paiement effectué avec succès!")
        fenetre.destroy()

    def afficher_historique(self):
        historique_fenetre = tk.Toplevel(self.root)
        historique_fenetre.title("Historique des commandes")
        for commande in self.historique_commandes:
            tk.Label(historique_fenetre, text=f"Plats: {', '.join(commande['plats'])}, Total: {commande['total']}€").pack()
    
    def donner_avis(self):
        avis_fenetre = tk.Toplevel(self.root)
        avis_fenetre.title("Donner un avis")
        tk.Entry(avis_fenetre).pack(pady=5)
        tk.Button(avis_fenetre, text="Envoyer", command=lambda: messagebox.showinfo("Avis", "Avis soumis!"))
    
    def afficher_recommandations(self):
        recommandations_fenetre = tk.Toplevel(self.root)
        recommandations_fenetre.title("Recommandations")
        tk.Label(recommandations_fenetre, text="Plats recommandés : Salade, Pâtes").pack(pady=10)
    

if __name__ == '__main__':
    root = tk.Tk()
    app = InterfaceClient(root)
    root.mainloop()



