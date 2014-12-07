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
        self.alphaR = Alphabet(pos=(self.window_size[0]/2-110,350))
        self.alphaG = Alphabet(pos=(self.window_size[0]/2+90,350))
        self.bg = Background()

    def init(self):
        super(RedGreenGame, self).init()
        self.score = 0
        self.hp = 100
        self.time = 0.0
        self.wait_press = 3.0
        self.combo = 0
        self.wait_press = 3.0
        self.speed_image = Image(pos = (600,200))
#        self.render_score()
#        self.render_hp()
#        self.render_alphabet()

    def update(self):
    #    if self.is_key_press(K_RETURN):
    #        self.is_started = True
    #    self.check_key_pressed()
        print self.wait_press   
        if self.is_started and not self.is_ended :
            self.bg.change_image(index = 1)
            self.play_game()
        if self.time/1000.0 >= self.wait_press:
            self.update_butt()
            self.hp -=25
            self.combo = 0
            self.time = 0
            self.wait_press = 3.0


    def update_alpha(self):
#        if self.time/1000.0 >=self.wait_press:
        self.alphaR.random_value()
        self.alphaG.random_value()
        if self.alphaR.value == self.alphaG.value:
            self.update_alpha()
        

    def update_butt(self):
    #    self.time +=self.clock.get_time()
    #    print self.time/1000.0 ,self.wait_press 
    #    if self.time/1000.0 >= self.wait_press:
    #        print self.time
        if random.randint(0,1) == 0:
            self.buttonG.get_posR()
            self.buttonR.get_posL()
            self.update_alpha()
            self.alphaG.get_posR()
            self.alphaR.get_posL()

        else :
            self.buttonG.get_posL()
            self.buttonR.get_posR()
            self.update_alpha()
            self.alphaG.get_posL()
            self.alphaR.get_posR()

        self.time = 0

    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0,RedGreenGame.WHITE)

    def render_hp(self):
        if self.hp >=50 :
            self.hp_image = self.font.render("HP : %d"% self.hp ,1,RedGreenGame.GREEN)
        else :
            self.hp_image = self.font.render("HP : %d"% self.hp ,1,RedGreenGame.RED)
        if self.hp <= 0:
            self.is_started = False
            self.is_ended = True
            self.bg.change_image(index = 2)
        
    def render_combo(self):
        self.combo_image = self.font.render("%d COMBOS "% self.combo,1,RedGreenGame.WHITE)
    def restart_game(self):
        self.hp = 100
        self.score = 0
        self.wait_press = 3.0

    def render(self, surface):
        self.bg.render(surface)
        if self.is_started:
            surface.blit(self.score_image,(10,10))
            surface.blit(self.hp_image,(400,10))
            self.buttonR.render(surface)
            self.buttonG.render(surface)
            self.alphaR.render(surface,RedGreenGame.BLACK)
            self.alphaG.render(surface,RedGreenGame.BLACK)
            
            if self.combo >= 10:
                surface.blit(self.combo_image,(400,100))
                if self.combo % 10 >= 0 and self.combo % 10 <= 2:
                    self.speed_image.render(surface)
                    
        if not self.is_started and self.is_ended : 
            self.end_score = pygame.font.SysFont("Tlwg Typist,BoldOblique",30).render("Your Score : %d "% self.score,1,RedGreenGame.WHITE)
            surface.blit(self.end_score,(400,250))          
    def speed_up(self):
        if self.wait_press >= 1.0:
            self.wait_press -= 0.5
        else :
            self.wait_press = 0.44

    def play_game(self):
        self.render_score()
        self.render_hp()
        self.render_combo()
        self.time += self.clock.get_time()
    
    def on_key_up(self, key):
        if self.is_started == False:
            if key == K_RETURN:
                self.is_started = True
                self.is_ended = False
                self.restart_game()
    #    print key
        alpha_tuple = (K_a,K_b,K_c,K_d,K_e,K_f,K_g,K_h,K_i,K_j,K_k,K_l,K_m,K_n,K_o,K_p,K_q,K_r,K_s,K_t,K_u,K_v,K_w,K_x,K_y,K_z)
        for i in alpha_tuple:
            if key == i:
#                print key,"2"
                self.check_hit(i)

    def check_hit(self,i):
    #    print chr(i)

        if chr(i) == self.alphaG.get_value():
            self.score += 5
            self.update_butt()
            self.combo += 1
            
            if self.combo == 50:
                if self.hp <= 90:
                    self.hp += 5
                else:
                    self.score += 30
        elif chr(i) == self.alphaR.get_value():
            self.hp -= 25
            self.update_butt()
            self.combo = 0
            self.wait_press = 3.0

        if self.combo % 10 == 0 and  self.combo > 0:
            self.speed_up()

def main():
    game = RedGreenGame()
    game.run()

if __name__ == '__main__':
    main()


        



