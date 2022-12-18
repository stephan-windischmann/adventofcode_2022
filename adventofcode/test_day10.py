from unittest import TestCase

from adventofcode import day10


class Test(TestCase):
    def test_solve_part1(self):
        commands: list[str] = day10.load_input("../input/day10/input_test")
        r: int = day10.solve_part1(commands)
        self.assertEqual(13140, r)

    def test_solve_part2(self):
        commands: list[str] = day10.load_input("../input/day10/input_test")
        r: list[list[str]] = day10.solve_part2(commands)
        for line in r:
            print("".join(line))
