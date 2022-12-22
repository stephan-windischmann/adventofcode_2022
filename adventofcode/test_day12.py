from unittest import TestCase

from adventofcode import day12


class Test(TestCase):
    def test_solve_part1(self):
        heightmap: list[list[str]] = day12.load_input("../input/day12/input_test")
        r: int = day12.solve_part1(heightmap)
        self.assertEqual(31, r)

    def test_solve_part2(self):
        heightmap: list[list[str]] = day12.load_input("../input/day12/input_test")
        r: int = day12.solve_part2(heightmap)
        self.assertEqual(29, r)
