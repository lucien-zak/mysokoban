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
    ['.', '.', '.','.', 'W', 'W','W', 'W', 'W','.','.','.','.','.','.','.','.','.',],
    ['.', '.', '.','.', 'W', '.','.', '.', 'W','.','.','.','.','.','.','.','.','.',],
    ['.', '.', 'W','W', 'W', '.','P', '.', 'W','W','.','.','.','.','.','.','.','.',],
    ['.', '.', 'W','.', '.', '.','.', 'B', '.','W','.','.','.','.','.','.','.','.',],
    ['W', 'W', 'W','.', 'W', '.','W', 'W', '.','W','.','.','W','W','W','W','W','W',],
    ['W', '.', '.','.', 'W', '.','W', 'W', '.','W','W','W','W','.','.','.','H','W',],
    ['W', '.', '.','.', '.', 'B','.', '.', '.','.','.','.','.','.','.','.','H','W',],
    ['W', 'W', 'W','W', '.', '.','.', '.', '.','B','.','.','.','.','.','.','H','W',],
    ['.', '.', '.','W', '.', 'B','W', 'W', 'W','.','.','W','W','.','.','.','H','W',],
    ['.', '.', '.','W', '.', '.','.', '.', '.','.','.','W','W','W','W','W','W','W',],
    ['.', '.', '.','W', 'W', 'W','W', 'W', 'W','.','.','W','.','.','.','.','.','.',],
    ['.', '.', '.','.', '.', '.','.', '.', '.','W','W','.','.','.','.','.','.','.',],

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
                wall = Wall((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50, 'black', screen)
                walls.append(wall)
            if char == 'H':
                hole = Hole((nbCol - 1) * 50, (nbRow - 1) * 50, 50, screen)
                holes.append(hole)
            if char == 'B':
                box = Box((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50, (0, random.randrange(0, 255), 255), screen)
                boxes.append(box)
            if char == 'P':
                player = Player((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50, (255, 0, 0), screen)
    return nbRow, nbCol, walls, boxes, holes, player



running = 1

boxInHole = []

def gameLoop():
    global boxInHole

    nbRow, nbCol, walls, boxes, holes, player = generateMaps(MAPS)

    while running:
        screen.fill((120, 120, 120))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            else:
                player.move(event)
        Utils.detectCollideBoxes(boxes, player, event, walls)
        for hole in holes:
            hole.draw()
            isInHole, indexBox = hole.boxIsOnHole(boxes)
            if isInHole:
                print(indexBox)
                
                boxInHole.append(indexBox)
                boxes.pop(indexBox - 1)
                hole.validateHole()
                # if boxInHole == len(boxes):
                #     print('You win')
                #     pygame.quit()    
        for wall in walls:
            wall.draw()
        for box in boxes:
            box.moveIfCollideWithOtherBoxList(boxes, event, player)
            box.draw()
            if box.rect.collidelist(walls) != -1:
                player.moveBack()
                box.moveBack()
        player.draw()
        pygame.display.flip()



while True:
    gameLoop()

