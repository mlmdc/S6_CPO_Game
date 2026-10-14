### INIT.py
import pyglet
import utils.cfg as cfg
import cardlib
import obj.stats as fst
import obj.thread as thr
import utils.display_events as dspe
import utils.thread_data


def cards_init():
	## Initialisation des cartes dans cfg.cards
	## load of pngs and cards
	cfg.cards = cardlib.createCardLib()
	### TEMPORAIRE
	
	cfg.randomCards = cardlib.createCardLib()
	### 
	'''
	cfg.carte_actuelle = rd.choice(list(cfg.cards.keys())) #choix de l'indice de la carte actuelle
	cfg.cards[cfg.carte_actuelle].showCard(cfg.fenetre,0)
	'''

def stats_init():
	industry = fst.Stats("INDUSTRY",cfg.png['icon_industry'],"png/icon_industry.png")
	people = fst.Stats("PEOPLE",cfg.png['icon_people'],"png/icon_people.png")
	climate = fst.Stats("CLIMATE",cfg.png['icon_tree'],"png/icon_tree.png")
	treasury = fst.Stats("TREASURY",cfg.png['icon_moulaga'],"png/icon_moulaga.png")
	cfg.stats= [industry, people, climate, treasury]
	for i in range(len(cfg.stats)): cfg.stats[i].set_value(50) #initial value

def clock_init():
    # Configurez la boucle de mise à jour
	cfg.clk=pyglet.clock.get_default()
	cfg.clk.schedule_interval(dspe.update, 1 / 120)
#prototype thread_init

def thread_init():
	## Creation des threads selon leurs classes respectives
	# THREADSDATA = thread_data.createThreadsData()

	cfg.randomThread = thr.RandomThread(_cardList = list(cfg.randomCards.values()))
	#aucune attribution des threads dans ce prototype 


#prototype selector_init

def selector_init(): #Le selecteur est unique et donc dans cfg
	#Ici, accroche des threads au selecteur
	#Ceux-ci doivent etre differents, ici pour test
	cfg.selector.threadAppend(cfg.randomThread)

	#Selection cfg.carte_actuelle
	cfg.carte_actuelle = cfg.selector.cardSelection()
	#cfg.carte_actuelle = rd.choice(list(cfg.cards.keys())) #choix de l'indice de la carte actuelle
	cfg.carte_actuelle.showCard(angle_rotation = 0)

def menu_init():
	cfg.current_state=cfg.STATE_MAIN_MENU
	#cfg.current_state=cfg.STATE_TRANSITION

def music_init():
	cfg.music_manager.load_sound('sounds/musique.mp3')
	#cfg.music_manager.load_sound(cfg.sounds["musique"])
	cfg.music_manager.set_volume((cfg.music_volume/100)*(cfg.master_volume/100))
	cfg.music_manager.set_looping(True)
	cfg.music_manager.play()