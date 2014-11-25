import pygame
from pygame.locals import *

class ButtonR:

    def __init__(self,color,radius = 70,appearTime=5):
        self.pos =()
        self.color = color
        self.radius = radius
        self.appearTime = appearTime
    
    def get_color(self):
        self.color = 'red'
        return self.color

    def get_pos(self):
        self.pos = (200,300)
        return self.pos

    def render(self,surface):
        pos = self.get_pos()
        pygame.draw.circle(surface,self.color,pos,self.radius,0)
    
class ButtonL(ButtonR):
    def get_pos(self):
        self.pos = (440,300)
        return self.pos

    def get_color(self):
        self.color = 'green'
        return self.color





