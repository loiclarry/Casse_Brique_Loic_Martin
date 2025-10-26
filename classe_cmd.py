# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
Caractéristiques de notre jeu: Skins de balle, angle de rebond de la balle sur la planche, niveaux de difficultés.
"""



class Commande_clavier:
    def __init__(self, canevas, planche):
        """Initialisation des variables

        Variables:
            canevas: importation du caneva principal dans Commande_clavier
            planche: importation de Planche
        """

        self.canevas = canevas
        self.planche = planche

        #Liaison des touches gauche et droite avec les fonctions de déplacement de la planche
        self.canevas.bind_all("<KeyPress-Left>", self.planche.deplacer_gauche)
        self.canevas.bind_all("<KeyPress-Right>", self.planche.deplacer_droite)
        
