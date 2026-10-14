import pyglet
import time
launch_time = time.time()
import init
import utils.cfg as cfg
import cardlib
import save


#fonction pour initialiser le jeu
def app_init():
    #display_init n'est pas utilisee ici
    ref = time.time()
    init.clock_init()
    end = time.time()
    print("clock_init :", end-ref)

    ref = time.time()
    init.menu_init()
    end = time.time()
    print("menu_init :", end-ref)

#def content_init():
    ### Content init
    ref = time.time()
    init.stats_init()
    end = time.time() 
    print("stats_init :", end-ref)
    
    ref = time.time()
    init.cards_init()
    end = time.time()
    print("cards_init :", end-ref)
    
    ref = time.time()
    init.thread_init()
    end = time.time()
    print("thread_init :", end-ref)
    
    ref = time.time()
    init.selector_init()
    end = time.time()
    print("selector_init :", end-ref)
    
    ref = time.time()
    init.music_init()
    end = time.time()
    print("music_init :", end-ref)

    cfg.has_init = True

    save.load_game()



# Lancer l'initialisation et boucle principale
if __name__ == "__main__":
    ### test for createCardLib

    app_init()
    #content_init()
    print("\ninit_time : ",time.time()-launch_time )
    pyglet.app.run(1/120)

