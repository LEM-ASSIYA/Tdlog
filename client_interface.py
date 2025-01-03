import tkinter as tk
from tkinter import messagebox

class InterfaceClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau de Bord - Client")
        self.root.geometry("600x400")
        
        tk.Label(root, text="Interface Client", font=("Arial", 20, "bold")).pack(pady=20)
        
        # Boutons des fonctionnalités
        tk.Button(root, text="Passer Commande", command=self.passer_commande).pack(pady=10)
        tk.Button(root, text="Payer Facture", command=self.payer_facture).pack(pady=10)
        tk.Button(root, text="Faire Réservation", command=self.faire_reservation).pack(pady=10)
        tk.Button(root, text="Se Déconnecter", command=root.quit).pack(pady=10)

    def passer_commande(self):
        messagebox.showinfo("Commande", "Commande passée avec succès.")

    def payer_facture(self):
        messagebox.showinfo("Paiement", "Facture payée.")

    def faire_reservation(self):
        messagebox.showinfo("Réservation", "Réservation effectuée.")
