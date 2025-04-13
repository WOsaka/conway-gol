import pygame
import time
from rectangle import Rectangle
from field_status import FieldStatus


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
        self.set_border_dead()

    def compute_next_generation(self):
        fields_statuses = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                field_status = self.get_field_status_next_gen(i, j)
                if field_status == FieldStatus.DEAD:
                    row.append(True)
                elif field_status == FieldStatus.COPY:
                    row.append(self.fields[i][j].is_dead)
                elif field_status == FieldStatus.ALIVE:
                    row.append(False)
            fields_statuses.append(row)

        for i in range(self.rows):
            for j in range(self.columns):
                living_status = fields_statuses[i][j]
                self.fields[i][j].is_dead = living_status

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

    def get_field_status_next_gen(self, row, column):
        """
        Returns the status of the field in the next generation.
        :param row: Row of the field.
        :param column: Column of the field.
        :return: The status of the field in the next generation.
        """
        living_neighbor = 0
        if 0 < row < self.rows - 1 and 0 < column < self.columns - 1:
            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    if i == row and j == column:
                        continue
                    if not self.fields[i][j].is_dead:
                        living_neighbor += 1
        if living_neighbor < 2 or 3 < living_neighbor:
            return FieldStatus.DEAD
        elif living_neighbor == 3:
            return FieldStatus.ALIVE
        else:
            return FieldStatus.COPY

    def set_border_dead(self):
        for i in range(self.columns):
            self.set_field_dead(0, i)
            self.set_field_dead(self.rows - 1, i)

        for i in range(self.rows):
            self.set_field_dead(i, 0)
            self.set_field_dead(i, self.columns - 1)
