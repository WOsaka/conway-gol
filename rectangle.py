import pygame


class Rectangle:
    def __init__(self, screen, x, y, width, height, is_dead=True):
        self._screen = screen
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.is_dead = is_dead

    def draw(self):
        if self.is_dead:
            self._color = (255, 255, 255)
        else:
            self._color = (0, 0, 0)

        pygame.draw.rect(
            self._screen, self._color, (self._x, self._y, self._width, self._height)
        )

    
    def set_alive(self):
        if not self.is_dead:
            return
        self.is_dead = False
    
    def set_dead(self):
        if self.is_dead:
            return
        self.is_dead = True
