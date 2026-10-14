from obj.card import Card
import utils.cfg as cfg

class NarrativeCard(Card):
    def __init__(self, nom, image, cardtext, ltext, rtext, actions=None, taille=400, lback=None, rback=None, nextcard=None):
        super.__init__(self,nom,image,cardtext, ltext, rtext, actions, taille, lback, rback)

        self.nextcard=nextcard

    def rightAction(self, stats):
        cfg.sound_manager.play_sound('whoosh.mp3',2)
        cfg.clic_release=False
        if self.actions!=None:
            action_right = self.actions[1]
            if self.rback==None:
                for i in range(len(action_right)):
                    stats[i].modifications(action_right[i])
                cfg.carte_actuelle = self.nextcard
            else:
                if self.is_backed==False:
                    for i in range(len(action_right)):
                        stats[i].modifications(action_right[i])
                    self.back_text.text=self.rback
                    self.is_backed=True
                else:
                    cfg.carte_actuelle = self.nextcard
                    self.is_backed=False
        else:
            if self.rback==None:
                cfg.carte_actuelle = self.nextcard
            else:
                if self.is_backed==False:
                    self.back_text.text=self.rback
                    self.is_backed=True
                else:
                    cfg.carte_actuelle = self.nextcard
                    self.is_backed=False
    
    def leftAction(self, stats):
        cfg.sound_manager.play_sound('whoosh.mp3',2)
        if self.actions!=None:
            cfg.clic_release=False
            action_left = self.actions[0]
            if self.lback==None:
                for i in range(len(action_left)):
                    stats[i].modifications(action_left[i])
                cfg.carte_actuelle = self.nextcard
            else:
                if self.is_backed ==False:
                    for i in range(len(action_left)):
                        stats[i].modifications(action_left[i])
                    self.back_text.text=self.lback
                    self.is_backed=True
                else:
                    cfg.carte_actuelle = self.nextcard
                    self.is_backed=False
        else:
            if self.lback==None:
                cfg.carte_actuelle = self.nextcard
            else:
                if self.is_backed==False:
                    self.back_text.text=self.lback
                    self.is_backed=True
                else:
                    cfg.carte_actuelle = self.nextcard
                    self.is_backed=False
