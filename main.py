

import tkinter as tk
from tkinter import messagebox
import json
import os
from chef_interface import InterfaceChef
from client_interface import InterfaceClient
from gerant_interface import InterfaceGerant
from serveur_interface import InterfaceServeur
from livreur_interface import InterfaceLivreur
from inventaire import Inventaire  # Import de la classe Inventaire



# ✅ Initialisation de la base de données JSON
DATABASE_FILE = 'database.json'
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'w') as db:
        json.dump({"utilisateurs": {}, "commandes": [], "notifications": [], "inventaire": {}}, db)

def lire_database():
    with open(DATABASE_FILE, 'r') as db:
        return json.load(db)

def ecrire_database(data):
    with open(DATABASE_FILE, 'w') as db:
        json.dump(data, db, indent=4)



# ✅ Interface d'Authentification
class AuthentificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentification")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Titre
        self.label_titre = tk.Label(root, text="Connexion", font=("Arial", 18, "bold"))
        self.label_titre.pack(pady=20)




        # Champ Nom d'utilisateur
        self.label_username = tk.Label(root, text="Nom d'utilisateur:")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        # Champ Mot de passe
        self.label_password = tk.Label(root, text="Mot de passe:")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)




       # Bouton Connexion
        self.btn_login = tk.Button(root, text="Se connecter", command=self.authentifier)
        self.btn_login.pack(pady=10)

        # Bouton Inscription
        self.btn_register = tk.Button(root, text="S'inscrire", command=self.inscrire)
        self.btn_register.pack(pady=10)



    def authentifier(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        data = lire_database()
        utilisateurs = data.get("utilisateurs", {})

        if username in utilisateurs and utilisateurs[username]["mot_de_passe"] == password:
            role = utilisateurs[username]["role"]
            messagebox.showinfo("Connexion réussie", f"Bienvenue {username}, rôle : {role}.")
            self.ouvrir_interface_role(role)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")








#     def ouvrir_interface_role(self, role):
#         if role == "chef":
#             top = tk.Toplevel(self.root)
#             app = InterfaceChef(top)
#         elif role == "client":
#             top = tk.Toplevel(self.root)
#             app = InterfaceClient(top)
#         elif role == "gerant":
#             top = tk.Toplevel(self.root)
#             app = InterfaceGerant(top)
#         elif role == "serveur":
#             top = tk.Toplevel(self.root)
#             app = InterfaceServeur(top)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AuthentificationApp(root)
#     root.mainloop()
