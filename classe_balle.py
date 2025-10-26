# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
Caractéristiques de notre jeu: Skins de balle, angle de rebond de la balle sur la planche, niveaux de difficultés.
"""


import random
import math

class Balle:
    def __init__(self, canevas, planche, briques, logique, interface):
        """Initialisation des variables

        Variables:
            canevas: importation du caneva principal dans Balle
            planche: importation de Planche
            briques: importation de Briques
            logique: importation de la logique du jeu
            interface: importation de l'interface graphique
            vitesse: Vitesse de la balle
            angle: Angle de départ de la balle
            dx, dy: Vecteurs de déplacement de la balle
            x, y: Coordonnées initiales de la balle
            rayon: Rayon de la balle
            stop: Booléen pour arrêter la balle
        """
        self.caneva_balle = canevas
        self.vitesse = 12
        self.angle = random.uniform(math.pi/6, (5*math.pi)/6)
        self.dx = self.vitesse * math.cos(-self.angle)
        self.dy = self.vitesse * math.sin(-self.angle)
        self.x = 500
        self.y = 659
        self.rayon = 10
        self.planche = planche
        self.brique = briques
        self.logique = logique
        self.interface = interface
        self.stop = True


    #Visuel de la balle

    def afficher_balle(self):
        """Fonction pour affichier la balle
        """

        self.visu_balle = self.caneva_balle.create_oval(490, 650, 510, 670, fill=self.interface.skin_couleur)


    #Reset et arrêt de la balle

    def reset_ball(self):
        """Fonction qui reset toutes les caractéristique de la balle
        """

        #Reset de toutes les variables de la balle
        self.x = 500
        self.y = 659
        self.angle = random.uniform(math.pi/6, (5*math.pi)/6)
        self.dx = self.vitesse * math.cos(self.angle)
        self.dy = -(self.vitesse * math.sin(self.angle))
        self.caneva_balle.coords(self.visu_balle,self.x - self.rayon,self.y - self.rayon,self.x + self.rayon,self.y + self.rayon)

    def stop_balle(self):
        """Fonction qui arrête la balle
        """

        #Changement du booléen stop
        self.stop = False


    #Déplacement de la balle

    def deplacer_balle(self):
        """Fonction qui s'occupe du déplacement de la balle et des collisions
        """

        #Récupération des coordonnées de la planche
        x_planche1, x_planche2 = self.planche.coord[0], self.planche.coord[1]

        #Gestion des collisions avec les murs
        if self.x + self.rayon >= 995 or self.x - self.rayon <= 5:
            self.x -= self.dx
            self.dx = -self.dx

        if self.y - self.rayon <= 5:
            self.y -= self.dy
            self.dy = -self.dy

        #Gestion des collisions avec la planche
        if self.y + self.rayon > 669:
            if self.x + self.rayon > x_planche1 and self.x - self.rayon < x_planche2:
                self.y = 2*(670 - self.rayon) - self.y

                #L'impact fais en sorte que la balle rebondisse selon l'endroit ou elle touche la planche
                impact_x = (self.x - (x_planche2-50))/(100) 
                angle_refl=(-impact_x*(math.pi/3))+(math.pi/2)
                self.dx=self.vitesse*math.cos(angle_refl)
                self.dy=self.vitesse* math.sin(angle_refl)
                
                self.dy = -self.dy

        #Gestion des collisions avec les briques
        for i in self.brique.liste_briques[:]: #liste_briques contient des listes de coordonnées [x1,x2,y1,y2, visuel]
            if self.x + self.rayon > i[0] and self.x - self.rayon < i[1] and self.y + self.rayon > i[2] and self.y - self.rayon < i[3]:
                
                #Calcul de la position précédente de la balle
                pre_x=self.x -self.dx

                #Collision latérale
                if (pre_x + self.rayon < i[0] and self.x + self.rayon >i[0]) or (pre_x - self.rayon > i[1] and self.x - self.rayon < i[1]):
                    self.brique.frapper_brique(i)
                    self.logique.point()
                    self.interface.maj_point()
                    self.dx = -self.dx
                    break
                
                #Collision verticale
                self.brique.frapper_brique(i)
                self.logique.point()
                self.interface.maj_point()
                self.dy = -self.dy
                break
        
        #Vérification de la victoire
        if self.brique.liste_briques == []:
            self.interface.victoire_finale()
        
        #Vérification de la perte de vie
        if self.y > 700:
            self.logique.vie_perdu()
            self.interface.maj_vie()
            if self.logique.life > 0:
                self.reset_ball()

        #Mise à jour des coordonnées de la balle
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        #Mise à jour du visuel de la balle
        self.caneva_balle.coords(self.visu_balle, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)
        
        #Rappel de la fonction toutes les 20 ms tant que le booléen stop est vrai
        #20 ms est un bon compromis entre fluidité et performance pour le module tkinter
        if self.stop == True:
            self.caneva_balle.after(20, self.deplacer_balle)

