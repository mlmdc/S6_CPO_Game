import utils.cfg as cfg
import pyglet
from pyglet.shapes import Rectangle, Line

class Screen_Checkbox:
    def __init__(self, x, y, width, height, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.checked = False

    def draw(self):
        rectangle = Rectangle(self.x, self.y, self.width, self.height, color=(255, 255, 255))
        rectangle.draw()

        if self.checked:
            # Draw lines
            Line(self.x, self.y, self.x + self.width, self.y + self.height, color=(0, 0, 0)).draw()
            Line(self.x, self.y + self.height, self.x + self.width, self.y, color=(0, 0, 0)).draw()

        label = pyglet.text.Label(
            self.label,
            font_size=24,
            x=self.x + self.width + 5,
            y=self.y + self.height // 2,
            anchor_x='left',
            anchor_y='center'
        )
        label.draw()

    def on_click(self, x, y):
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.checked = not self.checked
            cfg.clic_release=False
            click_sounds = cfg.sounds["epee"].play()
            click_sounds.volume = (cfg.sound_volume/100)*(cfg.master_volume/100)
            
