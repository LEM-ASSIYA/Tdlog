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


class Serveur(Utilisateur):
    def __init__(self, ids, nom, email, mot_de_passe):
        super().__init__(ids, nom, email, mot_de_passe)
        self.liste_tables_attribuees = []

    def prendre_commande(self):
        print(f"{self.nom} a pris une commande.")

    def servir_plat(self):
        print(f"{self.nom} sert un plat.")

    def assigner_table(self, table):
        self.liste_tables_attribuees.append(table)
        print(f"{self.nom} a assigné la table {table.num_table}.")