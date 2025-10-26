# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
Caractéristiques de notre jeu: Skins de balle, angle de rebond de la balle sur la planche, niveaux de difficultés.
"""


class Briques:
    def __init__(self, canevas, logique, interface):
        """Initialisation des variables

        Variables:
            canevas_brique: Importation du caneva principal dans Brique
            logique: Importation de la logique du jeu
            interface: Importation de l'interface graphique
            x1, y1, x2, y2: Coordonnées des briques
            liste_briques: Liste des briques
            couleurs: Liste des couleurs des briques selon le niveau
        """

        self.interface = interface
        self.caneva_brique = canevas
        self.logique = logique
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.liste_briques = []
        self.couleurs = ["red", "#B50101", "#8A0202", "#640202", "#200000"]
    

    #Création des briques

    def creer_briques(self):
        """Fonction qui créé les briques

        Variables:
            niv: Niveau de difficulté
            br: Visuel de la brique
            liste_briques: Liste des briques avec leurs coordonnées et leur visuel
        """

        #Boucle qui créé les briques en fonction du niveau de difficulté
        for i in range(self.logique.niv[-1]):
            for j in range(10):
                self.x1 = 10 + j*98
                self.y1 = 35 + i*38
                self.x2 = self.x1 + 95
                self.y2 = self.y1 + 35
                br = self.caneva_brique.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="red")
                self.liste_briques.append([self.x1,self.x2,self.y1,self.y2, br])


    #Frapper une brique

    def frapper_brique(self, brique):
        """Fonction qui change la couleur de la brique ou casse la brique si on tape de dessus suivant le niveau

        Variables:
            brique: Importation de la liste_briques pour savoir quelle brique est frappée
        """

        
        if self.caneva_brique.itemcget(brique[4], 'fill') == 'red' and self.logique.niv[-1] >1:
            self.caneva_brique.itemconfig(brique[4], fill="#B50101") #Change la couleur de la brique
        elif self.caneva_brique.itemcget(brique[4], 'fill') == "#B50101" and self.logique.niv[-1] >2:
            self.caneva_brique.itemconfig(brique[4], fill="#8A0202")
        elif self.caneva_brique.itemcget(brique[4], 'fill') == "#8A0202" and self.logique.niv[-1] >3:
            self.caneva_brique.itemconfig(brique[4], fill= "#640202")
        elif self.caneva_brique.itemcget(brique[4], 'fill') ==  "#640202" and self.logique.niv[-1] >4:
            self.caneva_brique.itemconfig(brique[4], fill= "#200000")
        else:
            self.caneva_brique.delete(brique[4]) #Supprime la brique
            self.liste_briques.remove(brique)
