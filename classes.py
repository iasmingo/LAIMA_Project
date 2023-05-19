import pygame
from pygame.locals import *
import random


class Sorvete(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/abacaxi.png'))
        self.sprites.append(pygame.image.load('sprites/baunilha.png'))
        self.sprites.append(pygame.image.load('sprites/ceu_azul.png'))
        self.sprites.append(pygame.image.load('sprites/chocolate.png'))
        self.sprites.append(pygame.image.load('sprites/chocomenta.png'))
        self.sprites.append(pygame.image.load('sprites/creme.png'))
        self.sprites.append(pygame.image.load('sprites/limao.png'))
        self.sprites.append(pygame.image.load('sprites/morango.png'))
        self.sprites.append(pygame.image.load('sprites/uva.png'))

        self.atual = random.randint(0, 8)
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = random.randint(0, 570), 0
