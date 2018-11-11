############################################################
#			Systeme expert			   #
############################################################

	Pour lancer ce programmme pas besoin de lui donner 
d'argument, la commande suivante suffit :

	python3 systeme.py

	Vous devrez alors choisir une base de connaissances
à l'aide du bouton "sélectionner base". Cela génèrera 
l'affichage de la base de données séléctionnée. Ensuite 
pour faire fonctionner le programme il faudra choisir 
"chainage avant" ou "chainage arrière" ce qui génèrera
les résultats dans la partie inférieure du programmme.

	1 - Objectifs 
	
	Nous souhaitions réaliser un système expert capable 
de recommander des livres à lire en fonction d'une base de 
données, ici réduite à quelques exemples par faute de temps
mais nous avions imaginé ajouter une procédure qui permet 
de générer automatiquement nos bases de connaissances à 
partir de bases de données extérieures. 

	2 - Syntaxe 

	Nous nous sommes inspirés de la syntaxe de prolog
pour générer notre base de connaissances sous format text
pour la rendre plus accessible au plus grand nombre. 
Ainsi :

	Cause(var)->consequence(var),consequence2(var,var2);

	signifiera que si cause(var) est présent dans la 
base de faits alors on aura consequence(var) dans notre base
étendue, etc.

	Fait(var);

	indique que pour la variable "var" le fait est ajouté
dans la base de faits

	le ; nous sert à reconnaitre la fin d'une règle ou d'un 
fait

	3 - Un système transposable

	En principe notre système s'adapte à toute base de 
données culturelle (films, musées, etc.) en modifiant le 
fait que notre système regarde en priorité "lu", vu que les
faits qui aident à la décision "aime()" ou "pas()" restent les 
mêmes.

	4 - Interactif 

	Nous avons imaginé notre système de façon interactive
pour que l'on puisse modifier directement depuis le programme 
notre base de connaissances. Nous n'avons pas réalisé cela 
jusqu'au bout, d'où la présence des boutons qui devaient 
servir à ajouter des faits et à sauvegarder la nouvelle base.

	5 - Le chainage arrière 

	Pour interroger la base de connaissances via le 
chainage arrière il faut remplir le champ 
"champ de saisie pour l'ajout à la base ou l'interroger"
	par exemple je veux savoir si le système me recommande
de lire "une seconde après"

	Propose(Une seconde apres,William R Forstchen);

	Attention la casse n'est pas gérée par notre parser.
