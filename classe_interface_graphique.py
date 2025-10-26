# -*- coding: utf-8 -*-
"""
Auteur : Le Godec Loïc & Arial Martin
Date : 06/10/2025
Description : Casse-briques
"""


#Importation de Tkinter et des autres classes nécessaires
import tkinter as tk
from classe_logique import Logique
from classe_cmd import Commande_clavier
from classe_balle import Balle
from classe_briques import Briques
from classe_planche import Planche

class Interface_graphique:
    """
    Classe Interface Graphique:
    C'est la classe qui gère toute la partie visuelle et affichage du jeu
    Elle appelle toutes les autres.
    """
    def __init__(self, root):
        """
        Initialisation des variables

        Variables:
            Fenetre: la fenêtre principale du jeu
            Canevas: le canevas qui contient tous les éléments du jeu
            Fond: le fond d'écran du jeu
            Bouton_quitter: le bouton pour quitter le jeu et fermer la fenêtre
            Bouton_démarrer: le bouton pour lancer démarrer_jeu()
            Bouton_skin: le bouton pour accéder au menu skin_ecran()
            Logique: appel de la classe Logique qui s'occupe des règles du jeu
            Briques: appel de la classe Briques qui gère l'état des briques
            Planche: appel de la classe Planche qui gère la planche et ses déplacements
            Commande: appel de la classe Commande_clavier qui récupère les actions claviers
            Balle: appel de la classe Balle qui gère les déplacements, les collisions,etc... de la balle
            Skin_couleur: Initialisation de la couleur de base de la balle
            Liste_scores: Initialisation de la liste contenant les meilleurs scores (Utilisation d'une Pile)

        """
        self.fenetre = root
        self.fenetre.title("Casse Briques")
        self.canevas = tk.Canvas(root, width=1000, height=700)
        self.fond = tk.PhotoImage(file = "img/fond_ecran.png")
        self.bouton_quitter = tk.Button(self.canevas, text="Q U I T T E R", bg="#F7DD68",     highlightcolor="white", width=10, height=2, font=("Arial", 14), command=root.destroy)
        self.bouton_démarrer = tk.Button(self.canevas, text="J O U E R", bg="#F7DD68",     highlightcolor="white", width=10, height=2, font=("Arial", 14), command=self.demarrer_jeu)
        self.skin = tk.Button(self.canevas, text="S K I N", bg="#F7DD68",     highlightcolor="white", width=10, height=2, font=("Arial", 14), command=self.skin_ecran)
        self.logique = Logique()
        self.briques = Briques(self.canevas, self.logique, self)
        self.planche = Planche(self.canevas)
        self.commande = Commande_clavier(self.canevas, self.planche)
        self.balle = Balle(self.canevas, self.planche, self.briques, self.logique, self)
        self.skin_couleur = "white"
        self.liste_scores = [0] #Utilisation d'une pile pour gérer les meilleurs scores


    #Menu principal :

    def menu_ecran(self):
        """Créé le menu écran

        Variables:
            Logique.niv: Réinitialisation de la liste des niveaux (Utilisation d'une File)
        
        """

        self.logique.niv = [5,4,3,2,1]

        #Supprime tout les canevas des différents menu
        self.canevas.delete("menu_fin")
        self.canevas.delete("menu_skin")
        self.canevas.delete("top_menu")
        self.canevas.delete("menu_victoire")

        #Initialise le caneva et créé les images, texte et window pour faire le menu
        self.canevas.pack()
        self.canevas.create_image(0,0, image = self.fond, anchor = "nw")
        self.canevas.create_text(500, 200, text="C A S S E  B R I Q U E S", fill="white", font=("Arial", 40), tags="menu")
        self.canevas.create_window(500, 320, window=self.bouton_démarrer, tags="menu")
        self.canevas.create_window(500, 380, window=self.skin, tags="menu")
        self.canevas.create_window(500, 440, window=self.bouton_quitter, tags="menu")


    #Menu Skin :

    def afficher_skin(self):
        """Fonction qui créé le menu skin

        Variables:
            Label_choose: Texte pour expliquer le menu
            Bouton1/2/3/4: Bouton qui permet de changer la couleur appliquer_skin1/2/3/4
            Bouton_retour: Bouton qui permet de revenir au menu_ecran()
        """
        self.label_choose = tk.Label(self.canevas, text="Choisissez votre skin de balle :", bg="#3434FF", fg="white", font=("Arial", 16))
        self.bouton1 = tk.Button(self.canevas, text="skin Jaune", bg="yellow", width=10, height=2, font=("Arial", 14), command=self.appliquer_skin1)
        self.bouton2 = tk.Button(self.canevas, text="skin Rose", bg="pink", width=10, height=2, font=("Arial", 14), command=self.appliquer_skin2)
        self.bouton3 = tk.Button(self.canevas, text="skin Rouge", bg="red", width=10, height=2, font=("Arial", 14), command=self.appliquer_skin3)
        self.bouton4 = tk.Button(self.canevas, text="skin Vert", bg="green", width=10, height=2, font=("Arial", 14), command=self.appliquer_skin4)
        self.bouton_retour = tk.Button(self.canevas, text="R E T O U R", bg="#F7DD68", highlightcolor="white", width=10, height=2, font=("Arial", 14), command=self.menu_ecran)
        
        #Création des différentes fenêtres contenant les boutons et le label
        self.canevas.create_window(500, 200, window=self.label_choose, tags="menu_skin")
        self.canevas.create_window(500, 260, window=self.bouton1, tags="menu_skin")
        self.canevas.create_window(500, 320, window=self.bouton2, tags="menu_skin")
        self.canevas.create_window(500, 380, window=self.bouton3, tags="menu_skin")
        self.canevas.create_window(500, 440, window=self.bouton4, tags="menu_skin")
        self.canevas.create_window(500, 500, window=self.bouton_retour, tags="menu_skin")

    def appliquer_skin1(self):
        """Change la couleur en jaune
        """
        self.skin_couleur = "yellow"

    def appliquer_skin2(self):
        """Change la couleur en rose
        """
        self.skin_couleur = "pink"

    def appliquer_skin3(self):
        """Change la couleur en rouge
        """
        self.skin_couleur = "red"

    def appliquer_skin4(self):
        """Change la couleur en vert
        """
        self.skin_couleur = "green"

    def skin_ecran(self):
        """Créé le menu skin
        """
        self.canevas.delete("menu")
        self.afficher_skin()


    #Fonction de reset

    def reset_jeu(self):
        """Fonction qui réinitialise toute les classes et variables du jeu

        Variables:
            Logique.life: Réinitialisation des vies
            Briques: appel de la classe Briques qui gère l'état des briques
            Planche: appel de la classe Planche qui gère la planche et ses déplacements
            Commande: appel de la classe Commande_clavier qui récupère les actions claviers
            Balle: appel de la classe Balle qui gère les déplacements, les collisions,etc... de la balle
        """

        self.logique.life = 3
        self.briques = Briques(self.canevas, self.logique, self)
        self.planche = Planche(self.canevas)
        self.commande = Commande_clavier(self.canevas, self.planche)
        self.balle = Balle(self.canevas, self.planche, self.briques, self.logique, self)

    def reset_score(self):
        """Fonction qui reset le score

        Variables:
            Logique.score: Réinitialisation du score
        """

        self.logique.score = 0


    #Affichage début du jeu, victoire et défaite :

    def demarrer_jeu(self):
        """Fonction qui lance le jeu

        Variables:
            Jeu_actif: Prend en valeur True tant que l'écran démarrer_jeu() tourne
            text_niveau/vie/best/score: création de texte en haut de l'écran
        """
        
        self.jeu_actif = True

        #Supprime tout les autres menus
        self.canevas.delete("menu")
        self.canevas.delete("menu_fin")
        self.canevas.delete("menu_victoire")

        #Initialise le canevas, le texte et les images
        self.canevas.pack()
        self.canevas.create_image(0,0, image = self.fond, anchor = "nw")
        self.text_niveau = self.canevas.create_text(300, 20, text=f"N I V : {self.logique.niv[-1]}", fill="white", font=("Arial", 20, "bold"), tags="top_menu")
        self.text_vie = self.canevas.create_text(20, 20, text=f"V I E S  : {self.logique.life}", fill="white", font=("Arial", 20, "bold"), anchor="w", tags="top_menu")
        self.text_best = self.canevas.create_text(600, 20, text=f"B E S T  : {self.liste_scores[-1]}", fill="white", font=("Arial", 20, "bold"), anchor="e", tags="top_menu")
        self.text_score = self.canevas.create_text(900, 20, text=f"S C O R E  : {self.logique.score}", fill="white", font=("Arial", 20, "bold"), anchor="e", tags="top_menu")

        #Appel de fonction dans différente classe
        self.planche.afficher_planche()
        self.briques.creer_briques()
        self.balle.afficher_balle()
        if self.jeu_actif:  #Seulement si jeu_actif == True
            self.balle.deplacer_balle()
        
    def fin_jeu(self):
        """Fonction Game Over qui envoie un écran quand le joueur perd
        Variables:
            Jeu_actif: Prend la valeur False pour agir sur l'arrêt total de la balle et du jeu
            Game_over: Texte
            Recommencer/Menu: Bouton pour recommencer ou retourner au menu
        """

        self.jeu_actif = False

        #Création de bouton avec comme commande la réinitialisation du jeu et du score puis l'écran démarrer_jeu()
        self.recommencer = tk.Button(self.canevas, text="R E C O M M E N C E R", bg="#F7DD68",     highlightcolor="white", width=25, height=2, anchor="center", font=("Arial", 14), command=lambda:[self.reset_jeu(), self.demarrer_jeu(), self.reset_score()])
        
        #Création de bouton avec comme commande la réinitialisation du jeu et du score puis l'écran menu_ecran()
        self.menu = tk.Button(self.canevas, text="M E N U", bg="#F7DD68",     highlightcolor="white", width=10, height=2, font=("Arial", 14), anchor="center", command=lambda:[self.reset_jeu(), self.menu_ecran(), self.reset_score()])
        
        #Appel de la fonction pour arrêter les déplacement de la balle
        self.balle.stop_balle()
        
        #Supprime tout les canevas
        self.canevas.delete("all")
        
        #Ajoute sur la pile (liste_scores) le meilleur scores
        if self.logique.score > self.liste_scores[-1]:
            self.liste_scores.append(self.logique.score)
        
        #Création de l'interface game_over
        self.canevas.create_text(500, 340, text="G A M E  O V E R", fill="red", font=("Arial", 40), tags="menu_fin")
        self.canevas.create_window(500,460, window = self.recommencer, tags="menu_fin")
        self.canevas.create_window(500,520, window = self.menu, tags="menu_fin")

    def victoire_finale(self):
        """Fonction Victoire qui envoie un écran victoire
        Variables:
            Jeu_actif: Prend la valeur False pour agir sur l'arrêt total de la balle et du jeu
            Score final: Texte affichant le score final
            Niveau suivant/Menu: Bouton pour passer au niveau suivant ou retourner au menu
        """

        self.jeu_actif = False

        #Arrêt de la balle
        self.balle.stop_balle()

        #Si le score est meilleur que le dernier, l'ajouter a la liste_scores 
        if self.logique.score > self.liste_scores[-1]: #Prend toujours le dernier élément de la liste, principe de la pile
            self.liste_scores.append(self.logique.score) #Ajoute un élément à la pile

        #Supprime tout les canevas et en recréer d'autre pour un texte et les boutons
        self.canevas.delete("all")
        self.canevas.create_text(500, 340, text="F É L I C I T A T I O N S  !", fill="black",font=("Arial", 40, "bold"), tags="menu_victoire")
        self.canevas.create_text(500, 400, text=f"Score final : {self.logique.score}", fill="black", font=("Arial", 14), tags="menu_victoire")
        self.niv_suivant = tk.Button(self.canevas, text="N I V E A U  S U I V A N T :", bg="#F7DD68",     highlightcolor="white", width=25, height=2, anchor="center", font=("Arial", 14), command=lambda:[self.logique.niv_suivant(), self.reset_jeu(), self.demarrer_jeu()])
        self.menu_vic = tk.Button(self.canevas, text="M E N U", bg="#F7DD68",     highlightcolor="white", width=10, height=2, font=("Arial", 14), anchor="center", command=lambda:[self.reset_jeu(), self.menu_ecran()])
        self.canevas.create_window(500,460, window = self.niv_suivant,tags="menu_victoire")
        self.canevas.create_window(500,520, window = self.menu_vic, tags="menu_victoire")


    #Fonction de mise à jour

    def maj_vie(self):
        """Fonction qui met à jour les vies 
        """

        #Met à jour le visuel pour les vies
        self.canevas.itemconfig(self.text_vie, text=f"V I E S  : {self.logique.life}")

        #Si il n'y a plus de vie, il y a game over
        if self.logique.life <= 0:
            self.fin_jeu()

    def maj_point(self):
        """Fonction qui met à jour les points
        """

        #Met à jour le visuel des points
        self.canevas.itemconfig(self.text_score, text=f"S C O R E  : {self.logique.score}")
