import tkinter as tk
from tkinter import messagebox
from Table import Table
from tkinter import simpledialog
import random  # Pour générer des capacités aléatoires


class InterfaceServeur:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau de Bord - Serveur")
        self.root.geometry("600x400")

        # Création des tables avec des capacités aléatoires entre 1 et 4
        self.tables = [Table(i, random.randint(1, 4)) for i in range(1, 11)]  # 10 tables avec des capacités aléatoires entre 1 et 4

        tk.Label(root, text="Interface Serveur", font=("Arial", 20, "bold")).pack(pady=20)

        # Boutons des fonctionnalités
        tk.Button(root, text="Prendre commande", command=self.prendre_commande).pack(pady=10)
        tk.Button(root, text="Servir plat", command=self.servir_plat).pack(pady=10)
        tk.Button(root, text="Assigner table", command=self.assigner_table).pack(pady=10)
        tk.Button(root, text="Libérer table", command=self.liberer_table).pack(pady=10)
        tk.Button(root, text="Se Déconnecter", command=root.quit).pack(pady=10)

    def prendre_commande(self):
        root = tk.Tk()
        root.withdraw()  # Masquer la fenêtre principale

        # Demander le numéro de table
        num_table = simpledialog.askinteger("Commande", "Entrez le numéro de la table :")
        if num_table:
            print(f"Commande prise pour la table {num_table}.")
            messagebox.showinfo("Commande", f"Commande prise pour la table {num_table}.")
        else:
            print("Aucune table sélectionnée.")

    def servir_plat(self):
        messagebox.showinfo("Plat", "Plat servi.")

    def assigner_table(self):
        # Récupère les tables libres
        tables_libres = [table for table in self.tables if not table.occupee]
        if not tables_libres:
            messagebox.showinfo("Table", "Toutes les tables sont occupées.")
            return

        # Création d'une nouvelle fenêtre pour afficher les tables libres avec leur capacité
        fenetre_libre = tk.Toplevel(self.root)
        fenetre_libre.title("Tables Libres")
        fenetre_libre.geometry("300x250")

        # Liste les tables libres avec leur capacité
        for table in tables_libres:
            button = tk.Button(fenetre_libre, text=f"Table {table.id_table} (Capacité: {table.capacite})", 
                               command=lambda t=table: self.confirmer_assignation(t))
            button.pack(pady=5)

    def confirmer_assignation(self, table):
        confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous assigner la table {table.id_table} (Capacité: {table.capacite}) ?")
        if confirmation:
            table.assigner_table()
            messagebox.showinfo("Table", f"Table {table.id_table} assignée avec succès.")
        else:
            messagebox.showinfo("Annulation", "Assignation annulée.")

    def liberer_table(self):
        table_id = self.demander_table()
        if table_id is not None:
            confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous libérer la table {table_id} ?")
            if confirmation:
                table = self.tables[table_id - 1]
                if table.occupee:
                    table.liberer_table()
                    messagebox.showinfo("Table", f"Table {table_id} libérée avec succès.")
                else:
                    messagebox.showwarning("Erreur", f"La table {table_id} est déjà libre.")

    def demander_table(self):
        try:
            table_id = int(simpledialog.askstring("Table", "Entrez le numéro de la table (1-10):"))
            if 1 <= table_id <= 10:
                return table_id
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un numéro de table valide (1-10).")
        except (ValueError, TypeError):
            messagebox.showerror("Erreur", "Entrée invalide.")
        return None
