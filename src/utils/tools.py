#import heartrate; heartrate.trace(browser=True)
'''
import os
from pyheat import PyHeat
ph = PyHeat(os.path.realpath(__file__))
ph.create_heatmap()
# To output the heatmap as a file.
ph.show_heatmap('image_file.png')
'''
###tools.py
import math


# Creates a list of 1+(stop-start)/step elements equal to [start, start+step, ..., stop]
def intRange(start, stop, step=1):
	lint = [] 
	index = start
	for i in range(start, stop+1, step):
		lint.append(index)
		index += step
	return lint 


def str2list(_l):
    l = [0]*len(_l)    
    for i in range(0,len(_l)):
        l[i] = int(_l[i])
    return l


def listToString(_l):
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in _l:
        str1 += ele
 
    # return string
    return str1

def formatTextList(_str, _nformat, _endpoll):
    data = _str
    data = data.capitalize()
    data_list = list(data)
    lines = math.ceil(int(len(data_list)/_nformat))
    buffer_index = 0
    for line in range(1, lines+1):
        space_present = False
        space_index = -1 #not used if no spaces
        for i in range(_nformat*line-_endpoll+buffer_index, _nformat*(line)+buffer_index):
            if (data_list[i] == ' '): #look for the first space character between _endpoll ands the end of the line
                space_present = True
                space_index = i
                break
        #treatment
        if (space_present):
            #replace a space character with a \n 
            #Line breaks can be forced with the \\ sequence
            data_list[space_index] = '\n'
        else:
            #add a - and a \n
            if (line != lines): #if not the last line
                data_list.insert(_nformat*line+buffer_index, "-")
                #Line breaks can be forced with the \\ sequence
                data_list.insert(_nformat*line+1+buffer_index, "\n")
                buffer_index += 2
    
    data = listToString(data_list)
    return data

def row2expl(row):
    '''
    Name #0;
    Character #1;
    png_link #2;
    cardtext #3";
    ltext #4;
    lindus #5;
    leco #6;
    lpop #7;
    lmoney #8;
    lback #9;
    rtext #10;
    rindus #11;
    reco #12;
    rpop #13;
    rmoney #14;
    class #15;
    rback #16;
    '''
    #string format variables in int
    #format = n; lines end at n+1
    cardTextFormat = 100
    choiceTextFormat = 30
    backTextFormat = 40

    #test1 = ['test', 'test.png', '10', '10', '10', '10', '20', '20', '20', '20']
    data = row
    #string to int
    lData = str2list(data[5:9])
    rData = str2list(data[11:15])
    data[5:9] = lData
    data[11:15] = rData

    #string format
    data[3] = formatTextList(data[3], cardTextFormat, 2)
    data[4] = formatTextList(data[4], choiceTextFormat, 2)
    data[10] = formatTextList(data[10], choiceTextFormat, 2)
    data[9] = formatTextList(data[9], backTextFormat, 2)
    data[16] = formatTextList(data[16], backTextFormat, 2)
    return data

def csvFileCleaning(_csvFile):
    csvHeader = _csvFile[0]
    csvData = [0]*(len(_csvFile)-1)
    dataToClean = _csvFile[1:(len(_csvFile))]
    for j in range(0, len(dataToClean)):
        csvData[j] = row2expl(dataToClean[j])
    return csvHeader, csvData

def equations_mouvement(u, t, k, g):
    x, y, vx, vy = u
    dxdt = vx
    dydt = vy
    dvxdt = -k * vx
    dvydt = -g - k * vy
    return [dxdt, dydt, dvxdt, dvydt]

def decomposer_vitesse(angle, vitesse):
    vx = vitesse * math.cos(math.radians(angle))
    vy = vitesse * math.sin(math.radians(angle))
    return vx, vy

def calculer_angle_rotation(vx, vy, angle):
    if vx>0:
        c=math.atan(vx/vy)
        if vy>0:
            return math.degrees(c)%90
        elif vy<0:
             return math.degrees(c)%90+90
        else:
             return 90
    else:
        c=math.atan(vx/vy)
        if vy>0:
            return math.degrees(c)%90
        elif vy<0:
             return math.degrees(c)%90-90
        else:
             return -90

def findAllCharacters(_str, _ch):
    lindex = []
    for i in range(0, len(_str)-1):
        if (_str.find(_ch ,i, i+1) != (-1)):
            lindex.append(i)
    return lindex