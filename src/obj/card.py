#import heartrate; heartrate.trace(browser=True)

import pyglet
import utils.cfg as cfg
import math

class Card:
    def __init__(self, nom, image, imagepath, cardtext, ltext, rtext, actions, taille=400, lback=None, rback=None):
        self.imagepath=imagepath
        image.anchor_x = image.width // 2 
        image.anchor_y = int(0.1*image.height) 

        self.sprite = pyglet.sprite.Sprite(image)

        #imageback = pyglet.resource.image("png/arriere_clair.png")
        imageback = cfg.png["arriere_clair"]
        imageback.anchor_x=imageback.width // 2 
        imageback.anchor_y=int(0.1*image.height) 
        self.spriteback =  pyglet.sprite.Sprite(imageback)

        #imagedeck = pyglet.resource.image("png/arriere_sombre.png")
        imagedeck = cfg.png["arriere_sombre"]
        imagedeck.anchor_x=imagedeck.width // 2 
        imagedeck.anchor_y=int(0.1*image.height)
        self.spritedeck= pyglet.sprite.Sprite(imagedeck)

        self.__redimensionner_sprite(taille)

        self.spritedeck.update(x=cfg.largeur_ecran//2, y=(0.8*cfg.hauteur_ecran-0.9*self.sprite.height) // 2-30)
        

        self.actions = actions

        self.name = pyglet.text.Label(nom,
                                       font_name=cfg.text_font,
                                       font_size=24,
                                       x=cfg.largeur_ecran / 2,
                                       y=(0.15*cfg.hauteur_ecran),
                                       color=(0,0,0,255),
                                       anchor_x='center',
                                       anchor_y='center')
        
        self.cardtext = pyglet.text.Label(cardtext,
                                       font_name=cfg.text_font,
                                       font_size=30,
                                       x=cfg.largeur_ecran / 2-50,
                                       y=(0.7*cfg.hauteur_ecran),
                                       color=(0,0,0,255),
                                       anchor_x='center',
                                       anchor_y='center',
                                       width = 400,
                                       multiline = True)
        self.ltext= pyglet.text.Label(ltext,
                                       font_name=cfg.text_font,
                                       font_size=12,
                                       x=cfg.largeur_ecran / 2-taille/4,
                                       y=(0.8*cfg.hauteur_ecran-1.1*self.sprite.height) // 2+19/20*self.sprite.height,
                                       color=(255,255,255,255),
                                       anchor_x='center',
                                       anchor_y='center',
                                       width = 100,
                                       multiline = True)
        self.rtext= pyglet.text.Label(rtext,
                                       font_name=cfg.text_font,
                                       font_size=12,
                                       x=cfg.largeur_ecran / 2+taille/2,
                                       y=(0.8*cfg.hauteur_ecran-1.1*self.sprite.height) // 2+19/20*self.sprite.height,
                                       color=(255,255,255,255),
                                       anchor_x='center',
                                       anchor_y='center',
                                       width = 300,
                                       multiline = True)
        self.back_text= pyglet.text.Label("",
                                       font_name=cfg.text_font,
                                       font_size=20,
                                       x=cfg.largeur_ecran / 2,
                                       y=(0.8*cfg.hauteur_ecran-1.1*self.sprite.height) // 2+19/20*self.sprite.height,
                                       color=(0,0,0,255),
                                       anchor_x='center',
                                       anchor_y='center',
                                       width = 300,
                                       multiline = True)
        self.lcarre = pyglet.shapes.Rectangle(x=cfg.largeur_ecran / 2-self.sprite.width/2, y=(0.8*cfg.hauteur_ecran-1.1*self.sprite.height) // 2+4/5*self.sprite.height, width=self.sprite.width/2, height=self.sprite.height/5+25,color=(0,0,0))
        self.rcarre = pyglet.shapes.Rectangle(x=cfg.largeur_ecran/2+taille/2, y=(0.8*cfg.hauteur_ecran-1.1*self.sprite.height) // 2+4/5*self.sprite.height, width=self.sprite.width/2, height=self.sprite.height/5+25,color=(0,0,0))
        
        self.rcarre.anchor_x=self.rcarre.width

        self.angleancrer=math.atan((taille/2)/((4/5)*taille-image.anchor_y))
        self.angleancrel=math.atan((-taille/2)/((4/5)*taille-image.anchor_y))
        self.angletextl=math.atan((-taille/4)/((19/20)*taille-image.anchor_y))
        self.angletextr=math.atan((taille/4)/((19/20)*taille-image.anchor_y))

        self.distanceancre=math.sqrt(200**2+((4/5)*taille-image.anchor_y)**2)
        self.distancetext=math.sqrt(100**2+((19/20)*taille-image.anchor_y)**2)
        self.distancebacktext=(17/20)*taille-image.anchor_y

        self.back_card=pyglet.shapes.Rectangle(x=cfg.largeur_ecran/2+taille/2, y=(0.8*cfg.hauteur_ecran-1.1*self.sprite.height) // 2+4/5*self.sprite.height, width=taille, height=taille,color=(255,255,255))
        self.back_card.anchor_x= self.back_card.width/2
        self.back_card.anchor_y= int(0.1*image.height)
        self.back_card.x=cfg.largeur_ecran//2
        self.back_card.y=(0.8*cfg.hauteur_ecran-0.78*self.back_card.height) // 2

        self.rback=rback
        self.lback=lback

        self.is_backed=False


    def __str__(self):
        return f"Card {self.__nom}, associated actions {self.actions}"

    def getName(self):
        n = self.__nom
        return n

    def getActions(self):
        a = self.actions
        return a

    def showCard(self, angle_rotation):
        self.sprite.update(rotation=angle_rotation, x=cfg.largeur_ecran//2, y=(0.8*cfg.hauteur_ecran-0.9*self.sprite.height) // 2)
        self.spriteback.update(rotation=angle_rotation, x=cfg.largeur_ecran//2, y=(0.8*cfg.hauteur_ecran-0.9*self.sprite.height) // 2-30)
        self.back_text.rotation=angle_rotation
        
        lopacity=0
        ropacity=0
        rtextopacity=0
        ltextopacity=0

        if angle_rotation==0:
            lopacity=0
            ropacity=0
            rtextopacity=0
            ltextopacity=0
        elif angle_rotation>0:
            ropacity=angle_rotation/cfg.angle_max_droit*220
            lopacity=0
            rtextopacity=angle_rotation/cfg.angle_max_droit*255
            ltextopacity=0
            if self.is_backed == False:
                action_right = self.actions[1]
                for i in range(len(action_right)):
                    cfg.stats[i].afficher_mod(i,action_right[i],angle_rotation)
                
        elif angle_rotation<0:
            ropacity=0
            lopacity=angle_rotation/cfg.angle_max_gauche*220
            rtextopacity=0
            ltextopacity=angle_rotation/cfg.angle_max_gauche*255
            if self.is_backed == False:
                action_left = self.actions[0]
                for i in range(len(action_left)):
                    cfg.stats[i].afficher_mod(i,action_left[i],angle_rotation)
        anglerad=angle_rotation*math.pi/180
        
        xr=self.distanceancre*math.sin(self.angleancrer+anglerad)+cfg.largeur_ecran/2
        yr=self.distanceancre*math.cos(self.angleancrer+anglerad)+self.sprite.y
        
        self.rcarre.x=xr
        self.rcarre.y=yr
        self.rcarre.rotation=angle_rotation

        xl=self.distanceancre*math.sin(self.angleancrel+anglerad)+cfg.largeur_ecran/2
        yl=self.distanceancre*math.cos(self.angleancrel+anglerad)+self.sprite.y

        self.lcarre.x=xl
        self.lcarre.y=yl
        self.lcarre.rotation=angle_rotation

        xtextl=self.distancetext*math.sin(self.angletextl+anglerad)+cfg.largeur_ecran/2
        ytextl=self.distancetext*math.cos(self.angletextl+anglerad)+self.sprite.y


        xtextr=self.distancetext*math.sin(self.angletextr+anglerad)+cfg.largeur_ecran/2+self.sprite.width/4
        ytextr=self.distancetext*math.cos(self.angletextr+anglerad)+self.sprite.y

        xbacktextdistance= self.distancebacktext*math.sin(anglerad)+cfg.largeur_ecran/2
        ybacktextdistance= self.distancebacktext*math.cos(anglerad)+self.sprite.y

        self.ltext.x=xtextl
        self.ltext.y=ytextl
        self.ltext.opacity=ltextopacity

        self.rtext.x=xtextr
        self.rtext.y=ytextr
        self.rtext.opacity=rtextopacity

        self.back_text.x=xbacktextdistance
        self.back_text.y=ybacktextdistance

        self.lcarre.opacity=int(lopacity)
        self.rcarre.opacity=int(ropacity)

        self.spritedeck.draw()

        if self.is_backed==False:
            self.sprite.draw()
            self.lcarre.draw()
            self.rcarre.draw()
            
            self.ltext.draw()
            self.rtext.draw()
        else:
            self.spriteback.draw()
            self.back_text.draw()
            
        self.cardtext.draw()
        self.name.draw()

        
        
        #self.back_card.draw()

    def __redimensionner_sprite(self, taille):
        self.sprite.update(scale_x = (taille/self.sprite.width)
                        ,scale_y= (taille/self.sprite.height))
        self.spriteback.update(scale_x = (taille/self.spriteback.width)
                        ,scale_y= (taille/self.spriteback.height))
        self.spritedeck.update(scale_x = (taille/self.spritedeck.width)
                        ,scale_y= (taille/self.spritedeck.height))
    def rightAction(self, stats):
        '''
        cfg.sound_manager.load_sound('sounds/whoosh.mp3')
        cfg.sound_manager.play()
        '''
        right_sound = cfg.sounds["whoosh"].play()
        right_sound.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)
        cfg.clic_release=False
        action_right = self.actions[1]
        if self.rback=="None" or self.rback=="default rback" or self.rback=="Default rback":
            for i in range(len(action_right)):
                stats[i].modifications(action_right[i])
            cfg.carte_actuelle = cfg.selector.cardSelection()
            cfg.compteur+=1
        else:
            if self.is_backed==False:
                for i in range(len(action_right)):
                    stats[i].modifications(action_right[i])
                self.back_text.text=self.rback
                self.is_backed=True
            else:
                cfg.carte_actuelle = cfg.selector.cardSelection()
                self.is_backed=False
                cfg.compteur+=1

    
    def leftAction(self, stats):
        '''
        cfg.sound_manager.load_sound('sounds/whoosh.mp3')
        cfg.sound_manager.play()
        sound_volume = 50
        master_volume = 50
        '''
        left_sound = cfg.sounds["whoosh"].play()
        left_sound.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)
        cfg.clic_release=False
        action_left = self.actions[0]
        if self.lback=="None" or self.lback=="default lback" or self.lback=="Default lback":
            for i in range(len(action_left)):
                stats[i].modifications(action_left[i])
            cfg.carte_actuelle = cfg.selector.cardSelection()
            cfg.compteur+=1
        else:
            if self.is_backed ==False:
                for i in range(len(action_left)):
                    stats[i].modifications(action_left[i])
                self.back_text.text=self.lback
                self.is_backed=True
            else:
                cfg.carte_actuelle = cfg.selector.cardSelection()
                self.is_backed=False
                cfg.compteur+=1

    def to_dict(self):
        # Convert the Card instance to a dictionary
        return {
            'nom': self.name.text,
            'image': "png/"+self.imagepath,  # assuming the image path is a string
            'cardtext': self.cardtext.text,
            'ltext': self.ltext.text,
            'rtext': self.rtext.text,
            'actions': self.actions,
            'lback': self.lback,
            'rback': self.rback
        }

    @classmethod
    def from_dict(cls, data):
        # Create a new Card instance from a dictionary
        card = cls(
            nom=data['nom'],
            image=pyglet.image.load(data['image']),  # adjust as needed based on your image loading logic
            imagepath= data['image'],
            cardtext=data['cardtext'],
            ltext=data['ltext'],
            rtext=data['rtext'],
            actions=data['actions'],
            lback=data['lback'],
            rback=data['rback']
        )
        # Add other attributes as needed
        return card