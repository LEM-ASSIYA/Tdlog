import tkinter as tk
from tkinter import messagebox
import json
import os

# ✅ Lecture et écriture de la base de données
DATABASE_FILE = 'database.json'
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'w') as db:
        json.dump({"commandes": [], "notifications": [], "utilisateurs": {}}, db)


def lire_database():
    with open(DATABASE_FILE, 'r') as db:
        return json.load(db)


def ecrire_database(data):
    with open(DATABASE_FILE, 'w') as db:
        json.dump(data, db, indent=4)


# ✅ Interface Livreur
class InterfaceLivreur:
    def __init__(self, root, livreur_nom):
        self.root = root
        self.root.title("Interface Livreur")
        self.root.geometry("600x500")
        self.livreur_nom = livreur_nom  # Enregistrer le nom du livreur
        
        # ✅ En-tête
        tk.Label(self.root, text=f"Tableau de Bord - Livreur ({self.livreur_nom})", font=("Arial", 20, "bold")).pack(pady=20)
        
        # ✅ Liste des commandes
        self.frame_commandes = tk.Frame(self.root)
        self.frame_commandes.pack(pady=10, fill='both', expand=True)
        
        self.commandes_listbox = tk.Listbox(self.frame_commandes, height=15, width=70)
        self.commandes_listbox.pack(pady=10)
        
        tk.Button(self.root, text="Actualiser Commandes", command=self.load_commandes).pack(pady=5)
        tk.Button(self.root, text="Marquer comme Livrée", command=self.marquer_livree).pack(pady=5)
        tk.Button(self.root, text="Se Déconnecter", command=self.se_deconnecter).pack(pady=10)
        
        self.load_commandes()
    
    def load_commandes(self):
        """Charger uniquement les commandes prêtes avec type_client='à emporter'."""
        self.commandes_listbox.delete(0, tk.END)
        data = lire_database()
        commandes = data.get("commandes", [])
        
        for commande in commandes:
            if commande.get("statut") == "Prête" and commande.get("type_client") == "à emporter":
                self.commandes_listbox.insert(
                    tk.END,
                    f"ID: {commande['id']} | Plats: {', '.join(commande['plats'])} | Adresse: {commande.get('adresse', 'Non spécifiée')}"
                )

    def marquer_livree(self):
        """Marquer une commande comme livrée."""
        selection = self.commandes_listbox.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner une commande à marquer comme livrée.")
            return
        
        index = selection[0]
        data = lire_database()
        commandes = data.get("commandes", [])
        
        commande = commandes[index]
        commande["statut"] = "Livrée"
        ecrire_database(data)
        
        self.load_commandes()
        messagebox.showinfo("Livraison", "Commande marquée comme livrée.")
    
    def se_deconnecter(self):
        """Se déconnecter et retourner à l'écran d'authentification."""
        self.root.destroy()
        from main import AuthentificationApp
        root = tk.Tk()
        app = AuthentificationApp(root)
        root.mainloop()


# ✅ Test Interface Livreur
if __name__ == '__main__':
    root = tk.Tk()
    app = InterfaceLivreur(root, livreur_nom="Livreur123")
    root.mainloop()