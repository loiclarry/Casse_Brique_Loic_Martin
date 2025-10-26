# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
Caractéristiques de notre jeu: Skins de balle, angle de rebond de la balle sur la planche, niveaux de difficultés.
"""


class Planche:
    def __init__(self, canevas):
        """Initialisation des variables

        Variables:
            canevas_planche: importation du caneva principal dans Planche
            x: Coordonnées initiale de la planche à gauche et à droite
            coord: Liste des coordonnées
        """

        self.caneva_planche = canevas
        self.x = [450, 550]
        self.coord = [self.x[0], self.x[1]]


    #Visuel de la planche

    def afficher_planche(self):
        """Fonction qui affiche la planche, appel dans l'interface
        """

        self.visu_planche = self.caneva_planche.create_rectangle(450, 670, 550, 690, fill="white")


    #Déplacement de la planche
    
    def deplacer_gauche(self, event):
        """Fonction de déplacement de la planche

        Variables:
            event: Appel d'un event dans Commande_clavier
        """

        #Si la planche ne dépasse pas le mur de gauche, la planche move vers la gauche
        if self.x[0] > 20:
            self.caneva_planche.move(self.visu_planche, -20, 0)
            self.x = [self.x[0] - 20, self.x[1] - 20] #Mise à jour des coordonnées
            self.coord = [self.x[0], self.x[1]] #Mise à jour des coordonnées

    def deplacer_droite(self, event):
        """Fonction de déplacement de la planche

        Variables:
            event: Appel d'un event dans Commande_clavier
        """

        #Si la planche ne dépasse pas le mur de droite, la planche move vers la gauche
        if self.x[1] < 980:
            self.caneva_planche.move(self.visu_planche, 20, 0)
            self.x = [self.x[0] + 20, self.x[1] + 20] #Mise à jour des coordonnées
            self.coord = [self.x[0], self.x[1]] #Mise à jour des coordonnées