import pyglet, random, math, pickle
from pyglet.window import key, FPSDisplay, mouse
from menumanager import *




class GameWindow(pyglet.window.Window):
    #Initilize the game window
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_icon(pyglet.image.load("icon.png"))

    def on_draw(self):
        self.clear()
        menuManager.update()

            
    def update(self, dt):
        pass









#This checks if the code has been read
if __name__ == "__main__":
    window = GameWindow(1000, 700, "Dungoen Escape", resizable=False)
    pyglet.app.run()
