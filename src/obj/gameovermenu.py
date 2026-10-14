from obj.menu import Menu
import utils.cfg as cfg
import pyglet

class GameOverMenu(Menu):
    def __init__(self):
        super().__init__()
        label = pyglet.text.Label("YOU LOST",
                            font_name= cfg.title_font,
                            font_size=100,
                            x=cfg.fenetre.width//2, y=cfg.fenetre.height//2,
                            anchor_x='center', anchor_y='center')
        self.labels.append(label)

        back_label = pyglet.text.Label("Retour au Menu principal",
                            font_name= cfg.button_font,
                            font_size=25,
                            x=cfg.fenetre.width//2, y=cfg.fenetre.height//2-300,
                            anchor_x='center', anchor_y='center')
        self.labels.append(back_label)

        #image= pyglet.image.load("png/gameover.png")
        image = cfg.png["gameover"]
        self.background= pyglet.sprite.Sprite(image)
        ### Depreciated 
        #self.background.width=cfg.largeur_ecran
        #self.background.height=cfg.hauteur_ecran
        self.background.update(scale_x=(cfg.largeur_ecran/self.background.width), 
                               scale_y=(cfg.hauteur_ecran/self.background.height))
        self.background.opacity=25/100*255


    def show(self):
        self.background.draw()
        super().show()

    def handle_events(self):
        for label in self.labels:
            if label.x - label.content_width / 2 < cfg.mouse_x < label.x + label.content_width / 2 and \
                    label.y - label.content_height / 2 < cfg.mouse_y < label.y + label.content_height / 2:
                if cfg.clic_release:
                    self.handle_menu_choice(label.text)
                    cfg.clic_release=False

    def handle_menu_choice(self, choice):
        if choice == "Retour au Menu principal":
            cfg.current_state = cfg.STATE_MAIN_MENU
            over_sounds = cfg.sounds["epee"].play()
            over_sounds.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)