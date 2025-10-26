# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
Caractéristiques de notre jeu: Skins de balle, angle de rebond de la balle sur la planche, niveaux de difficultés.
"""


class Logique: 
    def __init__(self):
        """Initialisation des variables

        Variables:
            life: Nombre de vie du joueur
            score: Score du joueur
            niv: Liste des niveaux de difficulté
        """

        self.life = 3
        self.score = 0
        self.niv = [5,4,3,2,1] #Utilisation d'une file pour gérer les niveaux


    # Gestion des vies, du score et des niveaux

    def vie_perdu(self):
        """Fonction qui enlève une vie

        Returns:
            life: Nombre de vie restant
        """

        self.life = self.life - 1
        return self.life

    def point(self):
        """Fonction qui augmente le score

        Returns:
            score: Score actuel
        """

        self.score += 10
        return self.score

    def niv_suivant(self):
        """Fonction qui augmente les niveaux

        Returns:
            niv_actuel: Niveau actuel
        """
        self.niv.remove(self.niv[-1]) #Enlève le niveau actuel pour prendre le suivant
        self.niv_actuel = self.niv[-1]
        return self.niv_actuel