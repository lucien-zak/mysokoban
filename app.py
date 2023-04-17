import pygame
import random
from pygame.locals import *
from modules.player import Player
from modules.box import Box
from modules.utils import Utils


pygame.init()
screen = pygame.display.set_mode((1024, 720))
player = Player(100, 100, 50, 50, (255, 0, 0), screen)
box1 = Box(100, 200, 50, 50, 'yellow', screen)
box2 = Box(100, 300, 50, 50, (0, random.randrange(0,255), 255), screen)
box3 = Box(100, 400, 50, 50, (0, random.randrange(0,255), 255), screen)
box4 = Box(100, 500, 50, 50, (0, random.randrange(0,255), 255), screen)
box5 = Box(100, 600, 50, 50, (0, random.randrange(0,255), 255), screen)
boxes = [box1, box2, box3, box4, box5]


running = 1


while running:
    screen.fill((120, 120, 120))
    player.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        else:
            player.move(event)
    for box in boxes:
        box.draw()
        box.moveIfCollideWithOtherBoxList(boxes, event)
    # player.detectAndMoveIfCollide(boxes, event)
    Utils.detectCollideBoxes(boxes, player, event)    
    pygame.display.flip()
pygame.quit()
