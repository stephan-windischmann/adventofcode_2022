from unittest import TestCase

from adventofcode import day5


class Test(TestCase):
    def test_solve_part1(self):
        s, commands = day5.load_input("../input/day5/input_test")
        r: str = day5.solve_part1(s, commands)
        self.assertEqual("CMZ", r)

    def test_solve_part2(self):
        s, commands = day5.load_input("../input/day5/input_test")
        r: str = day5.solve_part2(s, commands)
        self.assertEqual("MCD", r)
