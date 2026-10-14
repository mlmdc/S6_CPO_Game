import pyglet

class SoundManager:
    def __init__(self):
        self.player = pyglet.media.Player()
        self.sound = None
    def load_sound(self, sound_file):
        # Load the sound file
        self.sound = pyglet.media.load(sound_file, streaming=False)
        # Set the source for the player
        self.player.queue(self.sound)


    def play(self):
        # Play the loaded sound
        self.player.play()

    def stop(self):
        # Stop the player
        self.player.pause()

    def set_volume(self, volume):
        # Set the volume of the player
        self.player.volume = volume
    
    def set_looping(self, looping):
        # Set whether the sound should loop or not
        self.player.loop=looping
