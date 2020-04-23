# Game-of-life
# Automate cellulaire

Le « jeu de la vie » est un automate cellulaire bidimensionnel où chaque cellule peut prendre deux valeurs
(« 0 » ou « 1 », mais on parle plutôt de « vivante » ou « morte ») et où son état futur est déterminé par son état actuel
et par le nombre de cellules vivantes parmi les huit qui l'entourent :

Si la cellule est vivante et entourée par deux ou trois cellules vivantes, elle reste en vie à la génération suivante, sinon elle meurt.
Si la cellule est morte et entourée par exactement trois cellules vivantes, elle naît à la génération suivante.
