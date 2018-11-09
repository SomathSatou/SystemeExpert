import re
import sys
from tkinter import * 
from tkinter.filedialog import *

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def lectureBase(nomFichier):
	f= open(nomFichier,"r")
	sortie = f.read()
	f.close()
	f= open(nomFichier,"r")
	lignes  = f.readlines()
	
	f.close()
	"""expression regulier regle, fait"""
	regexp = re.compile(r'(?P<tete>\w+\([a-zA-Z]*(,[a-zA-Z]*)*\)).->.(?P<queue>\w+\([a-zA-Z]*(,[a-zA-Z]*)*\))')
	fait = re.compile(r'(?P<fait>\w+\([a-zA-Z]*(,[a-zA-Z]*)*\))')
	num = 0
	error = ""
	for ligne in lignes:
		num+=1
		#print("--------------------------------------newligne-------------------------------------------------------")
		#print(ligne)
		tmp = regexp.match(ligne)
		if tmp is not None:
			coupe = tmp.group('queue').split(",")
			addRegle(tmp.group('tete'),coupe)
		
		else:
			if re.match(fait,ligne) is not None:
				addFait()
			else:
				#print(bcolors.WARNING +" !!!!!!!!!!!! ligne non reconnue  !!!!!!!!!!!!!!!!"+ bcolors.ENDC)
				error += "\n erreur de syntaxe: ligne "+str(num)
	sortie = sortie + error	
	return sortie

def stringToArraylist():
	return 

def addRegle(fait , valeur):
	print("Charline a toi de jouer")
	return

def addFait():
	print("Charline a toi de re-jouer")
	return


def chainageAvant():
	#création d'une fenetre proposant le choix profondeur/largeur
	return

def chainageAvantP():
	listeElement = []
	#chainage avant en profondeur a coder stocker les resultats dans listElement
	affichageConseil(listeElement)
	return

def chainageAvantL():
	listeElement = []
	#chainage avant en largeur a coder stocker les resultats dans listElement
	affichageConseil(listeElement)
	return 

def chainageArriere():
	listeElement = []
	#chainage arrière stocker les resultats dans listElement
	affichageConseil(listeElement)
	return 

def affichageConseil(liste):
	for element in liste:
		tmp += "- "+element[0]+" par "+element[1]+"\n"
	textConseil.set(tmp)
	return

def sauverBase():
	#featuring non demandé si on a le temps 	
	return

def ajoutBase():
	#featuring non demandé si on a le temps 	
	return

def openBase():
	filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
	fichier = open(filename, "r")
	content.set(lectureBase(filename))
	fichier.close()
	return

def interface():
	global content, textConseil
	fenetre = Tk()
	fenetre.geometry("800x1200")
	fenetre.title("Quoi lire?")

	l = LabelFrame(fenetre, text="base de conaissance", padx=20, pady=20)
	l.pack(fill="both", expand="yes")
	 
	content = StringVar()
	content.set("selectionner une basse de données")
	base = Label(l, textvariable=content)
	base.pack(padx=10, pady=10)

	p = PanedWindow(fenetre, orient=HORIZONTAL)
	p.pack(expand=N, fill=BOTH, pady=2, padx=2)
	buttonOuvrir = Button(p,text="selectionner base", command= openBase)
	#buttonOuvrir.pack(side=LEFT )
	p.add(buttonOuvrir)

	addBase = Button(p, text="Ajouter dans la base", command=ajoutBase)
	p.add(addBase)

	saveBase = Button(p, text="Sauvegarde", command= sauverBase)
	p.add(saveBase)

	ChainageAvant = Button(p, text="Chainage avant", command= chainageAvant)
	p.add(ChainageAvant)

	chainageArriereButton= Button(p, text="Chainage arrière", command= chainageArriere)
	p.add(chainageArriereButton)

	bouton=Button(p, text="Aurevoir", command=sys.exit)
	#bouton.pack(side=RIGHT)
	p.add(bouton)
	
	value = StringVar() 
	value.set("champ de saisie pour l'ajout a la base")
	entree = Entry(fenetre, textvariable=value, width=300)
	entree.pack()

	conseil = LabelFrame(fenetre, text="Nous vous conseillons", padx=20, pady=20)
	conseil.pack(fill="both", expand="yes")

	textConseil = StringVar()
	textConseil.set("- La part de l'autre")
	labelConseil = Label(conseil, textvariable= textConseil)
	labelConseil.pack(padx=10,pady=10)

	fenetre.mainloop()
	return

# ------------ main -----------------

#lectureBase(sys.argv[1])
interface()
print("au travail !!!")
