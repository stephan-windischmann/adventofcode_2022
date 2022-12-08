from unittest import TestCase

from adventofcode import day6


class Test(TestCase):
    def test_solve_part1(self):
        r: int = day6.solve_part1("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(5, r)

        r: int = day6.solve_part1("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(6, r)

        r: int = day6.solve_part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(10, r)

        r: int = day6.solve_part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(11, r)

    def test_solve_part2(self):
        r: int = day6.solve_part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
        self.assertEqual(19, r)

        r: int = day6.solve_part2("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(23, r)

        r: int = day6.solve_part2("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(23, r)

        r: int = day6.solve_part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(29, r)

        r: int = day6.solve_part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(26, r)
