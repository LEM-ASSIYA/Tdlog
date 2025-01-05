# import tkinter as tk
# from tkinter import messagebox
# import json
# import os

# #  Initialisation de la base de données JSON
# DATABASE_FILE = 'database.json'
# if not os.path.exists(DATABASE_FILE):
#     with open(DATABASE_FILE, 'w') as db:
#         json.dump({"commandes": [], "notifications": []}, db)


# def lire_database():
#     with open(DATABASE_FILE, 'r') as db:
#         return json.load(db)


# def ecrire_database(data):
#     with open(DATABASE_FILE, 'w') as db:
#         json.dump(data, db, indent=4)


# #  Interface Serveur
# class InterfaceServeur:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Interface Serveur")
#         self.root.geometry("600x500")
        
#         # En-tête
#         tk.Label(self.root, text="Tableau de Bord - Serveur", font=("Arial", 20, "bold")).pack(pady=20)
        
#         # Zone de notification
#         self.frame_notifications = tk.Frame(self.root)
#         self.frame_notifications.pack(pady=10, fill='both', expand=True)
        
#         self.notifications_listbox = tk.Listbox(self.frame_notifications, height=15, width=70)
#         self.notifications_listbox.pack(pady=10)
        
#         tk.Button(self.root, text="Actualiser Notifications", command=self.load_notifications).pack(pady=5)
#         tk.Button(self.root, text="Effacer Notification", command=self.effacer_notification).pack(pady=5)
#         tk.Button(self.root, text="Se Déconnecter", command=self.se_deconnecter).pack(pady=10)
        
#         self.load_notifications()
    
#     def load_notifications(self):
#         self.notifications_listbox.delete(0, tk.END)
#         data = lire_database()
#         notifications = data.get("notifications", [])
        
#         # Filtrer uniquement les commandes sur place avec un numéro de table
#         for notification in notifications:
#             if notification.get("type_client") == "sur place" and notification.get("table"):
#                 self.notifications_listbox.insert(tk.END, f"{notification['message']} | Table: {notification['table']}")

    
#     def effacer_notification(self):
#         selection = self.notifications_listbox.curselection()
#         if not selection:
#             messagebox.showerror("Erreur", "Veuillez sélectionner une notification à effacer.")
#             return
        
#         index = selection[0]
#         data = lire_database()
#         data["notifications"].pop(index)
#         ecrire_database(data)
#         self.load_notifications()
#         messagebox.showinfo("Notification", "Notification effacée.")
    
#     def se_deconnecter(self):
#         self.root.destroy()
#         root = tk.Tk()
#         app = AuthentificationServeur(root)
#         root.mainloop()


# #  Interface d'Authentification Serveur
# class AuthentificationServeur:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Authentification Serveur")
#         self.root.geometry("400x300")
#         self.root.resizable(False, False)
        
#         tk.Label(root, text="Connexion Serveur", font=("Arial", 18, "bold")).pack(pady=20)
#         tk.Button(root, text="Se connecter", command=self.authentifier).pack(pady=20)
    
#     def authentifier(self):
#         self.root.destroy()
#         tableau_de_bord = tk.Tk()
#         app = InterfaceServeur(tableau_de_bord)
#         tableau_de_bord.mainloop()


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = AuthentificationServeur(root)
#     root.mainloop()



import tkinter as tk
from tkinter import messagebox
import json
import os

# ✅ Initialisation de la base de données JSON
DATABASE_FILE = 'database.json'
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'w') as db:
        json.dump({"commandes": [], "notifications": []}, db)


def lire_database():
    with open(DATABASE_FILE, 'r') as db:
        return json.load(db)


def ecrire_database(data):
    with open(DATABASE_FILE, 'w') as db:
        json.dump(data, db, indent=4)


# ✅ Interface Serveur
class InterfaceServeur:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Serveur")
        self.root.geometry("600x500")
        
        # ✅ En-tête
        tk.Label(self.root, text="Tableau de Bord - Serveur", font=("Arial", 20, "bold")).pack(pady=20)
        
        # ✅ Zone de notification
        self.frame_notifications = tk.Frame(self.root)
        self.frame_notifications.pack(pady=10, fill='both', expand=True)
        
        self.notifications_listbox = tk.Listbox(self.frame_notifications, height=15, width=70)
        self.notifications_listbox.pack(pady=10)
        
        tk.Button(self.root, text="Actualiser Notifications", command=self.load_notifications).pack(pady=5)
        tk.Button(self.root, text="Effacer Notification", command=self.effacer_notification).pack(pady=5)
        tk.Button(self.root, text="Se Déconnecter", command=self.se_deconnecter).pack(pady=10)
        
        # ✅ Liste pour stocker les indices réels des notifications
        self.notification_indices = []
        
        self.load_notifications()
    
    def load_notifications(self):
        """Charger uniquement les commandes prêtes avec type_client='sur place'."""
        self.notifications_listbox.delete(0, tk.END)
        self.notification_indices = []  # Réinitialiser les indices
        data = lire_database()
        notifications = data.get("notifications", [])
        
        for i, notification in enumerate(notifications):
            if notification.get("type_client") == "sur place" and notification.get("table") and notification.get("message"):
                self.notifications_listbox.insert(
                    tk.END, 
                    f"{notification['message']} | Table: {notification['table']}"
                )
                # Ajouter l'index réel de la notification
                self.notification_indices.append(i)

    def effacer_notification(self):
        """Effacer une notification sélectionnée."""
        selection = self.notifications_listbox.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner une notification à effacer.")
            return
        
        listbox_index = selection[0]
        database_index = self.notification_indices[listbox_index]
        
        data = lire_database()
        
        if 0 <= database_index < len(data["notifications"]):
            data["notifications"].pop(database_index)
            ecrire_database(data)
            self.load_notifications()
            messagebox.showinfo("Notification", "Notification effacée.")
        else:
            messagebox.showerror("Erreur", "Impossible de trouver la notification sélectionnée dans la base de données.")
    
    def se_deconnecter(self):
        """Se déconnecter et retourner à l'écran d'authentification."""
        self.root.destroy()
        from main import AuthentificationApp  # Éviter l'importation circulaire
        root = tk.Tk()
        app = AuthentificationApp(root)
        root.mainloop()


# ✅ Interface d'Authentification Serveur
class AuthentificationServeur:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentification Serveur")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        tk.Label(root, text="Connexion Serveur", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Button(root, text="Se connecter", command=self.authentifier).pack(pady=20)
    
    def authentifier(self):
        """Authentifier l'utilisateur et ouvrir l'interface Serveur."""
        self.root.destroy()
        tableau_de_bord = tk.Tk()
        app = InterfaceServeur(tableau_de_bord)
        tableau_de_bord.mainloop()


# ✅ Lancer l'application
if __name__ == '__main__':
    root = tk.Tk()
    app = AuthentificationServeur(root)
    root.mainloop()

