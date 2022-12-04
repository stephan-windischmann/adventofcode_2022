from unittest import TestCase

from adventofcode import day4


class Test(TestCase):
    def test_solve_part1(self):
        data: list[str] = day4.load_input("../input/day4/input_test")
        r: int = day4.solve_part1(data)
        self.assertEqual(2, r)

    def test_solve_part2(self):
        data: list[str] = day4.load_input("../input/day4/input_test")
        r: int = day4.solve_part2(data)
        self.assertEqual(4, r)
