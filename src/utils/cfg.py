#import heartrate; heartrate.trace(browser=True)
### config.py
import sys
import dep
#
if (dep.module_init() == 0): #if the module are functionals
	import pyglet
	import numpy
else :
	sys.exit()

import time
import cardlib
import obj.selector as selector
import obj.mainmenu as mainmenu
import obj.settingsmenu as settingsmenu
import obj.transitionmenu as transitionmenu
import obj.gamemenu as gamemenu
import obj.gameovermenu as gameovermenu
import obj.pausemenu as pausemenu
import utils.soundmanager as soundmanager


largeur_ecran = pyglet.canvas.get_display().get_default_screen().width
hauteur_ecran = pyglet.canvas.get_display().get_default_screen().height

# Crée une fenêtre Pyglet avec la résolution de l'écran
fenetre = pyglet.window.Window(width=largeur_ecran, height=hauteur_ecran, fullscreen=False)
cards = []
carte_actuelle = 0
stats = []
angle_rotation = 0

# Fonts
pyglet.font.add_file("font/Unitblock-mLAwm.ttf")
pyglet.font.add_file("font/NewAthleticM54-31vz.ttf")
pyglet.font.add_file("font/QuirkyBreweryRegular-X3wvo.ttf")
button_font = 'New Athletic M54'
title_font = 'New Athletic M54'
text_font = 'Unitblock'

# Variables pour suivre l'état du clic de souris
clic_en_cours = False
clic_release = False
start_x = 0
end_x = 0
mouse_x = 0
mouse_y = 0

# Variables pour suivre l'état de l'angle de rotation
angle_rotation = 0
angle_max_droit = 15
angle_max_gauche = -15
clk = []


# Variables pour suivre l'état du jeu
STATE_MAIN_MENU=0
STATE_SETTINGS=1
STATE_GAME=2
STATE_GAMEOVER=3
STATE_TRANSITION=4
current_state = None
next_state = None
paused = False

### cardlib.py
ref = time.time()
png = cardlib.createPNGlib()
end = time.time()
print("images_init :", end-ref)

cards = None
randomCards = None
compteur = 0

### selector.py
selector = selector.Selector() #selecteur avec liste vide

### thread.py
randomThread = None

### menu
main_menu = mainmenu.MainMenu()
settings_menu = settingsmenu.SettingsMenu()
transition_menu = transitionmenu.TransitionMenu()
game_menu = gamemenu.GameMenu()
game_over_menu= gameovermenu.GameOverMenu()
pause_menu= pausemenu.PauseMenu()

###Variable pour suivre l'état du son
music_volume = 50
sound_volume = 50
master_volume = 50


###Sound manager
sound_manager = soundmanager.SoundManager()

music_manager = soundmanager.SoundManager()

ref = time.time()
sounds = cardlib.createSoundLib()
end = time.time()
print("sounds_init :", end-ref)