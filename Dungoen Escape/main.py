import pyglet, random, math, pickle
from pyglet.window import key, FPSDisplay, mouse
from menumanager import *
from player import Player




class GameWindow(pyglet.window.Window):
    #Initilize the game window
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_icon(pyglet.image.load("icon.png"))

        self.player = Player(pos=(150,150))

            
    def update(self, dt):
        self.player.update(dt)

    def on_draw(self):
        self.clear()
        if menuManager.stage == "Menu":
            menuManager.update()

        if menuManager.stage == "Game":
            self.player.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.player.KeyDown("Left")
            
        if symbol == key.RIGHT:
            self.player.KeyDown("Right")

    def on_key_release(self, symbol, modifiers):
        #KeyUp
        if symbol == key.LEFT:
            self.player.KeyUp("Left")
            
        if symbol == key.RIGHT:
            self.player.KeyUp("Right")
    
    def on_mouse_press(self, x, y, button, modifiers):
        for b in menuManager.objects:
            if b.IsHover(x, y):
                if b.stage == "Exit":
                    self.close()
                if b.stage == "Play":
                    menuManager.stage = "Game"

    def on_mouse_motion(self, x, y, dx, dy):
        for b in menuManager.objects:
            if b.IsHover(x, y):
                b.sprite.color = b.hoverColor
            else:
                b.sprite.color = b.defColor
                









#This checks if the code has been read
if __name__ == "__main__":
    window = GameWindow(1000, 700, "Dungoen Escape", resizable=False)
    pyglet.clock.schedule_interval_soft(window.update, 1/60)
    pyglet.app.run()
