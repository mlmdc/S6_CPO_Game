############
'''
Contains threads data, with constructed data
'''
############

import utils.cfg
import obj.thread as thr

#Fonction pour initialiser apres les cartes
def createThreadsData():
	data = dict() #dictionnaire agrémenté des listes de cartes en arbres binaires


	### Random Thread

	randomList = ["starterAlien", "alienD0", "alienD1", "alienD2", "alienG3", "alienG4", "alienD3","alienFinal"]


	### Thread Alien
	alienThread = [None]*31
	alienThread[0] = [cfg.cards["starterAlien"]]
	alienThread[2] = [cfg.cards["alienD0"], cfg.cards["alienD1"], cfg.cards["alienD2"]]
	alienThread[5] = [cfg.cards["alienG3"], cfg.cards["alienG4"]]
	alienThread[6] = [cfg.cards["alienD3"]]
	alienThread[14] = [cfg.cards["alienFinal"]]

	data.update({"alien" : thr.Thread(cardlist = alienThread)})
	### Thread YYY

	corruption = [None]*89

	corruption[0] = [cfg.cards["Corruption1"]]
	corruption[1] = [cfg.cards["Corruption2"]]
	corruption[4] = [cfg.cards["Corruption3"]]
	corruption[10] = [cfg.cards["Corruption4"]]
	corruption[3] = [cfg.cards["Corruption4"]]
	corruption[21] = [cfg.cards["Corruption5"]]
	corruption[7] = [cfg.cards["Corruption5"]]
	corruption[43] = [cfg.cards["Corruption6"]]
	corruption[15] = [cfg.cards["Corruption6"]]




	data.update({"corruption" : thr.Thread(cardlist = corruption)})


	### Thread CDM

	cdm = [None]*45

	cdm[0] = [cfg.cards["CDM1"]]
	cdm[1] = [cfg.cards["CDM2"]]
	cdm[4] = [cfg.cards["CDM3"]]
	cdm[10] = [cfg.cards["CDM4"]]
	cdm[21] = [cfg.cards["CDM5"]]

	data.update({"cdm" : thr.Thread(cardlist = cdm)})


	### Thread Technospatial

	technospatial = [None]*60

	technospatial[0] = [cfg.cards["Technospatial1"]]
	technospatial[2] = [cfg.cards["Technospatial2"]]
	technospatial[1] = [cfg.cards["Technospatial3"]]
	technospatial[3] = [cfg.cards["Technospatial4"]]
	technospatial[6] = [cfg.cards["Technospatial5"]]
	technospatial[13] = [cfg.cards["Technospatial6"]]
	technospatial[27] = [cfg.cards["Technospatial7"]]

	technospatial[4] = [cfg.cards["Technospatial2"]]
	technospatial[8] = [cfg.cards["Technospatial2"]]
	technospatial[14] = [cfg.cards["Technospatial2"]]
	technospatial[28] = [cfg.cards["Technospatial2"]]

	data.update({"technospatial" : thr.Thread(cardlist = technospatial)})

	### Thread Pastis

	pastix = [None]*100

	pastix[0] = [cfg.cards["Pastis1"]]
	pastix[2] = [cfg.cards["Pastis2"]]
	pastix[1] = [cfg.cards["Pastis3"]]
	pastix[4] = [cfg.cards["Pastis4"]]
	pastix[10] = [cfg.cards["Pastis5"]]

	data.update({"pastix" : thr.Thread(cardlist = pastix)})

	### Thread pandemie_mondiale
	'''
	pandemie = [None]*500

	pandemie[0]= [cfg.cards["pandemie_mondiale1"]]
	pandemie[1]= [cfg.cards["pandemie_mondiale2"]]
	pandemie[2]= [cfg.cards["pandemie_mondiale3"]]
	
	pandemie[3]= [cfg.cards["pandemie_mondiale4"]]
	pandemie[4]= [cfg.cards["pandemie_mondiale5"]]
	pandemie[5]= [cfg.cards["pandemie_mondiale6"]]
	
	pandemie[6]= [cfg.cards["pandemie_mondiale7"]]
	pandemie[7]= [cfg.cards["pandemie_mondiale8"]]
	pandemie[8]= [cfg.cards["pandemie_mondiale9"]]
	
	pandemie[9]= [cfg.cards["pandemie_mondiale10"]]
	pandemie[10]= [cfg.cards["pandemie_mondiale11"]]
	pandemie[11]= [cfg.cards["pandemie_mondiale12"]]

	pandemie[12]= [cfg.cards["pandemie_mondiale13"]]

	data.update({"pandemie" : thr.Thread(cardlist = pandemie)})

	'''

	return data

