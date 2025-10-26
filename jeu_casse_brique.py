# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
Caractéristiques de notre jeu: Skins de balle, angle de rebond de la balle sur la planche, niveaux de difficultés.
"""

#Importation de Tkinter et de la classe qui gère l'interface graphique
import tkinter as tk
from classe_interface_graphique import Interface_graphique


#Programme principal
if __name__ == "__main__":

    #Initialisation de la fenêtre principale
    root = tk.Tk()    

    #Création de l'interface graphique
    interface = Interface_graphique(root)
    interface.menu_ecran()
    
    #Boucle principale de l'interface graphique
    root.mainloop()