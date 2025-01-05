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