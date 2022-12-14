from unittest import TestCase

from adventofcode import day9


class Test(TestCase):
    def test_solve_part1(self):
        data: list[str] = day9.load_input("../input/day9/input_test")
        r: int = day9.solve_part1(data)
        self.assertEqual(13, r)

    def test_solve_part2(self):
        data: list[str] = day9.load_input("../input/day9/input_test")
        r: int = day9.solve_part2(data)
        self.assertEqual(1, r)

        data: list[str] = day9.load_input("../input/day9/input_test_2")
        r: int = day9.solve_part2(data)
        self.assertEqual(36, r)
