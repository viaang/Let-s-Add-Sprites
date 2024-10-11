import pygame
import random


pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

RED = pygame.Color("red")
ORANGE = pygame.Color("orange")
PURPLE = pygame.Color("purple")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")
DARK_BLUE = pygame.Color("dark blue")


class Sprites(pygame.sprite.Sprite) :
    def __init__(self,width,height,color) :
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([1,2]),random.choice([1,2])]
    
    def update(self) :
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500 :
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 500 :
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit :
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKROUND_COLOR_CHANGE_EVENT))
    
    def color_change(self) :
        
        self.image.fill(random.choice([ORANGE,PURPLE,DARK_BLUE,BLACK,GREEN]))   
        
def back_change(self):
        global bg_color
        bg_color = random.choice([ORANGE,PURPLE,DARK_BLUE,BLACK,GREEN])

        
