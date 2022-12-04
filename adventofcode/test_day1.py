from unittest import TestCase

from adventofcode import day1


class Test(TestCase):
    def test_solve_part1(self):
        data: list[list[int]] = day1.load_input("../input/day1/input_test")
        r: int = day1.solve_part1(data)
        self.assertEqual(24000, r)

    def test_solve_part2(self):
        data: list[list[int]] = day1.load_input("../input/day1/input_test")
        r: int = day1.solve_part2(data)
        self.assertEqual(45000, r)
