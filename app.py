import pygame
from pygame.locals import *
from modules.player import Player

pygame.init()
screen = pygame.display.set_mode((1024, 720))
player = Player(100, 100, 50, 50, (255, 0, 0))

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      player.move(event)

  screen.fill((120, 120, 120))
  player.draw(screen)
  pygame.display.flip()

pygame.quit()