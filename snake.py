from enum import Enum
from main import pixel

class direct(Enum):
    n = 0
    s = 1
    e = 2
    w = 3

class segment:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y

class snake:

    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y
        self.length = 1
        self.body = []
        self.body.append(self)
        self.direction = direct.n


    def move(self):
        

        if self.direction is direct.n:
           self.y += pixel
        elif self.direction is direct.s:
            self.y += (pixel * -1)
        elif self.direction is direct.e:
            self.x += pixel
        else:
            self.x += (pixel * -1)




    def grow(self):
        self.length += 1
        #self.body.append()
