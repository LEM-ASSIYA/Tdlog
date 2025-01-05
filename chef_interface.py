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
from Plat import Plat
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

import tkinter as tk
from tkinter import messagebox
from utilisateur import Utilisateur
#  Interface d'Authentification
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
        tk.Button(root, text="Ajouter Plat", command=self.ajouter_plat).pack(pady=5)
        tk.Button(root, text="Modifier Plat", command=self.modifier_plat).pack(pady=5)
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
        
    def ajouter_plat(self):
        # Create new window for adding plat
        plat_window = tk.Toplevel(self.root)
        plat_window.title("Ajouter Plat")
        plat_window.geometry("400x300")

        tk.Label(plat_window, text="ID Plat:").pack()
        id_entry = tk.Entry(plat_window)
        id_entry.pack()

        tk.Label(plat_window, text="Nom:").pack()
        nom_entry = tk.Entry(plat_window)
        nom_entry.pack()

        tk.Label(plat_window, text="Prix:").pack()
        prix_entry = tk.Entry(plat_window)
        prix_entry.pack()

        tk.Label(plat_window, text="Temps de préparation:").pack()
        temps_entry = tk.Entry(plat_window)
        temps_entry.pack()

        def save_plat():
            nouveau_plat = Plat(
                id_entry.get(),
                nom_entry.get(),
                float(prix_entry.get()),
                int(temps_entry.get())
            )
            messagebox.showinfo("Succès", f"Plat {nouveau_plat.nom} ajouté avec succès!")
            plat_window.destroy()

        tk.Button(plat_window, text="Sauvegarder", command=save_plat).pack(pady=20)

    def modifier_plat(self):
        # Create a new window for modifying the dish
        modifier_window = tk.Toplevel(self.root)
        modifier_window.title("Modifier Plat")
        modifier_window.geometry("400x300")

        # Labels and entry fields for the dish details
        tk.Label(modifier_window, text="ID du Plat:").pack(pady=5)
        id_entry = tk.Entry(modifier_window)
        id_entry.pack(pady=5)

        tk.Label(modifier_window, text="Nom du Plat:").pack(pady=5)
        nom_entry = tk.Entry(modifier_window)
        nom_entry.pack(pady=5)

        tk.Label(modifier_window, text="Prix du Plat:").pack(pady=5)
        prix_entry = tk.Entry(modifier_window)
        prix_entry.pack(pady=5)

        tk.Label(modifier_window, text="Temps de Préparation:").pack(pady=5)
        temps_entry = tk.Entry(modifier_window)
        temps_entry.pack(pady=5)

        def save_modifications():
            # Logic to update the dish details
            plat_id = id_entry.get()
            nouveau_nom = nom_entry.get()
            nouveau_prix = float(prix_entry.get())
            nouveau_temps = int(temps_entry.get())

            # Assuming you have a list of plats, update the corresponding plat
            for plat in self.plats:
                if plat.id == plat_id:
                    plat.nom = nouveau_nom
                    plat.prix = nouveau_prix
                    plat.temps_preparation = nouveau_temps
                    messagebox.showinfo("Succès", f"Plat {plat.nom} modifié avec succès!")
                    break
            else:
                messagebox.showerror("Erreur", "Plat non trouvé")

            modifier_window.destroy()

        # Button to save the modifications
        tk.Button(modifier_window, text="Sauvegarder", command=save_modifications).pack(pady=20)

#  Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = AuthentificationApp(root)
    root.mainloop()
