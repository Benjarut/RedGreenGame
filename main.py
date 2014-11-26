import pygame
from pygame.locals import *

import gamelib

from elements import *

class RedGreenGame(gamelib.SimpleGame):
    time = 5
    BLACK = pygame.Color('black')
    RED = pygame.Color('red')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    def __init__(self):
        super(RedGreenGame, self).__init__('RedGreen',RedGreenGame.BLACK)
        self.buttonR = Button(color=RedGreenGame.RED,pos=(self.window_size[0]/2-100,400))
        self.buttonL = Button(color=RedGreenGame.GREEN,pos=(self.window_size[1]/2+200,400))
        self.score = 0
        self.hp = 100


    def init(self):
        super(RedGreenGame, self).init()
        self.render_score()
        self.render_hp()

    def update(self):
        if self.is_key_press(K_RETURN):
            self.is_started = True
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0,RedGreenGame.WHITE)

    def render_hp(self):
        if self.hp >=50 :
            self.hp_image = self.font.render("HP : %d"% self.hp ,1,RedGreenGame.GREEN)
        else :
            self.hp_image = self.font.render("HP : %d"% self.hp ,1,RedGreenGame.Red)
    def render(self, surface):
        if self.is_started:
            surface.blit(self.score_image,(10,10))
            surface.blit(self.hp_image,(400,10))
            self.buttonR.render(surface)
            self.buttonL.render(surface)

def main():
    game = RedGreenGame()
    game.run()

if __name__ == '__main__':
    main()


        





