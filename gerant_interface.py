import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from Inventaire import Inventaire

# Fichier JSON pour stocker les données
DATABASE_FILE = 'database.json'
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'w') as db:
        json.dump({"commandes": [], "notifications": [], "inventaire": {}}, db)

def lire_database():
    with open(DATABASE_FILE, 'r') as db:
        return json.load(db)

def ecrire_database(data):
    with open(DATABASE_FILE, 'w') as db:
        json.dump(data, db, indent=4)

class InterfaceGerant:
    def __init__(self, root, inventaire):
        self.root = root
        self.inventaire = inventaire
        self.root.title("Tableau de Bord - Gérant")
        self.root.geometry("800x600")
        
        tk.Label(root, text="Interface Gérant", font=("Arial", 20, "bold")).pack(pady=20)
        
        # Boutons des fonctionnalités
        tk.Button(root, text="Gérer Inventaire", command=self.gerer_employes).pack(pady=10)
        tk.Button(root, text="Consulter Stock", command=self.consulter_rapports).pack(pady=10)
        tk.Button(root, text="Se Déconnecter", command=root.quit).pack(pady=10)

    def consulter_stock(self):
        """Afficher le stock actuel dans un tableau."""
        fenetre_consultation = tk.Toplevel(self.root)
        fenetre_consultation.title("Consultation de l'Inventaire")
        fenetre_consultation.geometry("600x400")

        # Tableau pour afficher le stock
        tree = ttk.Treeview(fenetre_consultation, columns=("Ingrédient", "Quantité"), show="headings")
        tree.heading("Ingrédient", text="Ingrédient")
        tree.heading("Quantité", text="Quantité")
        tree.pack(fill="both", expand=True)

        # Recharger les données actualisées de l'inventaire depuis le fichier JSON
        data = lire_database()
        inventaire_data = data.get("inventaire", {})
        for ingrédient, quantité in inventaire_data.items():
            tree.insert("", "end", values=(ingrédient, quantité))


    def gerer_inventaire(self):
        """Permet au gérant de modifier l'inventaire."""
        fenetre_inventaire = tk.Toplevel(self.root)
        fenetre_inventaire.title("Gestion de l'Inventaire")
        fenetre_inventaire.geometry("600x400")

        # Tableau pour afficher le stock
        tree = ttk.Treeview(fenetre_inventaire, columns=("Ingrédient", "Quantité"), show="headings")
        tree.heading("Ingrédient", text="Ingrédient")
        tree.heading("Quantité", text="Quantité")
        tree.pack(fill="both", expand=True)

        # Recharger les données actualisées de l'inventaire depuis le fichier JSON
        data = lire_database()
        inventaire_data = data.get("inventaire", {})
        for ingrédient, quantité in inventaire_data.items():
            tree.insert("", "end", values=(ingrédient, quantité))

        # Entrées pour mise à jour
        tk.Label(fenetre_inventaire, text="Ingrédient:").pack(pady=5)
        ingredient_entry = tk.Entry(fenetre_inventaire)
        ingredient_entry.pack(pady=5)

        tk.Label(fenetre_inventaire, text="Nouvelle Quantité:").pack(pady=5)
        quantity_entry = tk.Entry(fenetre_inventaire)
        quantity_entry.pack(pady=5)

        def mettre_a_jour_stock():
            """Met à jour l'inventaire et actualise l'affichage."""
            ingrédient = ingredient_entry.get()
            try:
                quantité = int(quantity_entry.get())
                message = self.inventaire.mettre_à_jour_stock(ingrédient, quantité)

                # Sauvegarder dans JSON après modification
                data = lire_database()
                data["inventaire"] = self.inventaire.stock
                ecrire_database(data)

                # Recharger les données actualisées de l'inventaire depuis le fichier JSON
                data = lire_database()
                inventaire_data = data.get("inventaire", {})

                # Mettre à jour l'affichage du tableau
                for item in tree.get_children():
                    tree.delete(item)
                for ingrédient, quantité in inventaire_data.items():
                    tree.insert("", "end", values=(ingrédient, quantité))

                messagebox.showinfo("Succès", message)
            except ValueError as e:
                messagebox.showerror("Erreur", str(e))

        tk.Button(fenetre_inventaire, text="Mettre à jour", command=mettre_a_jour_stock).pack(pady=10)

    def consulter_rapports(self):
        messagebox.showinfo("Rapports", "Affichage des rapports.")
