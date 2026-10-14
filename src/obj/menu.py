class Menu:
    def __init__(self):
        self.labels = []

    def show(self):
        for label in self.labels:
            label.draw()

    def handle_events(self):
        pass