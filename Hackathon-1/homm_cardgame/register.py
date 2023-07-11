import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1600, 900), pygame.SCALED)
pygame.display.set_caption('Heroes of Might and Magic card game')

bg = pygame.image.load('game/images/background.jpg')
input_font = pygame.font.SysFont('Arial', 28)

class Field:
    def __init__(self, field) -> None:
        self.field = field
        self.text = ''
        self.active = False
        self.color = pygame.Color('chartreuse4')

    def activate(self):
        self.active = True
        self.color = pygame.Color('lightskyblue3')

    def deactivate(self):
        self.active = False
        self.color = pygame.Color('chartreuse4')

name_text = ''
password_text = ''
email_text = ''

name_inp = Field(pygame.Rect(400,200,200,32))
password_inp = Field(pygame.Rect(400,300,200,32))
email_inp = Field(pygame.Rect(400,400,200,32))

field_passive = pygame.Color('chartreuse4')
field_active = pygame.Color('lightskyblue3')

running = True

while running:

    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            name_inp.deactivate()
            password_inp.deactivate()
            email_inp.deactivate()

            if name_inp.field.collidepoint(event.pos):
                name_inp.activate()
            elif password_inp.collidepoint(event.pos):
                password_inp.activate()
            elif email_inp.collidepoint(event.pos):
                email_inp.activate()
                






