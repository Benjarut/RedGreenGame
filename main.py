import pygame,random
from pygame.locals import *

import gamelib

from elements import *

class RedGreenGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    RED = pygame.Color('red')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    def __init__(self):
        super(RedGreenGame, self).__init__('RedGreen',RedGreenGame.BLACK)
        self.buttonR = Button(color=RedGreenGame.RED,pos=(self.window_size[0]/2-100,400))
        self.buttonG = Button(color=RedGreenGame.GREEN,pos=(self.window_size[0]/2+100,400))
        self.score = 0
        self.hp = 100
        self.time = 0.0
        self.wait_press = 4.0
        self.alpha1 = Alphabet(pos=(self.window_size[0]/2-110,350))
        self.alpha2 = Alphabet(pos=(self.window_size[0]/2+90,350))
    


    def init(self):
        super(RedGreenGame, self).init()
        self.render_score()
        self.render_hp()
#        self.render_alphabet()

    def update(self):
    #    if self.is_key_press(K_RETURN):
    #        self.is_started = True
        self.check_key_pressed()
        if self.is_started:
            self.update_butt()
            self.update_alpha()

    def update_alpha(self):
        if self.time/1000.0 >=self.wait_press:
            self.alpha1.random_value()
            self.alpha2.random_value()
        if self.alpha1.value == self.alpha2.value:
            self.alpha2.random_value()
        

    def update_butt(self):
        self.time +=self.clock.get_time()
    #    print self.time/1000.0 ,self.wait_press 
        if self.time/1000.0 >= self.wait_press:
    #        print self.time
            if random.randint(0,1) == 0:
                self.buttonG.get_posR()
                self.buttonR.get_posL()
                self.update_alpha()

            else :
                self.buttonG.get_posL()
                self.buttonR.get_posR()
                self.update_alpha()

            self.time = 0

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
            self.buttonG.render(surface)
            self.alpha1.render(surface,RedGreenGame.BLACK)
            self.alpha2.render(surface,RedGreenGame.BLACK)

    def check_key_pressed(self):
        if self.is_key_press(K_RETURN):
            self.is_started = True
        alpha_tuple = (K_a,K_b,K_c,K_d,K_e,K_f,K_g,K_h,K_i,K_j,K_k,K_l,K_m,K_n,K_o,K_p,K_q,K_r,K_s,K_t,K_u,K_v,K_w,K_x,K_y,K_z)
        for i in alpha_tuple:
            if self.is_key_press(i):
                print i

def main():
    game = RedGreenGame()
    game.run()

if __name__ == '__main__':
    main()


        



