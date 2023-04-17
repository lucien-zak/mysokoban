import pygame
from pygame.locals import *
from modules.player import Player
from modules.box import Box

pygame.init()
screen = pygame.display.set_mode((1024, 720))
player = Player(100, 100, 50, 50, (255, 0, 0), screen)
box1 = Box(100, 200, 50, 50, (0, 0, 255), screen)
box2 = Box(100, 300, 50, 50, (0, 0, 255), screen)
boxes = [box1, box2]

running = 1

def detectCollideBoxes(boxes):
    for box in boxes:
        for box2 in boxes:
            if box != box2 and box.rect.colliderect(box2.rect):
                print("collide")
                box2.move(event)
                return
                

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
    player.detectAndMoveIfCollide(boxes, event)
    detectCollideBoxes(boxes)    
    pygame.display.flip()
pygame.quit()
