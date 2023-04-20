import pygame
import random
from pygame.locals import *
from modules.player import Player
from modules.box import Box
from modules.wall import Wall
from modules.utils import Utils
from modules.hole import Hole


pygame.init()
WIDTH = 1024
HEIGHT = 720
pygame.display.set_caption('Sokoban')
MAPS = [
    ['W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'H', 'P', '.', '.', 'W'],
    ['W', 'B', 'B', '.', '.', 'W'],
    ['W', '.', 'H', '.', '.', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W'],

]
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def generateMaps(MAPS):
    nbRow, nbCol = 0, 0
    walls, boxes, holes = [], [], []
    for row in MAPS:
        nbRow += 1
        nbCol = 0
        for char in row:
            nbCol += 1
            if char == 'W':
                print('W', nbRow)
                wall = Wall((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50, 'black', screen)
                walls.append(wall)
            if char == 'B':
                box = Box((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50, (0, random.randrange(0, 255), 255), screen)
                boxes.append(box)
            if char == 'P':
                player = Player((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50, (255, 0, 0), screen)
            if char == 'H':
                hole = Hole((nbCol - 1) * 50, (nbRow - 1) * 50, 50, screen)
                holes.append(hole)
    return nbRow, nbCol, walls, boxes, holes, player


nbRow, nbCol, walls, boxes, holes, player = generateMaps(MAPS)

running = 1

boxInHole = 0


while running:
    screen.fill((120, 120, 120))
    player.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        else:
            player.move(event)
    for hole in holes:
        hole.draw()
        if hole.boxIsOnHole(boxes):
            boxInHole += 1
            if boxInHole == len(boxes):
                print('You win')
                running = 0    
    for wall in walls:
        wall.draw()
    for box in boxes:
        box.draw()
        box.moveIfCollideWithOtherBoxList(boxes, event, player)
        if box.rect.collidelist(walls) != -1:
            player.moveBack()
            box.moveBack()
    Utils.detectCollideBoxes(boxes, player, event, walls)
    pygame.display.flip()
pygame.quit()
