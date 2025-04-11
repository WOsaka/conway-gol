import unittest
from grid import Grid


class Tests(unittest.TestCase):
    def test_grid_initialization(self):
        grid = Grid(None, 100, 100, 10, 10, 5)
        self.assertEqual(grid.width, 100)
        self.assertEqual(grid.heigth, 100)
        self.assertEqual(grid.field_width, 10)
        self.assertEqual(grid.field_heigth, 10)
        self.assertEqual(grid.padding, 5)

    def test_calculate_rows(self):
        grid = Grid(None, 100, 100, 10, 10, 5)
        self.assertEqual(grid.calculate_rows(), 6)
        grid = Grid(None, 100, 100, 10, 20, 5)
        self.assertEqual(grid.calculate_rows(), 3)

    def test_calculate_columns(self):
        grid = Grid(None, 100, 100, 10, 10, 5)
        self.assertEqual(grid.calculate_columns(), 6)
        grid = Grid(None, 100, 100, 20, 10, 5)
        self.assertEqual(grid.calculate_columns(), 3)

    def test_create_fields(self):
        grid = Grid(None, 100, 100, 10, 10, 5)
        self.assertEqual(len(grid.fields), grid.rows)
        self.assertEqual(len(grid.fields[0]), grid.columns)


if __name__ == "__main__":
    unittest.main()
