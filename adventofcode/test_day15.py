from unittest import TestCase

from adventofcode import day15


class Test(TestCase):
    def test_solve_part1(self):
        data: list[str] = day15.load_input("../input/day15/input_test")
        r: int = day15.solve_part1(data, row=10)
        self.assertEqual(26, r)

    def test_solve_part2(self):
        data: list[str] = day15.load_input("../input/day15/input_test")
        r: int = day15.solve_part2(data, max_x=20, max_y=20)
        self.assertEqual(56000011, r)
