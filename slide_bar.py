import primitives
from primitives import *

class SlideBar:

    back_layer = screen.subsurface(pygame.Rect(x, y, x + size, y + size))

    def __init__(self, x=0, y=0, size=255, scroll_size=1, color=foreground):
        self.x = x
        self.y = y
        self.size = size
        self.scroll_size = scroll_size
        self.color = color
        self.index = 0


    def add():
        line(self.x, self.y, self.x + self.size, self.y, self.foreground, back_layer)
        for i in range(5):
            circulo(self.x + self.index, i + 1, back_layer)
        
    def slide(index):
        self.index = index
         

