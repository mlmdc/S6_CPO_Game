### Display events
import utils.cfg as cfg
import pyglet
import main

# Fonction pour réinitialiser l'angle de rotation
def reinitialiser_rotation():
    cfg.angle_rotation = 0

# Fonction pour détecter le début du clic
@cfg.fenetre.event
def on_mouse_press(x, y, bouton, modifiers):
    if bouton == pyglet.window.mouse.LEFT:
        cfg.clic_en_cours = True
        if cfg.current_state==cfg.STATE_SETTINGS:
            cfg.settings_menu.screen_checkbox.on_click(x,y)
    cfg.start_x = x

# Fonction pour détecter le mouvement de la souris pendant le clic
@cfg.fenetre.event
def on_mouse_drag(x, y, dx, dy, boutons, modifiers):
    if cfg.current_state==cfg.STATE_GAME:
        if cfg.paused==False:
            if cfg.start_x is not None:
                delta_x = x - cfg.start_x
                # Déterminez la direction du glissement et ajustez l'angle de rotation
                if delta_x > 0:
                    cfg.angle_rotation += 1  # Rotation vers la droite
                elif delta_x < 0:
                    cfg.angle_rotation -= 1  # Rotation vers la gauche

                # Limitez l'angle de rotation à cfg.angle_max_droit degrés à droite
                if cfg.angle_rotation > cfg.angle_max_droit:
                    cfg.angle_rotation = cfg.angle_max_droit

                # Limitez l'angle de rotation à cfg.angle_max_gauche degrés à gauche
                if cfg.angle_rotation < cfg.angle_max_gauche:
                    cfg.angle_rotation = cfg.angle_max_gauche

    cfg.settings_menu.volume_slider.on_mouse_drag(x,y,0,0,0,0)
    cfg.settings_menu.sound_slider.on_mouse_drag(x,y,0,0,0,0)
    cfg.settings_menu.master_slider.on_mouse_drag(x,y,0,0,0,0)

# Fonction pour détecter la fin du clic
@cfg.fenetre.event
def on_mouse_release(x, y, bouton, modifiers):
    cfg.clic_release=True
    if bouton == pyglet.window.mouse.LEFT and cfg.clic_en_cours:
        cfg.clic_en_cours = False
        if cfg.current_state==cfg.STATE_GAME:
            if cfg.paused==False:
                if cfg.start_x +75< x:
                    # Glissement vers la droite
                    cfg.carte_actuelle.rightAction(cfg.stats)
                elif cfg.start_x -75> x:
                    # Glissement vers la gauche
                    cfg.carte_actuelle.leftAction(cfg.stats)
                reinitialiser_rotation()
            

@cfg.fenetre.event
def on_mouse_motion(x, y, dx, dy):
    update_mouse_position(x, y)

@cfg.fenetre.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE:
        if cfg.current_state==cfg.STATE_GAME:
            cfg.paused= not cfg.paused

            esc_sounds = cfg.sounds["epee"].play()
            esc_sounds.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)
        return pyglet.event.EVENT_HANDLED

    # Fonction pour mettre à jour l'affichage
def update(dt):
    cfg.fenetre.clear()
    if cfg.current_state == cfg.STATE_MAIN_MENU:
        cfg.main_menu.show()
        cfg.main_menu.handle_events()
    elif cfg.current_state == cfg.STATE_SETTINGS:
        cfg.settings_menu.show()
        cfg.settings_menu.handle_events()
        cfg.music_manager.set_volume((cfg.music_volume/100)*(cfg.master_volume/100))
        cfg.sound_manager.set_volume((cfg.sound_volume/100)*(cfg.master_volume/100))
    elif cfg.current_state == cfg.STATE_TRANSITION:
        cfg.transition_menu.show()
        cfg.transition_menu.update(0.1)
    elif cfg.current_state == cfg.STATE_GAME:
        verif=[True,True,True,True]
        for i in range(len(cfg.stats)):
            verif[i]=cfg.stats[i].check_max_min(cfg.fenetre)
        for i in range(len(verif)):
            if verif[i]==False:
                cfg.current_state=cfg.STATE_GAMEOVER
                pass
        cfg.game_menu.show()
    elif cfg.current_state == cfg.STATE_GAMEOVER:
        cfg.game_over_menu.handle_events()
        cfg.game_over_menu.show()
        cfg.carte_actuelle.is_backed=False
        for i in range(len(cfg.stats)):
            cfg.stats[i].set_value(50)
            cfg.stats[i].set_next_value(50)
    
    if cfg.paused==True:
        cfg.pause_menu.handle_events()
        cfg.pause_menu.show()

def update_mouse_position(x, y):
    cfg.mouse_x = x
    cfg.mouse_y = y