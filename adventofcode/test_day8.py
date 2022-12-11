from unittest import TestCase

from adventofcode import day8


class Test(TestCase):
    def test_solve_part1(self):
        trees: list[list[int]] = day8.load_input("../input/day8/input_test")
        r: int = day8.solve_part1(trees)
        self.assertEqual(21, r)

    def test_solve_part2(self):
        trees: list[list[int]] = day8.load_input("../input/day8/input_test")
        r: int = day8.solve_part2(trees)
        self.assertEqual(8, r)
