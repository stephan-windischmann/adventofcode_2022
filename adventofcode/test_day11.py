from unittest import TestCase

from adventofcode import day11


class Test(TestCase):
    def test_solve_part1(self):
        monkeys: list[day11.Monkey] = day11.load_input("../input/day11/input_test")
        r: int = day11.solve_part1(monkeys)
        self.assertEqual(10605, r)

    def test_solve_part2(self):
        monkeys: list[day11.Monkey] = day11.load_input("../input/day11/input_test")
        r: int = day11.solve_part2(monkeys)
        self.assertEqual(2713310158, r)
