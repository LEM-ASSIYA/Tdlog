# import tkinter as tk
# from tkinter import messagebox

# class InterfaceChef:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tableau de Bord - Chef")
#         self.root.geometry("600x400")
        
#         tk.Label(root, text="Interface Chef", font=("Arial", 20, "bold")).pack(pady=20)
        
#         # Boutons des fonctionnalités
#         tk.Button(root, text="Consulter Commandes", command=self.consulter_commandes).pack(pady=10)
#         tk.Button(root, text="Valider Commande", command=self.valider_commande).pack(pady=10)
#         tk.Button(root, text="Notifier Serveur", command=self.notifier_serveur).pack(pady=10)
#         tk.Button(root, text="Se Déconnecter", command=root.quit).pack(pady=10)

#     def consulter_commandes(self):
#         messagebox.showinfo("Commandes", "Affichage des commandes.")

#     def valider_commande(self):
#         messagebox.showinfo("Validation", "Commande validée.")

#     def notifier_serveur(self):
#         messagebox.showinfo("Notification", "Le serveur est notifié.")


from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox

# ✅ Classe abstraite Utilisateur
class Utilisateur(ABC):
    def __init__(self, id, nom, email, mot_de_passe):
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.logged_in = False

    @abstractmethod
    def se_connecter(self, mot_de_passe):
        pass

    @abstractmethod
    def se_deconnecter(self):
        pass


# ✅ Classe Chef
class Chef(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe):
        super().__init__(id, nom, email, mot_de_passe)
        self.commandes = []

    def se_connecter(self, mot_de_passe):
        if self.mot_de_passe == mot_de_passe:
            self.logged_in = True
            print(f"{self.nom} s'est connecté avec succès.")
            return True
        else:
            print("Mot de passe incorrect.")
            return False

    def se_deconnecter(self):
        self.logged_in = False
        print(f"{self.nom} s'est déconnecté.")

    def consulter_commandes(self):
        if not self.commandes:
            return "Aucune commande pour l'instant."
        return "\n".join([f"Commande {c['id']} : {c['plat']} - Statut: {c['statut']}" for c in self.commandes])

    def valider_commande(self):
        print("Commande validée par le chef.")

    def notifier_serveur(self):
        print("Serveur notifié pour récupération de la commande.")


# ✅ Interface d'Authentification
class AuthentificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentification Chef")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Titre
        tk.Label(root, text="Connexion Chef", font=("Arial", 18, "bold")).pack(pady=20)

        # Champ Nom d'utilisateur
        tk.Label(root, text="Nom d'utilisateur:").pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        # Champ Mot de passe
        tk.Label(root, text="Mot de passe:").pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        # Bouton Connexion
        tk.Button(root, text="Se connecter", command=self.authentifier).pack(pady=20)

        self.label_status = tk.Label(root, text="", fg="red")
        self.label_status.pack()

        # Crée un objet Chef
        self.chef = Chef(1, "Chef Pierre", "chef@example.com", "chef123")

    def authentifier(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == self.chef.nom and self.chef.se_connecter(password):
            messagebox.showinfo("Succès", "Connexion réussie en tant que Chef.")
            self.root.destroy()  # Ferme la fenêtre actuelle
            self.ouvrir_interface_chef()
        else:
            self.label_status.config(text="Nom d'utilisateur ou mot de passe incorrect.")

    def ouvrir_interface_chef(self):
        tableau_de_bord = tk.Tk()
        app = InterfaceChef(tableau_de_bord, self.chef)
        tableau_de_bord.mainloop()


# ✅ Interface Chef après Authentification
class InterfaceChef:
    def __init__(self, root, chef):
        self.root = root
        self.root.title("Tableau de Bord - Chef")
        self.root.geometry("600x400")

        self.chef = chef

        tk.Label(root, text=f"Bienvenue {self.chef.nom}!", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Button(root, text="Consulter Commandes", command=self.consulter_commandes).pack(pady=10)
        tk.Button(root, text="Valider Commande", command=self.valider_commande).pack(pady=10)
        tk.Button(root, text="Notifier Serveur", command=self.notifier_serveur).pack(pady=10)
        tk.Button(root, text="Se Déconnecter", command=self.se_deconnecter).pack(pady=10)

    def consulter_commandes(self):
        commandes = self.chef.consulter_commandes()
        messagebox.showinfo("Commandes", commandes)

    def valider_commande(self):
        self.chef.valider_commande()
        messagebox.showinfo("Commande", "Commande validée.")

    def notifier_serveur(self):
        self.chef.notifier_serveur()
        messagebox.showinfo("Notification", "Serveur notifié avec succès.")

    def se_deconnecter(self):
        self.chef.se_deconnecter()
        self.root.destroy()
        root = tk.Tk()
        app = AuthentificationApp(root)
        root.mainloop()


#  Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = AuthentificationApp(root)
    root.mainloop()
