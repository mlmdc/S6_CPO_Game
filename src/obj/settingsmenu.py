# settingsmenu.py
from obj.menu import Menu
from obj.volumeslider import Volume_Slider
from obj.screencheckbox import Screen_Checkbox
import pyglet
import utils.cfg as cfg

class SettingsMenu(Menu):
    def __init__(self):
        self.slider_batch = pyglet.graphics.Batch()
        '''
        base = pyglet.resource.image("png/angry_man1.png")
        knob = pyglet.resource.image("png/rnd1_ttsicon_00001_.png")
        '''
        base = pyglet.resource.image("png/slider.png")
        knob = pyglet.resource.image("png/slider_choice.png")

        base.width = 600
        base.height = 20
        knob.width = 10
        knob.height = 30

        self.volume_slider = Volume_Slider(
            cfg.largeur_ecran // 2 - 300, cfg.hauteur_ecran // 2 - 50,
            base=base, knob=knob, batch=self.slider_batch
        )
        self.sound_slider = Volume_Slider(
            cfg.largeur_ecran // 2 - 300, cfg.hauteur_ecran // 2 + 50,
            base=base, knob=knob, batch=self.slider_batch
        )

        self.master_slider = Volume_Slider(
            cfg.largeur_ecran // 2 - 300, cfg.hauteur_ecran // 2 + 150,
            base=base, knob=knob, batch=self.slider_batch
        )

        self.labels = []

        back_label = pyglet.text.Label('Retour',
                                       font_name=cfg.button_font,
                                       font_size=36,
                                       x=cfg.largeur_ecran // 2,
                                       y=cfg.hauteur_ecran // 2 - 100,
                                       anchor_x='center',
                                       anchor_y='center')
        self.labels.append(back_label)
        
        volume_label = pyglet.text.Label(
            f'Music Volume: {int(self.volume_slider.value)}%',
            font_name=cfg.text_font,
            font_size=24,
            x=cfg.largeur_ecran // 2,
            y=cfg.hauteur_ecran // 2,
            anchor_x='center',
            anchor_y='center'
        )

        self.labels.append(volume_label)

        sound_label = pyglet.text.Label(
            f'Sound Volume: {int(self.volume_slider.value)}%',
            font_name=cfg.text_font,
            font_size=24,
            x=cfg.largeur_ecran // 2,
            y=cfg.hauteur_ecran // 2+100,
            anchor_x='center',
            anchor_y='center'
        )

        self.labels.append(sound_label)

        master_label = pyglet.text.Label(
            f'Sound Volume: {int(self.volume_slider.value)}%',
            font_name=cfg.text_font,
            font_size=24,
            x=cfg.largeur_ecran // 2,
            y=cfg.hauteur_ecran // 2+200,
            anchor_x='center',
            anchor_y='center'
        )

        self.labels.append(master_label)

        self.screen_checkbox=Screen_Checkbox(cfg.largeur_ecran // 2 - 100, cfg.hauteur_ecran // 2 +250, 40, 40, "Fullscreen")

        #image=pyglet.image.load("png/mainmenu.png")
        image = cfg.png["mainmenu"]

        self.background=pyglet.sprite.Sprite(image)
        ### Depreciated
        #self.background.width=cfg.largeur_ecran
        #self.background.height=cfg.hauteur_ecran
        self.background.update(scale_x=(cfg.largeur_ecran/self.background.width), 
                               scale_y=(cfg.hauteur_ecran/self.background.height))
        self.background.opacity=25/100*255
        
    def show(self):
        self.background.draw()
        # Afficher les labels
        super().show()

        # Show the volume slider
        self.slider_batch.draw()
        self.screen_checkbox.draw()

    def handle_events(self):
        # Gérez les événements spécifiques au menu Paramètre ici
        for label in self.labels:
            # Vérifiez si le curseur est sur un label et si l'utilisateur clique
            if label.x - label.content_width / 2 < cfg.mouse_x < label.x + label.content_width / 2 and \
                    label.y - label.content_height / 2 < cfg.mouse_y < label.y + label.content_height / 2:
                if cfg.clic_release:
                    self.handle_menu_choice(label)
                    cfg.clic_release = False
        cfg.music_volume=self.volume_slider.value
        cfg.sound_volume=self.sound_slider.value
        cfg.master_volume=self.master_slider.value
        self.labels[1].text = f'Music Volume: {int(self.volume_slider.value)}%'
        self.labels[2].text = f'Sound Volume: {int(self.sound_slider.value)}%'
        self.labels[3].text = f'Master Volume: {int(self.master_slider.value)}%'

        if self.screen_checkbox.checked == True:
            cfg.fenetre.set_fullscreen(True)
        else:
            cfg.fenetre.set_fullscreen(False)

    def handle_menu_choice(self, choice):
        if choice.text == 'Retour':
            cfg.current_state = cfg.STATE_MAIN_MENU
            settings_sounds = cfg.sounds["epee"].play()
            settings_sounds.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)
