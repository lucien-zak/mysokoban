import pygame

class Hole():
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.color = (0, 0, 0)
        self.width = 25
        self.valided = False

    def draw(self):
        if self.valided:
            self.color = (0, 255, 0)
        pygame.draw.circle(self.screen, self.color, (self.x + self.width, self.y + self.width), 25, self.width)

    def boxIsOnHole(self, boxes):
        i = 0
        if self.valided == True:
            return False, i
        for box in boxes:
            i += 1
            if box.x == self.x and box.y == self.y:
                return True, i
        return False, i
    
    def validateHole(self):
        self.color = (0, 255, 0)
        self.valided = True
    