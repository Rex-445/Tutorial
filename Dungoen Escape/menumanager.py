import pyglet





class MenuManager():
    def __init__(self):
        self.objects = []
        self.stage = "Menu"

    def AddObject(self, pos=(0,0), objectType="Image", stage="Menu",img="sprites/UI/Main_Menu/BG.png", size=[1,1]):
        self.objects.append(MenuObject(pos, objectType, img, size, stage))
        
    def update(self):
        for m in self.objects:
            m.update()
            m.sprite.draw()




class MenuObject():
    def __init__(self, pos=(0,0), objectType="Image", img="sprites/UI/Main_Menu/BG.png", size=[1,1], stage="Menu"):
        self.pos = list(pos)
        self.type = objectType
        self.sprite = pyglet.sprite.Sprite(pyglet.image.load(img))
        self.action = None
        self.size = size
        self.stage = stage

        self.defColor = (255,255,255)
        self.hoverColor = (255,255,0)

        #Set The Scale
        self.sprite.scale_x = self.size[0]
        self.sprite.scale_y = self.size[1]

    def update(self):
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]
        
    def IsHover(self, x, y):
        if self.type == "Button":
            if x < self.pos[0] + self.sprite.width and x > self.pos[0]:
                if y > self.pos[1] and y < self.pos[1] + self.sprite.height:
                    return True
            else:
                return False
        



menuManager = MenuManager()
menuManager.AddObject(pos=(0,0), objectType="Image", size=[.55, .65])
menuManager.AddObject(pos=(650,450), objectType="Image", size=[.7, .7], img="sprites/UI/Main_Menu/Title.png")
menuManager.AddObject(pos=(800,200), objectType="Button", size=[.7, .7], img="sprites/UI/Main_Menu/Start_Button.png", stage="Play")
menuManager.AddObject(pos=(800,100), objectType="Button", size=[.7, .7], img="sprites/UI/Main_Menu/Quit_Button.png", stage="Exit")
