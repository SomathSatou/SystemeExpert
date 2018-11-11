import re
import sys
from tkinter import * 
from tkinter.filedialog import *

BF = {} 

BR = {}

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
	regexp = re.compile(r'(?P<tete>\w+\([\s\w]+(,[\s\w]+)*\)).->.(?P<queue>[!\w]\w*\([\s\w\-]+(,[\s\w\-]+)*\)(,[!\w]\w*\([\s\w\-]+(,[\s\w\-]+)*\))*)\s*;')
	fait = re.compile(r'(?P<fait>\w+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')
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
			#print(bcolors.UNDERLINE + str(tmp.group('tete'))+" -> "+tmp.group('queue') + bcolors.ENDC)
		
		else:
			tmp = re.match(fait,ligne)
			if tmp is not None:
				variables = tmp.group('valeur').split(",")
				addFait(tmp.group('fait'),variables)
				#print(bcolors.UNDERLINE + str(tmp.group('fait'))+" -> "+tmp.group('valeur') + bcolors.ENDC)
			else:
				#print(bcolors.WARNING +" !!!!!!!!!!!! ligne non reconnue  !!!!!!!!!!!!!!!!"+ bcolors.ENDC)
				if ligne!="\n":
					error += "\n erreur de syntaxe: ligne "+str(num)
	sortie = sortie + error	
	return sortie


def addRegle(tete , queue):
	if tete in BR:
		BR[tete].append(queue)
	else :
		BR[tete] = [queue]
	return


def addFait(fait, valeur): #voir pour lu il fait une liste de liste avec un seul élément à l'intérieur ( une simple liste avec une string aurait suffit mais je pense que c'est normal)
	 # ajoute un fait dans la base de données ex (chat, Jahwi)
	if fait in BF:    # si le fait n'est pas encore dans la base on créée la liste avec le premier élément
		BF[fait].append(valeur)
	else :             # sinon on ajoute l'élément à la liste d'élément déjà existante
		BF[fait] = [valeur]
	return


def chainageAvant():
	choixAvant = Tk()
	choixAvant.geometry("200x65")
	choixAvant.title("choix de chainage avant")	

	def chp():
		chainageAvantP()
		choixAvant.destroy()
		return

	def chl():
		chainageAvantL()
		choixAvant.destroy()
		return

	choix = PanedWindow(choixAvant, orient=VERTICAL)
	choix.pack(expand=N, fill=BOTH, pady=2, padx=2)
	choix.add(Button(choix, text="Profondeur",command= chp))
	choix.add(Button(choix, text="Largeur", command= chl))

	choixAvant.mainloop()
	return

def chainageAvantP():
	listeElement = []
	contrainte = []
	fait = re.compile(r'(?P<fait>\w+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')	
	but = re.match(fait,entree.get())
	if but is not None:
		buts = but.group('valeur').split(",")
		#chainage avantP stocker les resultats dans listElement
		if but.group('fait') in BF:
			i = 0
			for test in BF[but.group('fait')]:
				if buts[0] == BF[but.group('fait')][i][0]:
					if len(BF[but.group('fait')][i]) >1:
						listeElement.append([buts[0],buts[1]])
					else:
						listeElement.append([buts[0],""])
				i=i+1
		if regles in BR:
			contrainte = 
			
	else : 
		listeElement = [["erreur de syntaxe dans la valeur interroger",entree.get()]]
	affichageConseil(listeElement)
	return

def chainageAvantL():
	listeElement = []
	#chainage avant en largeur a coder stocker les resultats dans listElement
	affichageConseil(listeElement)
	return 

def chainageArriere():
	listeElement = []
	fait = re.compile(r'(?P<fait>\w+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')	
	but = re.match(fait,entree.get())
	if but is not None:
		#chainage arrière stocker les resultats dans listElement
		print("ça passe")
	else : 
		listeElement = [["erreur de syntaxe dans la valeur interroger",entree.get()]]
	affichageConseil(listeElement)
	return 

def checkContradiction():
	#verifie qu'il n'y a pas de contradiction dans la base de connaissance	
	return

def affichageConseil(liste):
	tmp = ""
	for element in liste:
		tmp += "-"+element[0]+","+element[1]+"\n"
	if len(liste) == 0:
		tmp += "pas de solution dans la base de connaisance"
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
	global content, textConseil, entree
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
	p.add(bouton)

	value = StringVar() 
	value.set("champ de saisie pour l'ajout a la base ou l'interoger")
	entree = Entry(fenetre, textvariable=value, width=300)
	entree.pack()

	conseil = LabelFrame(fenetre, text="Nous vous conseillons", padx=20, pady=20)
	conseil.pack(fill="both", expand="yes")

	textConseil = StringVar()
	textConseil.set("bientôt des livres d'exception par ici")
	labelConseil = Label(conseil, textvariable= textConseil)
	labelConseil.pack(padx=10,pady=10)

	fenetre.mainloop()
	return

# ------------ main -----------------

interface()
