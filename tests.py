import unittest
import pygame
from grid import Grid


class Tests(unittest.TestCase):
    global screen
    screen = pygame.display.set_mode((100, 100))

    def test_calculate_rows(self):
        grid = Grid(screen, 10, 10, 5)
        self.assertEqual(grid.calculate_rows(), 6)
        grid = Grid(screen, 10, 20, 5)
        self.assertEqual(grid.calculate_rows(), 3)

    def test_calculate_columns(self):
        grid = Grid(screen, 10, 10, 5)
        self.assertEqual(grid.calculate_columns(), 6)
        grid = Grid(screen, 20, 10, 5)
        self.assertEqual(grid.calculate_columns(), 3)

    def test_create_fields(self):
        grid = Grid(screen, 10, 10, 5)
        self.assertEqual(len(grid.fields), grid.rows)
        self.assertEqual(len(grid.fields[0]), grid.columns)
    
    def test_field_survives(self):
        grid = Grid(screen, 10, 10, 5)
        grid.fields[1][1].set_alive()
        grid.fields[1][2].set_alive()
        grid.fields[2][1].set_alive()
        grid.field_survives(1, 1)
        self.assertTrue(not grid.fields[1][1].is_dead)
    
    def test_field_survives_dead(self):
        grid = Grid(screen, 10, 10, 5)
        grid.fields[1][1].set_alive()
        grid.fields[1][2].set_alive()
        grid.fields[2][1].set_alive()
        grid.field_survives(0, 0)
        self.assertTrue(grid.fields[0][0].is_dead)


if __name__ == "__main__":
    unittest.main()
