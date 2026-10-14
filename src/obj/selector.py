### Selector.py
# Python file defining the Selector class and associated functions
import random as rnd
import numpy as nmp
import utils.tools as tools


class Selector:

	__threadList = [] #Private attribute : list of Card class element
	# List instead of nmp.array() as it does not allow  
	#Initiator
	def __init__(self, cardList=[]):
		self.__cardList = cardList


	def __str__(self):
		return f"I am the selector and I contain {self.__threadList}"

	#get

	def getThreadList(self):
		tl = self.__threadList
		return tl

	def getThreadPriorities(self): #returns an array of each thread priority attribute, in order of linked thread
		tPrios =[]
		for thread in self.__threadList:
			tPrios.append(thread.getPriority())
		return nmp.array(tPrios)

	def getThreadWeight(self): #returns an array of each thread weight attribute, in order of linked thread
		tWei =[]
		for thread in self.__threadList:
			tWei.append(thread.getWeight())
		return nmp.array(tWei)
	
	def getThreadImportance(self): #returns an array of each thread importance attribute, in order of linked thread
		tImp =[]
		for thread in self.__threadList:
			tImp.append(thread.getImportance())
		return nmp.array(tImp)
	#set

	#For cardList, no specific set
	def threadClear(self):
		self.__threadList.clear()

	def threadPop(self,position=-1):
		self.__threadList.pop(position)

	def threadAppend(self,thread):
		self.__threadList.append(thread)

	def threadInsert(self,thread, position):
		self.__threadList.insert(position, thread)

	def threadIndex(self,thread):
		return self.__threadList.index(thread)


	def cardSelection(self):
		Card = None
		# Priority selection
		thrImportance = self.getThreadImportance()
		thrPriority = self.getThreadPriorities()
		thrWeight = self.getThreadWeight()
		if ((thrPriority<0).any()): #thrImportance < 0 changes element on the array by their boolean value respective to the test, any() returns true if true in array
			Card = (self.__threadList[list(thrPriority).index(min(thrPriority))]).cardGive()
			print("Test de la fonctionnalite priority et CardPop",Card)
			print("\nCard.cardPop() :", Card)
			print("\nself.__threadList[list(thrPriority).index(min(thrPriority))] : ", self.__threadList[list(thrPriority).index(min(thrPriority))]) #pops the last component (pos =-1) and returns the card
			#no importance addition
			#thread deletion in case of end
			if (self.__threadList[list(thrPriority).index(min(thrPriority))].getCardList() == []): #if empty list
				self.__threadList[list(thrPriority).index(min(thrPriority))].threadDell() #triggers the deletion of the thread, empties the slot in the list


		else:
			totWeight = 0
			for weight in thrWeight: #adds to the total weight every weights
				totWeight += weight

			randomWeight = nmp.round(thrWeight/totWeight, 5) #divides the array by the total weight, rounded to cull out the sparse infinite floats
			chosenThreadIndex = rnd.choices(
											tools.intRange(0, len(self.__threadList)-1), #[0, ..., len(self.__threadList)]
											weights = randomWeight, #takes as weight imput the list of weights respectives to elements
											k=1 #Only one iteration
											)[0] #reduces the output of choices from [int] to int
			## If selected, adds importance
			Card = (self.__threadList[chosenThreadIndex]).cardGive()
			#Deletion if end of the thread
			if (self.__threadList[chosenThreadIndex] == []):
				self.__threadList.index(chosenThread).threadDell()
			for threads in self.__threadList:

				threads.addImp(threads.getImportance()) 

		return Card #returns card
