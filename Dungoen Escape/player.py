import pyglet, random, math







class Player():
    def __init__(self, pos=(0,0), size=[1,1]):
        self.pos = list(pos)
        self.action = 0
        self.frame = 0
        self.cell = []
        self.size = [1,1]

        #Movement Variables
        self.direction = 1
        self.speed = 100
        self.left = False
        self.right = False
        
        #Animations
        self.idle = self.__init__self__(7, 5, 256, 256, "Sprites/Characters/Player/Idle.png")
        self.walk = self.__init__self__(5, 4, 256, 256, "Sprites/Characters/Player/Walk.png")
        self.run = self.__init__self__(8, 3, 256, 256, "Sprites/Characters/Player/Run.png")

        self.sprite = pyglet.sprite.Sprite(self.idle[0])


        self.RemoveFrame(1, self.idle)
        self.RemoveFrame(2, self.run)
        
    def RemoveFrame(self, amount, frame):
        for i in range(amount):
            frame.remove(frame[-1])


    def KeyDown(self, direction):
        if direction == "Left":
            self.left = True
            self.direction = -1
            
        if direction == "Right":
            self.right = True
            self.direction = 1

    def KeyUp(self, direction):
        if direction == "Left":
            self.left = False
            self.action = 0
            
        if direction == "Right":
            self.right = False
            self.action = 0

    #function was made to make GameObject's Initilization easier       
    def __init__self__(self, row, col, width, height, img):
        img = pyglet.image.load(img)
        sprite_sheet = pyglet.image.ImageGrid(img, col, row, item_width=width, item_height=height)

        cell = sprite_sheet
        counting = len(cell)
        new_cell = []
        for d in range(col):
            counting -= row
            for n in range(row):
                new_cell.append(cell[counting + n])
        return new_cell

    def Movement(self, dt):
        if self.left:
            self.pos[0] -= self.speed * dt
            self.action = 2
            
        if self.right:
            self.pos[0] += self.speed * dt
            self.action = 2
            
    def update(self, dt):
        #Idle
        if self.action == 0:
            self.cell = self.idle

        #Walking
        if self.action == 1:
            self.cell = self.walk

        #Running
        if self.action == 2:
            self.cell = self.run

        
        self.frame += 30 * dt
        if int(self.frame) >= len(self.cell):
            self.frame = 0

        self.Movement(dt)


    def draw(self):
        self.sprite = pyglet.sprite.Sprite(self.cell[int(self.frame)])
        self.sprite.scale_x = self.size[0] * self.direction
        #Update Positions
        self.sprite.x = self.pos[0]
        self.sprite.y = self.pos[1]
        if self.direction == -1:
            self.sprite.x += 220
        
        self.sprite.draw()







