import pygame,random
from pygame.locals import *

class Button(object):

    def __init__(self,color,pos,radius = 70,appearTime=5):
        self.pos =pos
        self.color = color
        self.radius = radius
        self.appearTime = appearTime
    
    def get_color(self):
        self.color = 'red'
        return self.color

    def get_posR(self):
        self.pos = (300,400)

    def get_posL(self):
        self.pos = (500,400)

    def render(self,surface):
        pygame.draw.circle(surface,self.color,self.pos,self.radius,0)
""" 
class ButtonL(ButtonR):
    def get_pos(self):
        self.pos = (440,300)
        return self.pos

    def get_color(self):
        self.color = 'green'
        return self.color
"""
class Alphabet(object):
    def __init__(self,pos):
        self.pos = pos
        self.value = ''

    def random_value(self):
        value ='abcdefghijklmnopqrstuvwxyz'
        self.value = random.choice(value)
        value =self.value
        return value

    def position(self):
        return self.pos


