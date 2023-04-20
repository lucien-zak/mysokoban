import pygame

class Hole():
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.color = (0, 0, 0)
        self.width = 25

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x + self.x / 2, self.y + self.y / 2), 25, self.width)

    def boxIsOnHole(self, boxes):
        for box in boxes:
            if box.x == self.x and box.y == self.y:
                return True
        return False