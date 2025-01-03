import tkinter as tk
from tkinter import messagebox
from chef_interface import InterfaceChef
from client_interface import InterfaceClient
from gerant_interface import InterfaceGerant
from serveur_interface import InterfaceServeur


# Utilisateurs temporaires pour authentification
UTILISATEURS = {
    "chef": {"mot_de_passe": "chef123", "role": "chef"},
    "client": {"mot_de_passe": "client123", "role": "client"},
    "gerant": {"mot_de_passe": "gerant123", "role": "gerant"},
    "serveur":{"mot_de_passe": "serveur123", "role": "serveur"},
    "serveur1":{"mot_de_passe": "serveur123", "role": "serveur"},
    "serveur2":{"mot_de_passe": "serveur123", "role": "serveur"},
    "serveur3":{"mot_de_passe": "serveur123", "role": "serveur"},
}

class AuthentificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentification")
        self.root.geometry("400x300")
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
        self.btn_login.pack(pady=20)

    def authentifier(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in UTILISATEURS and UTILISATEURS[username]["mot_de_passe"] == password:
            role = UTILISATEURS[username]["role"]
            messagebox.showinfo("Connexion réussie", f"Bienvenue {username}, rôle : {role}.")
            self.ouvrir_interface_role(role)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def ouvrir_interface_role(self, role):
        self.root.destroy()
        if role == "chef":
            root = tk.Tk()
            app = InterfaceChef(root)
            root.mainloop()
        elif role == "client":
            root = tk.Tk()
            app = InterfaceClient(root)
            root.mainloop()
        elif role == "gerant":
            root = tk.Tk()
            app = InterfaceGerant(root)
            root.mainloop()
        elif role == "serveur":
            root = tk.Tk()
            app = InterfaceServeur(root)
            root.mainloop()    

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthentificationApp(root)
    root.mainloop()
