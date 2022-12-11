from unittest import TestCase

from adventofcode import day7


class Test(TestCase):
    def test_solve_part1(self):
        commands: list[str] = day7.load_input("../input/day7/input_test")
        r: int = day7.solve_part1(commands)
        self.assertEqual(95437, r)

    def test_solve_part2(self):
        commands: list[str] = day7.load_input("../input/day7/input_test")
        r: int = day7.solve_part2(commands)
        self.assertEqual(24933642, r)
