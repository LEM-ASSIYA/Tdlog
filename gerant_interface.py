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
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau de Bord - Gérant")
        self.root.geometry("600x400")
        
        tk.Label(root, text="Interface Gérant", font=("Arial", 20, "bold")).pack(pady=20)
        
        # Boutons des fonctionnalités
        tk.Button(root, text="Gérer Employés", command=self.gerer_employes).pack(pady=10)
        tk.Button(root, text="Consulter Rapports", command=self.consulter_rapports).pack(pady=10)
        tk.Button(root, text="Se Déconnecter", command=root.quit).pack(pady=10)




    def gerer_employes(self):
        messagebox.showinfo("Gestion Employés", "Employés gérés avec succès.")

    def consulter_rapports(self):
        messagebox.showinfo("Rapports", "Affichage des rapports.")
