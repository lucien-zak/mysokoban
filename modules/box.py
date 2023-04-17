import pygame
from pygame.locals import *


class Box():

    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

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

