import pygame
from pygame.locals import *
import os

def loadImages(path):
    images = []
    for file in os.listdir(path):
        if file.endswith(".png"):
            images.append(pygame.image.load(os.path.join(path, file)))
    return images

IMAGES = loadImages("assets")
print(IMAGES)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.image = pygame.transform.scale(IMAGES[0], (self.width, self.height))
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.screen.blit(self.image, self.rect)

    def move(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                 self.x -= 10
            if event.key == K_RIGHT:
                self.x += 10
            if event.key == K_UP:
                self.y -= 10
            if event.key == K_DOWN:
                self.y += 10

    def detectAndMoveIfCollide(self, boxes, event):
        for box in boxes:
            if self.rect.colliderect(box):
                box.move(event)
                pygame.display.flip()
    