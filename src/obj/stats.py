import pyglet
import utils.cfg as cfg
import math

class Stats:
    def __init__(self, nom, image, image_path, value=50):
        self.nom = nom
        self.__value = value
        self.next_value=value

        self.image_path=image_path

        self.sprite = pyglet.sprite.Sprite(image)
        self.__redimensionner_sprite(cfg.largeur_ecran/3/4)
        self.sprite.y=4/5*cfg.hauteur_ecran+1/25*cfg.hauteur_ecran

        self.lowbackground=pyglet.shapes.Rectangle(x=cfg.largeur_ecran/3, y=4/5*cfg.hauteur_ecran+1/25*cfg.hauteur_ecran, width=cfg.largeur_ecran/3/4,height=cfg.largeur_ecran/3/4,color=(229,168,85))
        self.upbackground=pyglet.shapes.Rectangle(x=cfg.largeur_ecran/3, y=4/5*cfg.hauteur_ecran+1/25*cfg.hauteur_ecran, width=cfg.largeur_ecran/3/4,height=cfg.largeur_ecran/3/4,color=(150,96,42))
        self.view=pyglet.shapes.Circle(x=cfg.largeur_ecran/3, y=0.82*cfg.hauteur_ecran,radius=10,color=(229,168,85))
    def __str__(self):
        return f"Stat {self.__nom}, actual value = {self.__value}"
    
    def get_value(self):
        v= self.__value
        return v
    
    def set_value(self, value):
        self.__value = value

    def set_next_value(self, value):
        self.next_value = value

    def __redimensionner_sprite(self, taille):
        self.sprite.update(scale_x = (taille/self.sprite.width)
                        ,scale_y= (taille/self.sprite.height))

    def afficher_Stats(self, offset):
        self.lowbackground.height=self.__value/100*cfg.largeur_ecran/3/4
        self.lowbackground.x=cfg.largeur_ecran/3+cfg.largeur_ecran/3/4*offset
        self.lowbackground.draw()

        self.upbackground.y=4/5*cfg.hauteur_ecran+1/25*cfg.hauteur_ecran+self.lowbackground.height
        self.upbackground.height=(100-self.__value)/100*cfg.largeur_ecran/3/4
        self.upbackground.x=cfg.largeur_ecran/3+cfg.largeur_ecran/3/4*offset
        self.upbackground.draw()

        self.sprite.x=cfg.largeur_ecran/3+cfg.largeur_ecran/3/4*offset
        self.sprite.draw()

    def afficher_mod(self,offset,value, angle):
        self.view.x=cfg.largeur_ecran/3+cfg.largeur_ecran/3/4*offset+1/2*cfg.largeur_ecran/3/4
        if value !=0:
            self.view.opacity=int(abs(angle/cfg.angle_max_droit)*255)
            if abs(value)<10:
                self.view.radius=5
            elif abs(value)>=10 and abs(value)<20:
                self.view.radius=10
            elif abs(value)>=20:
                self.view.radius=15
            self.view.draw()

    def update(self):

        delta_value=0
        if self.__value<self.next_value:
            delta_value=2.5
        
        elif self.__value>self.next_value:
            delta_value=-2.5

        self.__value=delta_value+self.__value
        self.lowbackground.height=self.__value/100*cfg.largeur_ecran/3/4

        self.upbackground.y=4/5*cfg.hauteur_ecran+1/25*cfg.hauteur_ecran+self.lowbackground.height
        self.upbackground.height=(100-self.__value)/100*cfg.largeur_ecran/3/4



    def modifications(self, value):
        self.next_value = self.__value+value

    def check_max_min(self, fenetre):
        if ((self.__value >=100) or (self.__value <= 0)):
            return False
        
    def to_dict(self):
        return {
            'nom': self.nom,
            'imagepath':self.image_path,
            'value': self.get_value(),
        }

    @classmethod
    def from_dict(cls, data):
        stats = cls(
            nom=data['nom'],
            image=pyglet.image.load(data['imagepath']),
            image_path= data['imagepath'],
            value=data['value']
        )
        return stats