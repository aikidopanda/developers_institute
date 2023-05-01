import os
import django
import sys
import random
import pygame
from pygame.locals import *
from random import uniform, randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homm_cardgame.settings')
django.setup()

from game.models import *
from main_things import main_menu

class Button_exit:

    def __init__(self, x, y, text, font, bg='darkblue', feedback = ''):
        self.font = font
        if feedback == '':
            self.feedback = 'text'
        else:
            self.feedback = feedback
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.text = self.font.render(text, 1, pygame.Color('White'))
        self.clicked = False
        self.size = self.text.get_size()
        self.surface = pygame.Surface()
        self.surface.fill(bg)

    def activate(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                sys.exit()
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        screen.blit(self.surface, (self.rect.x, self.rect.y))

def draw_circle():
    pos_x = uniform(100, 900)
    pos_y = uniform(100, 500)
    color = (randint(0,255),randint(0,255),randint(0,255))
    pygame.draw.circle(screen, color, (pos_x, pos_y), uniform(10, 50))

    
    

pygame.init()

CLOCK = pygame.time.Clock()
FPS = 30

bg = pygame.image.load('game/images/background.jpg')
test_img = pygame.image.load('game/images/Angel.webp')
font = pygame.font.SysFont('Arial', 20)

B = Button_exit(800, 400)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homm_cardgame.settings')
django.setup()

# from main_things import *

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

# screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH])
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

menurunning = True
gamerunning = False

while menurunning:
    screen.blit(bg, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    B.draw()

while gamerunning:
    screen.blit(bg, (0, 0))

    for j in range(2):
        for i in range(4):
            surf = pygame.Surface((87, 115))
            surf.fill((48,19,196))
            surf_center = (
                (960-surf.get_width()) + i * 100,
                (640-surf.get_height()) + j * 150,
            )
            screen.blit(surf, surf_center)
            rect = surf.get_rect()

    for j in range(2):
        for i in range(4):
            surf = pygame.Surface((87, 115))
            surf.fill((192,42,19))
            surf_center = (
                (960-surf.get_width()) + i * 100,
                (640-surf.get_height())-500 + j * 150,
            )
            screen.blit(surf, surf_center)
            rect = surf.get_rect()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    B.draw()

    

        
    # card = pygame.image.load('game/images/Pikeman.webp')
    # card_center = (
    #     (SCREEN_WIDTH-card.get_width())/3,
    #     (SCREEN_HEIGHT-card.get_width())/2,
    # )
    
    # screen.blit(card, card_center)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
