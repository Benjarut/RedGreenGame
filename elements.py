import pygame,random
from pygame.locals import *

class Button(object):

    def __init__(self,color,pos,radius = 70):
        self.pos =pos
        self.color = color
        self.radius = radius
    
    def get_color(self):
        self.color = 'red'
        return self.color

    def get_posR(self):
        self.pos = (500,400)

    def get_posL(self):
        self.pos = (300,400)

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
#################################################
class Alphabet(object):
    def __init__(self,pos):
        self.pos = pos
        self.value = random.choice('abcdefghijklmnopqrstuvwxyz')

    def random_value(self):
        value ='abcdefghijklmnopqrstuvwxyz'
        self.value = random.choice(value)
    
    def get_value(self):
        return self.value

    def get_posL(self):
        self.pos = (280,350)
        
    def get_posR(self):
        self.pos = (490,350)
        
    def get_pos(self):
        return self.pos

    def render(self,surface,fontColor):

        self.alpha_image = pygame.font.SysFont("Padauk",60).render(self.value,1,fontColor)
        surface.blit(self.alpha_image,self.pos)
####################################################
class Background(object):
    def __init__(self):
        (self.x, self.y) = (0, 0)
        self.images = ('res/color_background.jpg',
                       'res/blue_bokeh.png',
                       'res/blue_bubbles.jpg') 
        self.pic = self.images[0]
        self.count = 0

    def change_image(self,index):
        self.pic = self.images[index]

    def render(self,surface):
        self.img = pygame.image.load(self.pic)
        self.img = pygame.transform.scale(self.img,(800,600)) 
        surface.blit(self.img,(self.x,self.y))

####################################################
class Image(object):
    def __init__(self,pos):
        (self.x,self.y) = pos
        self.pic = 'res/speedup.png'
        
    def render(self,surface):
        self.img = pygame.image.load(self.pic)
        surface.blit(self.img,(self.x,self.y))
