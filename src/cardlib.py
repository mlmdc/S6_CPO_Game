#import heartrate; heartrate.trace(browser=True)

### cardlib.py

import pyglet
import utils.cfg as cfg
import obj.card as fcd
import csv
import utils.tools as tools
import os


#dictionnaire referancant les photos et leurs positions
#pour obtenir les images : cfg.cfg.pngDict[...]
def createPNGlib():
    files = os.listdir('png') #'png' = None if in png
    png = dict()
    for i in range(len(files)) : 
        png.update({files[i].rstrip('_.png') : pyglet.image.load("png/"+files[i])})
    return png

def createSoundLib():
	files = os.listdir('sounds') #'png' = None if in png
	sounds = dict()
	for i in range(len(files)) : 
		sounds.update({files[i].rstrip('_.mp3') : pyglet.media.load("sounds/"+files[i], streaming=False)})
	return sounds

def createCardLib():
	### Opening .csv and garnishing, then cleaning it
	with open("utils/cards_data.csv", mode = 'r', encoding='UTF-8', newline='') as file:  
      
		# reading the CSV file  
		csvReader = csv.reader(file, delimiter=';')  
		csvFile = []
		for row in csvReader:
			if (row[0] != "default"): #if the line is not edited
				csvFile.append(row)

	### cleaning
	csvHeader, csvData = tools.csvFileCleaning(csvFile)
	### dict creation
	cardict = dict ()
	for i in range(len(csvData)): ### for all files
		if (csvData[i][15]=="Card"): ### if the selected type is 'Card'
			cardict.update({csvData[i][0] : fcd.Card(nom=csvData[i][1], #title
												image=cfg.png[csvData[i][2].rstrip('_.png')], #image from
												imagepath=csvData[i][2],
												cardtext=csvData[i][3],
												ltext=csvData[i][4] ,
												rtext=csvData[i][10] ,
												actions=[csvData[i][5:9],csvData[i][11:15]],
												taille = 400,
												lback = csvData[i][9],
												rback = csvData[i][16]
												)})
	#print("\nCARDICT TEST : ",cardict)
	#del cardict["default"] #Removes the default key not meant to be played
	return cardict