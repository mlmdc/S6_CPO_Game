from obj.menu import Menu
import utils.cfg as cfg
import pyglet

class GameMenu(Menu):
    def __init__(self):
        super().__init__()
        self.bottom_rectangle = pyglet.shapes.Rectangle(x=cfg.largeur_ecran/3, y=0, width=cfg.largeur_ecran/3, height=cfg.hauteur_ecran/10,color=(110,79,31))
        self.middle_rectangle = pyglet.shapes.Rectangle(x=cfg.largeur_ecran/3, y=cfg.hauteur_ecran/10, width=cfg.largeur_ecran/3, height=(cfg.hauteur_ecran-cfg.hauteur_ecran/5-cfg.hauteur_ecran/10),color=(229,175,85))
        self.top_rectangle = pyglet.shapes.Rectangle(x=cfg.largeur_ecran/3, y=4/5*cfg.hauteur_ecran, width=cfg.largeur_ecran/3, height=cfg.hauteur_ecran/5,color=(110,79,31))
    
        #image=pyglet.image.load("png/Normal.png")
        image = cfg.png["Normal"]
        self.background=pyglet.sprite.Sprite(image)
        ### Depreciated
        #self.background.width=cfg.largeur_ecran
        #self.background.height=cfg.hauteur_ecran
        self.background.update(scale_x=(cfg.largeur_ecran/self.background.width), 
                               scale_y=(cfg.hauteur_ecran/self.background.height))
        
        self.labels=[]
        month_label = pyglet.text.Label('Mois :' +str(cfg.compteur),
                                       font_name=cfg.button_font,
                                       font_size=32,
                                       x=cfg.largeur_ecran *0.4,
                                       y=cfg.hauteur_ecran *0.075,
                                       anchor_x='center',
                                       anchor_y='center')
        self.labels.append(month_label)
    def show(self):
        self.labels[0].text='Mois :' +str(cfg.compteur)
        self.background.draw()
        self.bottom_rectangle.draw()
        self.middle_rectangle.draw()
        self.top_rectangle.draw()
        cfg.carte_actuelle.showCard(cfg.angle_rotation)
        for i in range(len(cfg.stats)):
            cfg.stats[i].afficher_Stats(i)
            cfg.stats[i].update()
        super().show()