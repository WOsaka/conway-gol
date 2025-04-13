from rectangle import Rectangle
import pygame


class Pattern:
    def __init__(self, grid):
        self._grid = grid
        self.screen = grid.screen
        self._field_height = grid.field_heigth
        self._field_width = grid.field_width
        self._padding = grid.padding
        self._patterns = []
        self._pattern_index = 0

        self.call_add_patter_funcs()

    def set_pattern_in_grid(self, mouseclick_event):
        row, column = self._grid.compute_clicked_field(mouseclick_event.pos)
        print("row, column:", self._grid.compute_clicked_field(mouseclick_event.pos))
        pattern = self._patterns[self._pattern_index]
        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                if 1 == pattern[i][j]:
                    self._grid.set_field_alive(row + i, column + j)

    def draw(self, x, y):
        x -= self._field_width / 2
        y -= self._field_height / 2
        pattern = self._patterns[self._pattern_index]
        for i in range(len(pattern)):
            y += self._padding
            x_tmp = x + self._padding
            for j in range(len(pattern[i])):
                if 1 == pattern[i][j]:
                    pygame.draw.rect(
                        self.screen,
                        (0, 0, 0),
                        (x_tmp, y, self._field_width, self._field_height),
                    )
                x_tmp += self._field_width + self._padding
            x_tmp = 0
            y += self._field_height

    def set_next_pattern(self):
        if self._pattern_index == len(self._patterns) - 1:
            self._pattern_index = 0
        else:
            self._pattern_index += 1

    def set_prev_pattern(self):
        if 0 == self._pattern_index:
            self._pattern_index = len(self._patterns) - 1
        else:
            self._pattern_index -= 1

    def call_add_patter_funcs(self):
        self.add_big_ship()
        self.add_u()
        self.add_glider()
        self.add_blinker()
        self.add_penta_dec()
    

    def add_big_ship(self):
        pattern = [
            [0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 0],
        ]
        self._patterns.append(pattern)

    def add_glider(self):
        pattern = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
        ]
        self._patterns.append(pattern)

    def add_u(self):
        pattern = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        self._patterns.append(pattern)

    def add_blinker(self):
        pattern = [[1], [1], [1]]
        self._patterns.append(pattern)

    def add_penta_dec(self):
        pattern = [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]
        self._patterns.append(pattern)
