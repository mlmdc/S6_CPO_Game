# transitionmenu.py
from obj.menu import Menu
from utils.tools import decomposer_vitesse, equations_mouvement, calculer_angle_rotation
from scipy.integrate import odeint
import pyglet
import pyglet.graphics
import numpy as np
import utils.cfg as cfg
import random

class TransitionMenu(Menu):
    def __init__(self):
        # Paramètres initiaux
        self.x0, self.y0 = cfg.largeur_ecran//2, cfg.hauteur_ecran//2+50  # Position initiale
        self.angle_rotation = 75  # Angle de départ en degrés
        self.vitesse_initiale = 40  # Vitesse initiale

        v0x, v0y = decomposer_vitesse(self.angle_rotation, self.vitesse_initiale)

        self.g = 9.8  # Accélération due à la gravité
        self.k = 0.1  # Coefficient de frottement de l'air
        # Conditions initiales
        self.u0 = [self.x0, self.y0, v0x, v0y]

         # Temps
        self.temps = np.linspace(0, 30, 320)

        self.solution = odeint(equations_mouvement, self.u0, self.temps, args=(self.k, self.g))

        cote = 150
        self.carre = pyglet.shapes.Rectangle(x=self.x0, y=self.y0, width=cote, height=cote)
        self.carre.anchor_x=75
        self.carre.anchor_y=10

        self.indice_temps = 0

        # Ajoutez un label pour afficher le pourcentage de progression
        self.progress_label = pyglet.text.Label(
            '0%',
            font_name=cfg.text_font,
            font_size=18,
            x=cfg.largeur_ecran // 2,
            y=cfg.hauteur_ecran // 2-10,
            anchor_x='center',
            anchor_y='center'
        )

        self.progress_percentage = 0

    def show(self):
        self.carre.x, self.carre.y = self.u0[0], self.u0[1]  # Mise à jour des coordonnées du carré
        self.carre.draw()
        # Affiche le label du pourcentage de progression
        self.progress_label.draw()

    def update(self, dt):
        self.u0 = self.solution[self.indice_temps]
        self.angle_rotation = calculer_angle_rotation(self.u0[2], self.u0[3], self.angle_rotation)
        self.carre.rotation= self.angle_rotation
        if self.indice_temps<len(self.solution)-1:
            self.indice_temps +=1
        if self.carre.y<0:
            self.carre.x, self.carre.y = self.x0,self.y0
            self.carre.rotation=0

            self.indice_temps=0
            
            orientation=random.randint(0,1)
            self.angle_rotation = random.randrange(40,70,10)*orientation+ random.randrange(110,140,10)*(1-orientation)
            self.vitesse_initiale = random.randrange(80,110,10)

            v0x, v0y = decomposer_vitesse(self.angle_rotation, self.vitesse_initiale)

            self.u0 = [self.x0, self.y0, v0x, v0y]

            self.solution = odeint(equations_mouvement, self.u0, self.temps, args=(self.k, self.g))
            

        self.progress_percentage+=(random.randint(1,10)/100)*16
        self.progress_label.text = f'Loading... {int(self.progress_percentage)}%'
        if self.progress_percentage>=101:
            cfg.current_state=cfg.next_state
            self.progress_percentage=0

    def handle_events(self):
        pass
