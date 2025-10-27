
Projet de Jeu Casse-Briques:
____________________________

Auteurs : Loïc Le Godec & Martin Arial
Date : 20 octobre 2025
____________________________

--- Description Générale du Projet ---

Ce programme Python est inspiré du jeu d'arcade classique "Casse-Briques", réalisé à l'aide de la bibliothèque Tkinter. L'objectif principal était de mettre en pratique les concepts de programmation par classe, de gestion des objets et des collisions dans une interface graphique, ainsi que d'utiliser une file, une liste et une pile.


--- Principes et Règles du Jeu ---

- Objectif : Le but du jeu est de détruire l'ensemble des briques présentes dans l'écran de jeu.

- Mécanique principale : Le joueur contrôle une planche située en bas de l'écran afin de faire rebondir une balle. Lorsque la balle entre en collision avec une brique, cette dernière perd en solidité et peut-être  détruite.

- Condition de défaite : Une vie est perdue si la balle franchit le bas de l'écran. La partie s'achève lorsque le joueur a épuisé ses 3 vies.

- Condition de victoire : Le joueur remporte le niveau en cours lorsque toutes les briques ont été éliminées de l'écran. Le jeu comporte 5 niveaux de plus en plus difficiles.


--- Caractéristiques propres à notre jeu ---

Notre programme intègre plusieurs fonctionnalités techniques spécifiques.

- Gestion de la Collision sur la Raquette :
  L'angle de rebond de la balle sur la planche n'est pas classique. Il est calculé dynamiquement en fonction du point d'impact sur la raquette. Un impact au centre produit un rebond vertical, tandis qu'un impact sur les côtés engendre un rebond diagonal dont l'angle dépend de la distance par rapport au centre de la planche.

- Initialisation Aléatoire de la Trajectoire :
  Afin d'assurer la non-répétitivité des parties, la trajectoire initiale de la balle est déterminée par un angle de départ aléatoire, calculé dans un intervalle allant de -40 à 140 degrés.

- Système de Score :
  Un système de score a été implémenté. Chaque brique détruite augmente le score du joueur de 10 points. Le score affiché est toujours celui de la partie en cours, reset à chaque niveau. Le meilleur est enregistré dans une pile et affiché.

- Gestion des Niveaux :
  Le jeu est composé de 5 niveaux prédéfinis, chacun présentant une disposition de briques différente et une difficulté croissante (une ligne supplémentaire et parfois certaines briques sont plus solides).
Les niveaux s'enchainent, ils sont stockés sous forme d'une pile.
Vous pouvez recommencer le dernier niveau en cas d'échec, ou repartir au menu initial.

- Skins de la Balle et Fond d'écran :
  Le jeu possède un fond d'écran unique et vous propose de choisir la couleur de la balle parmi certaines proposées dans le menu en cliquant sur le bouton skin.



--- Contrôles et Jeu ---

Pour jouer lancer le programme, choisissez éventuellement le skin de balle que vous désirez puis cliquez sur jouer.
Les commandes pour jouer sont les flèches gauche et droite du clavier.


Nous espérons que le programme vous plaira,
Sincèrement,

Martin ARIAL & Loïc LE GODEC


