import pygame


class Rectangle:
    def __init__(self, screen, x, y, width, height, color=(255, 255, 255)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(
            self.screen, self.color, (self.x, self.y, self.width, self.height)
        )
