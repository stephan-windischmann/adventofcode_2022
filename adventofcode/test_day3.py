from unittest import TestCase

from adventofcode import day3


class Test(TestCase):
    def test_solve_part1(self):
        data: list[str] = day3.load_input("../input/day3/input_test")
        r: int = day3.solve_part1(data)
        self.assertEqual(157, r)

    def test_solve_part2(self):
        data: list[str] = day3.load_input("../input/day3/input_test")
        r: int = day3.solve_part2(data)
        self.assertEqual(70, r)
