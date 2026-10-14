### history.py

class History :

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

