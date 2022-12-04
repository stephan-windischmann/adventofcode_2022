from unittest import TestCase

from adventofcode import day2


class Test(TestCase):
    def test_solve_part1(self):
        data: list[str] = day2.load_input("../input/day2/input_test")
        r: int = day2.solve_part1(data)
        self.assertEqual(15, r)

    def test_solve_part2(self):
        data: list[str] = day2.load_input("../input/day2/input_test")
        r: int = day2.solve_part2(data)
        self.assertEqual(12, r)
