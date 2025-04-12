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

    def change_fields_living_status(self, mouseclick_event):
        row, column = self.compute_clicked_field(mouseclick_event.pos)
        print("row, column:", self.compute_clicked_field(mouseclick_event.pos))
        if self.fields[row][column].is_dead:
            self.set_field_alive(row, column)
        elif not self.fields[row][column].is_dead:
            self.set_field_dead(row, column)

    def compute_clicked_field(self, event):
        x, y = event
        column = (x - self.padding) // (self.field_width + self.padding)
        row = (y - self.padding) // (self.field_heigth + self.padding)
        return row, column

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
