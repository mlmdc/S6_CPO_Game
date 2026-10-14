import pyglet
import save
import utils.cfg as cfg

from obj.menu import Menu

class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        # Add the font file to the system

        self.labels = []

        title_label_shadow = pyglet.text.Label('Reignib',
                                        font_name=cfg.title_font,
                                        font_size=192,
                                        x=cfg.largeur_ecran // 2+5,
                                        y=(cfg.hauteur_ecran // 4) *3+5,
                                        anchor_x='center',
                                        anchor_y='center',
                                        color=(0,0,0,255))
        
        play_label_shadow = pyglet.text.Label('Jouer',
                                      font_name=cfg.button_font,
                                      font_size=72,
                                      x=cfg.largeur_ecran // 2+5,
                                      y=cfg.hauteur_ecran // 2+5,
                                      anchor_x='center',
                                      anchor_y='center',
                                      color=(0,0,0,255))
        settings_label_shadow = pyglet.text.Label('Parametres',
                                           font_name=cfg.button_font,
                                           font_size=72,
                                           x=cfg.largeur_ecran // 2+5,
                                           y=cfg.hauteur_ecran // 2 - 90+5,
                                           anchor_x='center',
                                           anchor_y='center',
                                           color=(0,0,0,255))
        quit_label_shadow = pyglet.text.Label('Quitter',
                                       font_name=cfg.button_font,
                                       font_size=72,
                                       x=cfg.largeur_ecran // 2+5,
                                       y=cfg.hauteur_ecran // 2 - 180+5,
                                       anchor_x='center',
                                       anchor_y='center',
                                       color=(0,0,0,255))

        title_label = pyglet.text.Label('Reignib',
                                        font_name=cfg.title_font,
                                        font_size=192,
                                        x=cfg.largeur_ecran // 2,
                                        y=(cfg.hauteur_ecran // 4) *3,
                                        anchor_x='center',
                                        anchor_y='center')
        
        play_label = pyglet.text.Label('Jouer',
                                      font_name=cfg.button_font,
                                      font_size=72,
                                      x=cfg.largeur_ecran // 2,
                                      y=cfg.hauteur_ecran // 2,
                                      anchor_x='center',
                                      anchor_y='center')
        settings_label = pyglet.text.Label('Parametres',
                                           font_name=cfg.button_font,
                                           font_size=72,
                                           x=cfg.largeur_ecran // 2,
                                           y=cfg.hauteur_ecran // 2 - 90,
                                           anchor_x='center',
                                           anchor_y='center')
        quit_label = pyglet.text.Label('Quitter',
                                       font_name=cfg.button_font,
                                       font_size=72,
                                       x=cfg.largeur_ecran // 2,
                                       y=cfg.hauteur_ecran // 2 - 180,
                                       anchor_x='center',
                                       anchor_y='center')

        self.labels.extend([title_label_shadow,play_label_shadow,settings_label_shadow,quit_label_shadow, title_label, play_label, settings_label, quit_label])

        #image=pyglet.image.load("png/mainmenu.png")
        image = cfg.png["main_paysage"]

        self.background=pyglet.sprite.Sprite(image)
        ### Depreciated
        #self.background.width=cfg.largeur_ecran
        #self.background.height=cfg.hauteur_ecran
        self.background.update(scale_x=(cfg.largeur_ecran/self.background.width), 
                               scale_y=(cfg.hauteur_ecran/self.background.height))

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
        if choice == 'Jouer':
            cfg.next_state = cfg.STATE_GAME
            cfg.current_state = cfg.STATE_TRANSITION
        elif choice == 'Parametres':
            cfg.current_state = cfg.STATE_SETTINGS
        elif choice == 'Quitter':
            save.save_game()
            pyglet.app.exit()
        '''
        cfg.sound_manager.load_sound('sounds/epee.mp3')
        cfg.sound_manager.play()
        '''
        menu_sounds = cfg.sounds["epee"].play()
        menu_sounds.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)

