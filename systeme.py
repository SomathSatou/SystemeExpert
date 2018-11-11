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
	regexp = re.compile(r'(?P<tete>\w+\([\s\w]+(,[\s\w]+)*\)(&[!\w]\w*\([\s\w\-]+(,[\s\w\-]+)*\))*).->.(?P<queue>[!\w]\w*\([\s\w\-]+(,[\s\w\-]+)*\)(&[!\w]\w*\([\s\w\-]+(,[\s\w\-]+)*\))*)\s*;')
	fait = re.compile(r'(?P<fait>[\!\w]+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')
	num = 0
	error = ""
	for ligne in lignes:
		num+=1
		#print("--------------------------------------newligne-------------------------------------------------------")
		#print(ligne)
		tmp = regexp.match(ligne)
		if tmp is not None:
			coupe = tmp.group('queue').split("&")
			coupetete = tmp.group('tete')
			addRegle(coupetete,coupe)
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
	#print("\nBase de regles")
	#print(BR)
	#print("\nBase de Faits")
	#print(BF)
	return sortie


def addRegle(tete , queue):
	fait = re.compile(r'(?P<fait>[\!\w]+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*')
	cle = ""
	variable = []
	coupTete= tete.split("&")
	for elem in coupTete:
		regle = fait.match(str(elem))
		if regle is not None:
			cleTmp = regle.group('fait')
			if cle != "" :
				cle = cle+","+cleTmp
			else:
				cle= cleTmp
			variableTmp = regle.group('valeur').split(",")
			variable.append(variableTmp)
	
	variable.append(queue)
	if cle in BR:
		BR[cle].append(variable)
	else :
		BR[cle] = [variable]
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

def chainageArriere():
	solution = 0
	contraintes = []
	fait = re.compile(r'(?P<fait>[\!\w]+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')	
	but = re.match(fait,entree.get())
	if but is not None:
		buts = but.group('valeur').split(",")
		#chainage avantP stocker les resultats dans listElement
		if but.group('fait') in BF:
			i = 0
			faitTmp = but.group('fait')
			for test in BF[but.group('fait')]:
				if buts[0] == BF[but.group('fait')][i][0]:
					solution = 1
					#listeElement.append([fait,"est dans la base de fait"])
				i=i+1
		for regles in BR:
			if regles == but.group('fait'):	
				size = len(BR[regles])
				for regle in BR[regles]:
					for elt in regle[-1]:
						j = 0
						while regle[j] != regle[-1]:
							k=0
							while k < len(regle[j]):
								tmpRegle = []
								for remplacer in regle[-1]:
									tmpRegle.append(remplacer.replace(regle[j][k],buts[k]))
									regle[-1] = tmpRegle
								k+=1
							j+=1
					contraintes.append(tmpRegle)
		for contrainte in contraintes:
#			for element
			l=0
			sup = 0
			while checkContradiction(contrainte) and l<len(contrainte):
				print(l)
				print(contrainte[l-sup])
				if checkContrainte(contrainte[l-sup]): 
					del contrainte[l-sup]
					sup+=1
				elif contrainte[l-sup] in BR:
					contrainte[l-sup] = appliquerRegles(contrainte[l-sup])
				l+=1
			print(contrainte)
			if contrainte == []:					
				solution = 2				
				#listeElement.append([fait,"est une solution ateigniable"])
				 
			 
			
	else : 
		solution = -1
		#listeElement = [["erreur de syntaxe dans la valeur interroger",entree.get()]]
	affichageConseil(solution)
	return

def chainageAvantL():
    listeElement = []
    #chainage avant en largeur a coder stocker les resultats dans listElement
    fait = re.compile(r'(?P<fait>\w+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')	
    but = re.match(fait,entree.get())
    #if but is not None:
        #traitementAvantL(but)
    traitementAvantL("aime('moi')")
    
    affichageConseil(listeElement)
    return

def traitementAvantL(monBut): #mon but est de la forme fait(valeur, autre)
    if checkContrainte(monBut) :
        return True
    else :

        for regles,conditions in BR.items() : #pour chaque regles
            regle = regles.split(",") #on met les conséquences sous forme de liste (avant ->)
            print("j'ai trouvé une conséquence")
            print(regle)
        
            variables = []
            faits = []        

            for groupeCondition in conditions:#pour chaque conditions (après ->)
                indiceVariable = 0
                for condition in groupeCondition: # on sépare les variables des conditions
                    if indiceVariable < len(regle): #si ce sont des variables on stock dans variables
                        variables.append(condition)
                    else :
                        faits.append(condition) #si ce sont des conditions on stock dans faits
                    indiceVariable += 1
            print("faits a tester :")
            print(faits)
            test =[]
            #il faut voir si les faits correspondent au but
            for elements in faits :
                for element in elements: # element ressemble a : fait(valeur)
                    liste = []
                    fait = re.compile(r'(?P<fait>[\!\w]+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*')
                    monFait = re.match(fait,element)   
                    if monFait is not None :
                        tmp = monFait.group('fait')
                        liste.append(tmp)#on extrait le nom du fait 
                        var = monFait.group('valeur').split()#on extrait la liste des valeurs






        

    return 




def chainageAvantP():
	listeElement = []
	fait = re.compile(r'(?P<fait>\w+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*;')	
	but = re.match(fait,entree.get())
	if but is not None:
		#chainage arrière stocker les resultats dans listElement
		print("ça passe")
	else : 
		listeElement = [["erreur de syntaxe dans la valeur interrogée",entree.get()]]
	affichageConseil(listeElement)
	return 

def checkContradiction(pile):
	for elem in pile:
		if elem[0][0] == "!":
			if elem[0] in BF:
				return False;
		else:
			tmp = "!"+elem[0]
			if tmp in BF:
				return False;
	#verifie qu'il n'y a pas de contradiction dans la base de connaissance	
	return True

def checkContrainte(contrainte): #retourne vrai si contrainte de la forme : fait(valeur) est dans la base de faits
	fait = re.compile(r'(?P<fait>[\!\w]+)\((?P<valeur>[\s\w\-]+(,[\s\w\-]+)*)\)\s*')	
	val = re.match(fait,contrainte)
	if val is not None:
		valeur = val.group('valeur')
		valeur = valeur.split(',')
		if val.group('fait') in BF : #si le fait existe
			if valeur in BF[val.group('fait')] : #si la valeur est dans la base de faits
				return True
	return False

def affichageConseil(solution):
	tmp = ""
	if solution == -1:
		tmp = "erreur de syntaxe"
	elif solution == 0:
		tmp = "le fait n'as pas de solution dans la base de connaissances"
	elif solution == 1:
		tmp = "le fait est bien dans la base de faits"
	elif solution == 2:
		tmp = "le fait est atteignable d'après la base de connaissances"
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

	l = LabelFrame(fenetre, text="base de connaissances", padx=20, pady=20)
	l.pack(fill="both", expand="yes")
	 
	content = StringVar()
	content.set("sélectionner une base de données")
	base = Label(l, textvariable=content,height=40,justify='left')
	base.pack(padx=10, pady=10)

	p = PanedWindow(fenetre, orient=HORIZONTAL)
	p.pack(expand=N, fill=BOTH, pady=2, padx=2)
	buttonOuvrir = Button(p,text="sélectionner base", command= openBase)
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
	value.set("champ de saisie pour l'ajout dans la base ou l'interroger")
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

