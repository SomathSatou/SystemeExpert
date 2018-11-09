############################################################
#			Systeme expert			   #
############################################################

	Pour lancer ce programmme pas besoin de lui donner 
des d'argument, la commande suivant suffit :

	python3 systeme.py

	Vous devrez alors choisir une base de connaissance
a l'aide du boutton "selectionner base" cela généreras 
l'affichage de la base de donnés séléctionné, ensuite 
pout faire fonctionner le programme il faudras choisir 
"chainage avant" ou "chainage arrière" qui généras ensuite 
les resutlats dans la partie inférieur du programmme.

	1 - Objectifs 
	
	nous souhaitions rélisée un Systeme expert capable 
de recommandé des livres a lire en fonction d'un base de 
donnés, ici réduite a quelque exemple par faute de temps
mais nous avions imaginé ajouté un procédure qui permet 
de generer automatiquement nos base de connaissance à 
partir de base de données exterieur. 

	2 - Syntaxe 

	nous nous sommes inspiré de la syntaxe de prolog
pour générer notre base de connaissance sous format text
pour la rendre plus accessible aux plus grand nombre, 
ainsi 

	Cause(var)->consequence(var),conséquence2(var,var2) 

	signifiras que si cause(var) est présent dans la 
Base de fait alors on auras consequence(var) dans notre base
étendu ... etc

	Fait(var) 

	indique que pour la var le fait est ajouter dans la
base de fait

	3 - Un systeme transposable

	En principe notre systeme s'adapte a toute base de 
données culturel, films, musée, etc ... en modifiant le 
fait que notre systeme regarde en priorité "lu", vue que les
fait qui aident a la décision "aime()" ou "pas()" reste les 
mêmes

	4 - Interactif 

	Nous avons imaginer notre systeme de façons interactifs
pour que l'on puisse modifier directement du programme notre 
base de connaissance, nous n'avons pas réaliser cela jusqu'au
bout d'ou la présence des bouton qui devais servir a ajouter 
des fait et a sauvegarder la nouvelle base
