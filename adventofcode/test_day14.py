from unittest import TestCase

from adventofcode import day14


class Test(TestCase):
    def test_solve_part1(self):
        m: set[tuple[int, int]] = day14.load_input("../input/day14/input_test")
        r: int = day14.solve_part1(m)
        self.assertEqual(24, r)

    def test_solve_part2(self):
        m: set[tuple[int, int]] = day14.load_input("../input/day14/input_test")
        r: int = day14.solve_part2(m)
        self.assertEqual(93, r)
        