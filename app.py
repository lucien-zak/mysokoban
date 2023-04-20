import pygame
import random
import os
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
    ['.', '.', '.', '.', 'W', 'W', 'W', 'W', 'W',
        '.', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['.', '.', '.', '.', 'W', '.', '.', '.', 'W',
        '.', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['.', '.', 'W', 'W', 'W', '.', 'P', '.', 'W',
        'W', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['.', '.', 'W', '.', '.', '.', '.', 'B', '.',
        'W', '.', '.', '.', '.', '.', '.', '.', '.',],
    ['W', 'W', 'W', '.', 'W', '.', 'W', 'W', '.',
        'W', '.', '.', 'W', 'W', 'W', 'W', 'W', 'W',],
    ['W', '.', '.', '.', 'W', '.', 'W', 'W', '.',
        'W', 'W', 'W', 'W', '.', '.', '.', 'H', 'W',],
    ['W', '.', '.', '.', '.', 'B', '.', '.', '.',
        '.', '.', '.', '.', '.', '.', '.', 'H', 'W',],
    ['W', 'W', 'W', 'W', '.', '.', '.', '.', '.',
        'B', '.', '.', '.', '.', '.', '.', 'H', 'W',],
    ['.', '.', '.', 'W', '.', 'B', 'W', 'W', 'W',
        '.', '.', 'W', 'W', '.', '.', '.', 'H', 'W',],
    ['.', '.', '.', 'W', '.', '.', '.', '.', '.',
        '.', '.', 'W', 'W', 'W', 'W', 'W', 'W', 'W',],
    ['.', '.', '.', 'W', 'W', 'W', 'W', 'W', 'W',
        '.', '.', 'W', '.', '.', '.', '.', '.', '.',],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.',
        'W', 'W', '.', '.', '.', '.', '.', '.', '.',],

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
                wall = Wall((nbCol - 1) * 50, (nbRow - 1)
                            * 50, 50, 50, 'black', screen)
                walls.append(wall)
            if char == 'H':
                hole = Hole((nbCol - 1) * 50, (nbRow - 1) * 50, 50, screen)
                holes.append(hole)
            if char == 'B':
                box = Box((nbCol - 1) * 50, (nbRow - 1) * 50, 50, 50,
                          (0, random.randrange(0, 255), 255), screen)
                boxes.append(box)
            if char == 'P':
                player = Player((nbCol - 1) * 50, (nbRow - 1)
                                * 50, 50, 50, (255, 0, 0), screen)
    return nbRow, nbCol, walls, boxes, holes, player


running = 1

boxInHole = []


def editorLoop():

    def itemSelector(event):
        items = ['box.png', 'wall.png', 'hole']
        if event.type == KEYDOWN:
            if event.key == pygame.K_1:
                print(items[0])
                return items[0]
            if event.key == K_2:
                return items[1]
            if event.key == K_3:
                return items[2]

        return image

    maps = []
    choosenGrid = pygame.draw.rect(screen, (255, 255, 255), (0, 0, 50, 50), 1)
    items = []
    image = 'box.png'

    while running:
        screen.fill((120, 120, 120))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_e:
                    gameLoop()
            image = itemSelector(event)
        mousPos = pygame.mouse.get_pos()
        if image != 'hole':
            choosenGrid = pygame.draw.rect(
                screen, ('black'), (mousPos[0] - mousPos[0] % 50, mousPos[1] - mousPos[1] % 50, 50, 50), 1)
            choosenGridImage = pygame.transform.scale(
                pygame.image.load(os.path.join("assets", image)), (50, 50))
            screen.blit(
                choosenGridImage, (mousPos[0] - mousPos[0] % 50, mousPos[1] - mousPos[1] % 50))
        else:
            choosenGrid = pygame.draw.circle(
                screen, (0, 0, 0), (mousPos[0] - mousPos[0] % 50 + 25, mousPos[1] - mousPos[1] % 50 + 25), 25)
        if pygame.mouse.get_pressed()[0]:
            if image != 'hole':
                items.append([image, mousPos[0] - mousPos[0] %
                             50, mousPos[1] - mousPos[1] % 50])
            else:
                items.append([image, mousPos[0] - mousPos[0] %
                             50 + 25, mousPos[1] - mousPos[1] % 50 + 25])
        for item in items:
            if item[0] != 'hole':
                itemImage = pygame.transform.scale(pygame.image.load(
                    os.path.join("assets", item[0])), (50, 50))
                screen.blit(itemImage, (item[1], item[2]))
            else:
                pygame.draw.circle(screen, (0, 0, 0), (item[1], item[2]), 25)
        pygame.display.flip()


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
    fonts = pygame.font.get_fonts()
    font = pygame.font.SysFont('arial', 30)
    text = font.render('Appuiyer sur G pour lancer le jeu',
                       True, (255, 255, 255))
    text1 = font.render('Appuyer sur E pour lancer l\'editeur', True, (255, 255, 255))
    text2 = font.render('Appuyer sur Echap pour quitter', True, (255, 255, 255))
    screen.blit(text, (WIDTH / 2 - 150, HEIGHT / 2 - 50))
    screen.blit(text1, (WIDTH / 2 - 150, HEIGHT / 2))
    screen.blit(text2, (WIDTH / 2 - 150, HEIGHT / 2 + 50))
    # screen.fill((120, 120, 120))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_e:
                editorLoop()
            if event.key == K_g:
                gameLoop()
    pygame.display.flip()
