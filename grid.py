import pygame
import time
from rectangle import Rectangle


class Grid:
    def __init__(self, screen, field_width, field_heigth, padding):
        self.screen = screen
        self.width = screen.get_width()
        self.heigth = screen.get_height()
        self.field_heigth = field_heigth
        self.field_width = field_width
        self.padding = padding
        self.rows = self.calculate_rows()
        self.columns = self.calculate_columns()
        self.fields = []

        self.create_fields()

    def draw(self):
        for row in self.fields:
            for field in row:
                field.draw()

    def create_fields(self):
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(
                    Rectangle(
                        self.screen,
                        self.padding + (self.padding + self.field_width) * j,
                        self.padding + (self.padding + self.field_heigth) * i,
                        self.field_width,
                        self.field_heigth,
                    )
                )
            self.fields.append(row)

    def set_field_alive(self, row, column):
        self.fields[row][column].set_alive()

    def set_field_dead(self, row, column):
        self.fields[row][column].set_dead()

    def calculate_rows(self):
        rows = (self.heigth - self.padding) // (self.field_heigth + self.padding)
        return rows

    def calculate_columns(self):
        columns = (self.width - self.padding) // (self.field_width + self.padding)
        return columns
