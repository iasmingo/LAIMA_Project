import pygame
from pygame.locals import *
from sys import exit
from classes import Sorvete

pygame.init()


largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Like Fun')
relogio = pygame.time.Clock()

x_jogador = 0
y_jogador = 0


todas_as_sprites = pygame.sprite.Group()
sorvete = Sorvete()
todas_as_sprites.add(sorvete)

while True:
    tela.fill((0, 0, 0))
    relogio.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    """if pygame.key.get_pressed()[K_RIGHT] and x < 600:
        x += 20
    if pygame.key.get_pressed()[K_LEFT] and x != 0:
        x -= 20"""

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()
