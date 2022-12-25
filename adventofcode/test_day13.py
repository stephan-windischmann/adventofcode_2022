from unittest import TestCase

from adventofcode import day13


class Test(TestCase):
    def test_solve_part1(self):
        data = day13.load_input("../input/day13/input_test")
        r: int = day13.solve_part1(data)
        self.assertEqual(13, r)

    def test_solve_part2(self):
        data = day13.load_input("../input/day13/input_test")
        r: int = day13.solve_part2(data)
        self.assertEqual(140, r)
