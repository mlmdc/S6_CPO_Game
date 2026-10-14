import utils.cfg as cfg
import pyglet
from pyglet.gui.widgets import Slider

class Volume_Slider(Slider):
    def __init__(self, x, y, base, knob, edge=0, batch=None, group=None):
        super().__init__(x, y, base, knob, edge, batch, group)
        self.value=50
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # Check if the slider is active (in the SettingsMenu state)
        if cfg.current_state == cfg.STATE_SETTINGS:
            # Update the knob position based on mouse drag
            if x>self.x-10 and x<(self.x+self.width+10):
                if y>self.y and y<(self.y+self.height):
                    self.value = min(max(((x-self.x)/ self.width)*100,0),100)
                    cfg.clic_release=False

            

