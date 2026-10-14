### Thread.py
# Python file defining the thread class and associated functions

import random as rd
import utils.cfg as cfg

class Choice:

	def __init__(self, cardIndex, indexListRight, indexListLeft):
		self.__cardIndex = cardIndex #Private Int : The card index is the card that affects the lists 
		self.__indexListRight = indexListRight #Private List : The list of card indexes in the pool to insert when right choice
		self.__indexListLeft = indexListLeft #Private List : The list of card indexes in the pool to insert when left choice

	#get
	def getIndexListRight(self):
		ilr = self.__indexListRight
		return ilr

	def getIndexListLeft(self):
		ill = self.indexListLeft
		return ill

	def getCardIndex(self):
		index = self.__cardIndex
		return index

	#set
	def setCardIndex(self, newCI):
		self.__cardIndex = newCI

	def indexClear(self, list = "right"):
		if (list == "list"):
			self.__cardIndexRight.clear()
		elif (list == "pool"):
			self.__cardIndexLeft.clear()

	def indexPop(self, position=-1, list = "right"):
		if (list == "list"):
			card = self.__cardIndexRight.pop(position)
		elif (list == "pool"):
			card = self.__cardIndexLeft.pop(position)
		return card

	def indexAppend(self, card, list = "right"):
		if (list == "list"):
			self.__cardIndexRight.append(card)
		elif (list == "pool"):
			self.__cardIndexLeft.append(card)

	def indexInsert(self, card, position, list = "right"):
		if (list == "list"):
			self.__cardIndexRight.insert(position, card)
		elif (list == "pool"):
			self.__cardIndexLeft.insert(position, card)

	def indexIndex(self, card, list = "right"):
		if (list == "list"):
			return self.__cardIndexRight.index(card)
		elif (list == "pool"):
			return self.__cardIndexLeft.index(card)

	def applyCardChoice(self, choice, thread):
		for i in range(0,len(thread.getCardList())): #Transfer all cards from list to bin
			thread.cardAppend(thread.cardPop(list, list = "list")
				, list = "bin")


		thread.cardClear() #list is cardList, security clear

		if (choice == "Right"):
			for index in self.__indexListRight:
				thread.cardAppend(thread.getCardPool()[index] #From the pool, the card at the selected index
					, list = "list") #Explicit choice of thread.__cardList

		if (choice == "Left"):
			for index in self.__indexListLeft:
				thread.cardAppend(thread.getCardPool()[index] #From the pool, the card at the selected index
					, list = "list") #Explicit choice of thread.__cardList

		del self #Delete itself from the list as it accomplishes its task

class Thread:

	__cardList = [] #Private attribute : list of Card class element meant for stocking up all the cards that will be played
	__cardPool = [] #Private attribute : List of Card class elements meant for stocking up all the cards that can be played
	__cardBin = [] #Private attribute : List of Card class elements meant for trashed cards
	__choiceList = [] #Private attribute : List of Choice class elements 
	__priority = None #Private attribute : real double
	__weight = None #Private qttribute : real double
	__importance = None #Private attribute : real double

	'''##### thread revision #####
	La nouvelle méthode est la suivante (inspirée de python binarytree):
	1. __cardlist contient le paquet de cartes actuel, dont la derniere carte agit comme fin de branche
		Uniquement constitué d'objets cartes
	2. __cardPool contient la liste de la liste des cartes 
		ex : [[starter], [branche1, suivante, suivante, finale1], [branche2, finale2], [branche11], ....]
	3. __cardBin contient la liste des listes de cartes utilisés ou mis au rebut (dont le choix ne permet donc pas d'utiliser)

	L'arbre de choix se constitue donc comme ceci :

	i=0	:		[starter]
			/				|		
	2i : [branche1]		2i+1 : [branche2]

	Ainsi, faire un choix, à droite ou à gauche revient à faire ceci :

	1. __cardBin.append(__cardList)
	2. Si __cardList n'est pas vide, seul la première carte (dans l'execution) est vidée
	2bis. Si __cardList est vide apres passage :
		 __cardList = __cardPool[2*i+1] si gauche
				    = __cardPool[2*i+2] si droit
					Si l'objet __cardPool[index] est un objet None, alors l'arbre de choix s'arrete
	3. i = 2*i (+1 si droit)

	'''
	#Initiator
	def __init__(self, priority = -1, weight=2, importance=2, cardList=[], cardPool =[], cardBin =[], choiceList =[]):
		self.__cardList = cardList ### Last of the list is -1, the card intended to be used
		self.__cardPool = cardPool ###
		self.__cardBin = cardBin
		self.__index = 0 #initialisé à 0
		self.__choiceList = choiceList
		self.__priority = priority
		self.__weight = weight
		self.__importance = importance


	def __str__(self):
		return f"I contain {self.__cardList}, of priority number {self.__priority}, of weight {self.__weight}, of importance {self.__importance} and with the following priority {self.__priority}"

	#get

	def getCard(self, position=-1):
		if (position > (len(self.__cardList)-1)):
			return self.__cardList[(len(self.__cardList)-1)]
		else:
			return self.__cardList[position]

	def getCardList(self):
		cl = self.__cardList
		return cl

	def getPriority(self):
		p = self.__priority
		return p

	def getWeight(self):
		w = self.__weight
		return w

	def getImportance(self):
		i = self.__importance
		return i

	def getCardPool(self):
		p = self.__cardPool
		return p

	def getCardBin(self):
		p = self.__cardBin
		return p

	def getChoiceList(self):
		cl = self.__choiceList
		return cl
	#set

	#For cards lists, the default choice is the playing list
	#An by-default argument named 'list' gives a way to select the list to modify
	def cardClear(self, list = "list"):
		if (list == "list"):
			self.__cardList.clear()
		elif (list == "pool"):
			self.__cardPool.clear()
		elif (list == "bin"):
			self.__cardBin.clear()

	def cardPop(self, position=-1, list = "list"):
		if (list == "list"):
			card = self.__cardList.pop(position)
		elif (list == "pool"):
			card = self.__cardPool.pop(position)
		elif (list == "bin"):
			card = self.__cardBin.pop(position)

		return card

	def cardAppend(self, card, list = "list"):
		if (list == "list"):
			self.__cardList.append(card)
		elif (list == "pool"):
			self.__cardPool.append(card)
		elif (list == "bin"):
			self.__cardBin.append(card)

	def cardInsert(self, card, position, list = "list"):
		if (list == "list"):
			self.__cardList.insert(position, card)
		elif (list == "pool"):
			self.__cardPool.insert(position, card)
		elif (list == "bin"):
			self.__cardBin.insert(position, card)

	def cardIndex(self, card, list = "list"):
		if (list == "list"):
			return self.__cardList.index(card)
		elif (list == "pool"):
			return self.__cardPool.index(card)
		elif (list == "bin"):
			return self.__cardBin.index(card)

	def choiceClear(self):
		self.__cardList.clear()

	def choicePop(self, position=-1):
		print("Experimentation cardPop avant cardPop :", self.__choiceList, "len", len(self.__choiceList))
		card = self.__choiceList.pop(position)
		print("\nExperimentation cardPop :", card)
		return card

	def choiceAppend(self, card):
		self.__choiceList.append(card)

	def choiceInsert(self, card, position):
		self.__choiceList.insert(position, card)

	def choiceIndex(self, card):
		return self.__choiceList.index(card)

	def setWeight(self, __nW):
		self.__weight = __nW

	def setImportance(self, __nI):
		self.__importance = __nI

	def setPriority(self, __nP):
		self.__priority = __P 

	def addImp(self, __imp):
		self.__weight += __imp


	def cardGive(self):
		#give card
		Card = self.cardPop(list = "list")

		#index = self.cardIndex(Card, list = "pool")
		self.cardAppend(Card, list = "bin")
		return Card

	#subtitut la classe Choice
	def applyChoice(_choice):
		self.cardAppend(self.cardPop(0), "bin") #Transfere la première carte de la liste vers la bin
		if (len(self.__cardList) == 0):
			if (_choice == "Left"):
				index = 2*(self.__index)+1 #change l'index vers la suivante

			else: #if (_choice == "Right"):
				index = 2*(self.__index)+2 #change l'index vers la suite droite
			
			if (self.__cardPool[self.__index] == None): #Si la suite est None 
				self.threadDell() #Alors suppression du thread par lui même
			else: #Si ce n'est pas le cas
				self.__cardList = self.__cardPool[self.__index] #charge la liste de carte suivante
		
	## Deletion of the class
	def threadDell(self):
		del self


### Extended class NarrativeThread from Thread

class NarrativeThread(Thread): #With priority defined by default as -1, contains pre-determined card set

	__cardList = [] #Private attribute : list of Card class element
	__cardPool = [] #Private attribute : List of Card class elements meant for stocking up all the cards that can be played
	__cardBin = [] #Private attribute : List of Card class elements meant for trashed cards
	__choiceList = []
	__priority = None #Private attribute : real double
	__weight = None #Private qttribute : real double
	__importance = None #Private attribute : real double

	def __init__(self, _priority = -1, _weight=1, _importance=1, _cardList=[], _cardPool=[], _cardBin=[], _choiceList=[]):
		Thread.__init__(self,_priority, _weight, _importance, _cardList, _cardPool, _cardBin, _choiceList)

class RandomThread(Thread):

	__cardList = [] #Private attribute : list of Card class element
	__cardPool = [] #Private attribute : List of Card class elements meant for stocking up all the cards that can be played
	__cardBin = [] #Private attribute : List of Card class elements meant for trashed cards
	__priority = None #Private attribute : real double
	__weight = None #Private qttribute : real double
	__importance = None #Private attribute : real double

	def __init__(self, _priority = 1, _weight=1, _importance=3, _cardList=[], _cardPool=[], _cardBin=[]):
		Thread.__init__(self,_priority, _weight, _importance, _cardList, _cardPool, _cardBin)

	def cardShuffling(self):
		self.__cardList = rd.shuffle(self.__cardList)

	def cardRandom(self): #Goal is to keep the deck refilled when used
		self.cardPop()
		self.cardInsert(rd.choice(blankCards) , 0) #Insert at 0 pos a card from the card pool

	def cardGive(self):
		Card = self.cardPop(list = "list")
		#index = self.cardIndex(Card, list = "pool")
		#self.cardAppend(getCardPool()[index], list = "bin")
		
		#insert at first position a card from the random cards pool
		self.cardInsert(cfg.randomCards[rd.choice(list(cfg.randomCards.keys()))], position=0)
		return Card


class MissionThread(Thread): #By default non callable by the selector (weight = 0), called by function

	__cardList = [] #Private attribute : list of Card class element
	__cardPool = [] #Private attribute : List of Card class elements meant for stocking up all the cards that can be played
	__cardBin = [] #Private attribute : List of Card class elements meant for trashed cards
	__choiceList = []
	__priority = None #Private attribute : real double
	__weight = None #Private qttribute : real double
	__importance = None #Private attribute : real double

	def __init__(self, _priority = 1, _weight=0, _importance=0, _cardList=[], _cardPool=[], _cardBin=[], _choiceList=[]):
		Thread.__init__(self,_priority, _weight, _importance, _cardList, _cardPool, _cardBin, _choiceList)

	def callThread(self):
		self.__priority = -2

class EndsThread(Thread):

	__cardList = [] #Private attribute : list of Card class element, predefined cards
	__cardPool = [] #Private attribute : List of Card class elements meant for stocking up all the cards that can be played
	__cardBin = [] #Private attribute : List of Card class elements meant for trashed cards
	# No need to use Choice class elements
	__priority = None #Private attribute : real double
	__weight = None #Private qttribute : real double
	__importance = None #Private attribute : real double

	def __init__(self, _priority = 1, _weight=0, _importance=0, _cardList=[], _cardPool=[], _cardBin=[]):
		Thread.__init__(self,_priority, _weight, _importance, _cardList, _cardPool, _cardBin)

	def callEnd(self):
		self.setPriority = -3
		#if conditions =>
			#return specific card
