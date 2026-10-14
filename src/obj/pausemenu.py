import pyglet
import utils.cfg as cfg

from obj.menu import Menu

class PauseMenu(Menu):
    def __init__(self):
        super().__init__()

        # Add the font file to the system
        pyglet.font.add_file("font/Unitblock-mLAwm.ttf")

        self.labels = []

        title_label = pyglet.text.Label('Pause',
                                        font_name='Unitblock',
                                        font_size=192,
                                        x=cfg.largeur_ecran // 2,
                                        y=(cfg.hauteur_ecran // 4) *3,
                                        anchor_x='center',
                                        anchor_y='center')
        
        play_label = pyglet.text.Label('Retour Menu Principal',
                                      font_name='Unitblock',
                                      font_size=72,
                                      x=cfg.largeur_ecran // 2,
                                      y=cfg.hauteur_ecran // 2,
                                      anchor_x='center',
                                      anchor_y='center')

        self.labels.extend([title_label, play_label])

        self.background = pyglet.shapes.Rectangle(x=2*cfg.largeur_ecran//7, y=cfg.hauteur_ecran/10, width=3*cfg.largeur_ecran//7, height=4*cfg.hauteur_ecran/5,color=(0,0,0))
        self.background.opacity=int(60/100*255)

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
        if choice == 'Retour Menu Principal':
            cfg.current_state = cfg.STATE_MAIN_MENU
            cfg.paused=False
            pause_sounds = cfg.sounds["epee"].play()
            pause_sounds.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)